import json
import os
import re
from dataclasses import asdict, dataclass
from http.server import BaseHTTPRequestHandler
from typing import Any, Dict, List, Optional

from freelancersdk.session import Session
from freelancersdk.resources.projects import search_projects
from freelancersdk.resources.projects.helpers import (
    create_get_projects_project_details_object,
    create_search_projects_filter,
)
from freelancersdk.resources.users import get_self_user_id

TOKEN_ENV = "FLN_OAUTH_TOKEN"

HUMAN_SPECIFIC = [
    r"survey", r"focus group", r"personal experience", r"mystery shop",
    r"video of yourself", r"voice sample", r"record yourself", r"in-person",
    r"on-site", r"onsite", r"captcha", r"different ip", r"human judgment",
    r"manual only", r"no automation", r"no scripts", r"must be done manually",
    r"phone calls?", r"cold call", r"appointment setter", r"virtual assistant",
    r"local candidate", r"must be located", r"onsite required",
]

PROHIBITED = [
    r"fake review", r"fake account", r"bypass captcha", r"evade",
    r"private customer database", r"different ip addresses", r"account farming",
    r"credential stuffing", r"scrape.*login", r"bypass.*paywall",
]

# Anything here is never autonomously bid during the proof stage. It may still be reviewed later.
REVIEW_ONLY = [
    r"illustrat", r"logo", r"flyer", r"graphic design", r"book cover", r"video ad",
    r"copywrit", r"seo", r"social media", r"marketing", r"lead gen", r"lead generation",
    r"lead sourcing", r"prospect", r"sales leads?", r"contact list", r"email list",
    r"bookkeep", r"accounting", r"financial advice", r"investment", r"forex", r"trading bot",
    r"crypto", r"gold trading", r"stock trading", r"legal", r"medical", r"architect",
    r"civil engineer", r"storm water", r"mobile app", r"flutter", r"react native",
    r"full.?stack", r"web development", r"website development", r"e.?commerce store",
    r"tensorflow", r"machine learning model", r"llm application", r"ai agent developer",
    r"business assistant", r"file management assistant", r"secretarial", r"product description",
    r"dashboard.*analysis", r"analysis dashboard", r"review visualization",
    r"supplier.*api bridge", r"api bridge", r"manufacturing lead",
]

# Initial autonomous whitelist: deliberately boring, deterministic data/file operations.
CORE_CLASSES = [
    r"(?:clean|cleaning|cleanse|cleansing).*(?:excel|csv|spreadsheet|data)",
    r"(?:excel|csv|spreadsheet|data).*(?:clean|cleaning|cleanse|cleansing)",
    r"deduplic|de-duplic|remove duplicates?",
    r"normaliz|reconcil|standardiz",
    r"pdf.*(?:excel|csv|spreadsheet|table|extract)",
    r"(?:excel|csv|spreadsheet|table).*pdf",
    r"(?:extract|extraction).*(?:excel|csv|spreadsheet|table|structured data)",
    r"(?:excel|csv|spreadsheet).*(?:extract|extraction|transform|conversion|convert)",
    r"(?:csv|excel|spreadsheet).*(?:format|formatting|merge|combine|consolidat)",
    r"(?:merge|combine|consolidat).*(?:csv|excel|spreadsheet)",
    r"(?:excel|csv).*(?:mysql|database).*(?:import|insert|update|upsert|sync)",
    r"(?:mysql|database).*(?:excel|csv).*(?:import|insert|update|upsert|sync)",
    r"(?:json|xml).*(?:csv|excel|transform|convert)",
    r"(?:csv|excel).*(?:json|xml|transform|convert)",
]

AUTOMATION_INTENT = [
    r"automate", r"automation", r"unattended", r"script", r"python", r"vba",
    r"power automate", r"zapier", r"scheduled", r"daily", r"batch", r"pipeline",
]

@dataclass
class Decision:
    project_id: int
    title: str
    verdict: str
    score: float
    reason: str
    bid_amount: Optional[float] = None
    period_days: Optional[int] = None
    core_hits: Optional[int] = None
    automation_hits: Optional[int] = None
    currency_code: Optional[str] = None


def _session() -> Session:
    token = os.environ.get(TOKEN_ENV)
    if not token:
        raise RuntimeError(f"Missing {TOKEN_ENV}")
    return Session(oauth_token=token)


def _has(blob: str, pats: List[str]) -> bool:
    return any(re.search(p, blob, re.I | re.S) for p in pats)


def _count(blob: str, pats: List[str]) -> int:
    return sum(1 for p in pats if re.search(p, blob, re.I | re.S))


def _evaluate(p: Dict[str, Any]) -> Decision:
    blob = f"{p.get('title','')}\n{p.get('description','')}".lower()
    pid = int(p['id'])
    title = p.get('title', '')
    currency = p.get('currency') or {}
    currency_code = currency.get('code') if isinstance(currency, dict) else None

    if _has(blob, PROHIBITED):
        return Decision(pid, title, "REJECT", -100, "policy/risk pattern", currency_code=currency_code)
    if _has(blob, HUMAN_SPECIFIC):
        return Decision(pid, title, "REJECT", -50, "specifically human/manual/location work", currency_code=currency_code)
    if _has(blob, REVIEW_ONLY):
        return Decision(pid, title, "REVIEW", 0, "outside proof-stage autonomous data-work envelope", currency_code=currency_code)

    core_hits = _count(blob, CORE_CLASSES)
    automation_hits = _count(blob, AUTOMATION_INTENT)
    bid_stats = p.get('bid_stats') or {}
    bid_count = int(bid_stats.get('bid_count') or 0)

    # Competition only matters after the work itself passes the whitelist.
    score = core_hits * 12 + automation_hits * 2 + max(0, 6 - min(6, bid_count / 5))

    if core_hits < 1:
        return Decision(
            pid, title, "REVIEW", score,
            "no exact proof-stage data/file work class matched",
            core_hits=core_hits, automation_hits=automation_hits,
            currency_code=currency_code,
        )

    # Broad deliverables are review-only even if a sentence happens to mention CSV/Excel.
    if _has(blob, [
        r"build (?:a |an )?(?:website|platform|application|app|system)",
        r"develop (?:a |an )?(?:website|platform|application|app)",
        r"end[- ]to[- ]end (?:application|platform|system)",
    ]):
        return Decision(
            pid, title, "REVIEW", score,
            "broad build scope despite data keywords",
            core_hits=core_hits, automation_hits=automation_hits,
            currency_code=currency_code,
        )

    budget = p.get('budget') or {}
    minimum = budget.get('minimum')
    maximum = budget.get('maximum')
    amount = float(maximum or minimum or 20)
    if maximum is not None and minimum is not None:
        # Conservative proof-stage bid, in the project's own currency.
        amount = round(float(minimum) + 0.25 * (float(maximum) - float(minimum)), 2)

    period = 3 if automation_hits >= 2 or _has(blob, [r"mysql", r"database", r"pipeline"]) else 1
    return Decision(
        pid, title, "AUTO_BID_READY", score,
        "exact deterministic data/file work class matched",
        amount, period, core_hits, automation_hits, currency_code,
    )


def run(limit: int = 60):
    s = _session()
    user_id = get_self_user_id(s)

    sf = create_search_projects_filter(
        sort_field="time_updated",
        reverse_sort=True,
        or_search_query=True,
    )
    pd = create_get_projects_project_details_object(
        full_description=True,
        jobs=True,
        upgrades=True,
    )

    result = search_projects(
        s,
        query="Excel CSV spreadsheet data cleaning data extraction PDF conversion deduplicate normalize reconcile merge transform",
        search_filter=sf,
        project_details=pd,
        active_only=True,
        limit=limit,
    )
    projects = result.get("projects", []) if isinstance(result, dict) else []
    decisions = sorted((_evaluate(p) for p in projects), key=lambda d: d.score, reverse=True)
    ready = [d for d in decisions if d.verdict == "AUTO_BID_READY"]

    return {
        "ok": True,
        "authenticated_user_id": user_id,
        "mode": "DRY_RUN_CORE_DATA_ONLY",
        "projects_seen": len(projects),
        "auto_bid_ready_count": len(ready),
        "auto_bid_ready": [asdict(d) for d in ready[:15]],
        "top_decisions": [asdict(d) for d in decisions[:30]],
    }


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            payload = run()
            code = 200
        except Exception as exc:
            payload = {"ok": False, "error_type": type(exc).__name__, "error": str(exc)[:500]}
            code = 500
        body = json.dumps(payload, default=str).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)
