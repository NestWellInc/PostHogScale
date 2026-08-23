import json
import os
import re
from dataclasses import asdict, dataclass
from http.server import BaseHTTPRequestHandler
from typing import Any, Dict, List, Optional

from freelancersdk.session import Session
from freelancersdk.resources.projects import get_bids, place_project_bid, search_projects
from freelancersdk.resources.projects.helpers import (
    create_get_projects_project_details_object,
    create_search_projects_filter,
)
from freelancersdk.resources.users import get_self_user_id

TOKEN_ENV = "FLN_OAUTH_TOKEN"
LIVE_ENV = "FLN_LIVE_BID"
MAX_BIDS_PER_RUN = 1

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

REVIEW_ONLY = [
    r"illustrat", r"logo", r"flyer", r"graphic design", r"book cover", r"video ad",
    r"copywrit", r"seo", r"social media", r"marketing", r"lead gen", r"lead generation",
    r"lead sourcing", r"prospect", r"sales leads?", r"contact list", r"email list",
    r"bookkeep", r"accounting", r"financial advice", r"investment", r"forex", r"trading bot",
    r"crypto", r"gold trading", r"stock trading", r"legal", r"medical", r"architect",
    r"civil engineer", r"storm water", r"mobile app", r"flutter", r"react native",
    r"full.?stack", r"web development", r"website development", r"wordpress", r"theme",
    r"e.?commerce store", r"tensorflow", r"machine learning model", r"llm application",
    r"ai agent developer", r"business assistant", r"file management assistant", r"secretarial",
    r"product description", r"dashboard", r"visualization", r"visualisation", r"analysis",
    r"supplier.*api bridge", r"api bridge", r"manufacturing lead", r"hla accuracy",
]

TITLE_CORE = [
    r"\b(?:excel|csv|spreadsheet)\b.*\b(?:clean|cleanup|cleansing|format|formatting|merge|combine|consolidat|convert|conversion|transform|deduplic|duplicate|normalize|standardiz|reconcil|extract|extraction|entry|import|export)\b",
    r"\b(?:clean|cleanup|cleansing|format|formatting|merge|combine|consolidat|convert|conversion|transform|deduplic|duplicate|normalize|standardiz|reconcil|extract|extraction|entry|import|export)\b.*\b(?:excel|csv|spreadsheet)\b",
    r"\bpdf\b.*\b(?:excel|csv|table|extract|extraction|convert|conversion)\b",
    r"\b(?:excel|csv|table)\b.*\bpdf\b",
    r"\bdata\s+(?:cleaning|cleansing|entry|extraction|conversion|transformation|deduplication|normalization|reconciliation)\b",
]

CORE_CLASSES = [
    r"(?:clean|cleaning|cleanse|cleansing).*(?:excel|csv|spreadsheet|data)",
    r"(?:excel|csv|spreadsheet|data).*(?:clean|cleaning|cleanse|cleansing)",
    r"deduplic|de-duplic|remove duplicates?", r"normaliz|reconcil|standardiz",
    r"pdf.*(?:excel|csv|spreadsheet|table|extract)", r"(?:excel|csv|spreadsheet|table).*pdf",
    r"(?:extract|extraction).*(?:excel|csv|spreadsheet|table|structured data)",
    r"(?:excel|csv|spreadsheet).*(?:extract|extraction|transform|conversion|convert)",
    r"(?:csv|excel|spreadsheet).*(?:format|formatting|merge|combine|consolidat)",
    r"(?:merge|combine|consolidat).*(?:csv|excel|spreadsheet)",
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
    title_hits: Optional[int] = None
    core_hits: Optional[int] = None
    automation_hits: Optional[int] = None
    currency_code: Optional[str] = None
    description_excerpt: Optional[str] = None
    already_bid: Optional[bool] = None


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
    title = p.get('title', '') or ''
    description = p.get('description', '') or ''
    blob = f"{title}\n{description}".lower()
    title_l = title.lower()
    pid = int(p['id'])
    currency = p.get('currency') or {}
    currency_code = currency.get('code') if isinstance(currency, dict) else None
    excerpt = re.sub(r"\s+", " ", description).strip()[:420]

    if _has(blob, PROHIBITED):
        return Decision(pid, title, "REJECT", -100, "policy/risk pattern", currency_code=currency_code, description_excerpt=excerpt)
    if _has(blob, HUMAN_SPECIFIC):
        return Decision(pid, title, "REJECT", -50, "specifically human/manual/location work", currency_code=currency_code, description_excerpt=excerpt)
    if _has(blob, REVIEW_ONLY):
        return Decision(pid, title, "REVIEW", 0, "outside proof-stage autonomous data-work envelope", currency_code=currency_code, description_excerpt=excerpt)

    title_hits = _count(title_l, TITLE_CORE)
    core_hits = _count(blob, CORE_CLASSES)
    automation_hits = _count(blob, AUTOMATION_INTENT)
    bid_stats = p.get('bid_stats') or {}
    bid_count = int(bid_stats.get('bid_count') or 0)
    score = title_hits * 25 + core_hits * 10 + automation_hits * 2 + max(0, 5 - min(5, bid_count / 5))

    if title_hits < 1:
        return Decision(pid, title, "REVIEW", score, "title is not an exact proof-stage data/file work class", title_hits=title_hits, core_hits=core_hits, automation_hits=automation_hits, currency_code=currency_code, description_excerpt=excerpt)
    if core_hits < 1:
        return Decision(pid, title, "REVIEW", score, "description does not confirm deterministic data/file scope", title_hits=title_hits, core_hits=core_hits, automation_hits=automation_hits, currency_code=currency_code, description_excerpt=excerpt)
    if _has(blob, [r"manual data entry", r"manual text data entry", r"type.*manually", r"human data entry"]):
        return Decision(pid, title, "REVIEW", score, "manual-entry wording requires human review", title_hits=title_hits, core_hits=core_hits, automation_hits=automation_hits, currency_code=currency_code, description_excerpt=excerpt)

    budget = p.get('budget') or {}
    minimum = budget.get('minimum')
    maximum = budget.get('maximum')
    amount = float(maximum or minimum or 20)
    if maximum is not None and minimum is not None:
        amount = round(float(minimum) + 0.20 * (float(maximum) - float(minimum)), 2)

    period = 3 if automation_hits >= 2 else 1
    return Decision(pid, title, "AUTO_BID_READY", score, "title and description both match deterministic proof-stage data/file work", amount, period, title_hits, core_hits, automation_hits, currency_code, excerpt)


def _proposal(d: Decision) -> str:
    return (
        f"I can complete the {d.title} work with a deterministic, validation-first workflow. "
        "I will structure and process the supplied data, preserve the requested output format, "
        "check for duplicates/formatting issues, and run reconciliation checks before delivery. "
        "You will receive the completed file plus a concise note describing any assumptions or exceptions."
    )


def _already_bid(session: Session, project_id: int, bidder_id: int) -> bool:
    result = get_bids(session, project_ids=[project_id], limit=100, offset=0)
    bids = result.get("bids", []) if isinstance(result, dict) else []
    return any(int(b.get("bidder_id") or 0) == int(bidder_id) and not b.get("retracted") for b in bids)


def _place_one(session: Session, bidder_id: int, d: Decision) -> Dict[str, Any]:
    if _already_bid(session, d.project_id, bidder_id):
        d.already_bid = True
        return {"project_id": d.project_id, "status": "SKIPPED_ALREADY_BID"}
    d.already_bid = False
    bid = place_project_bid(
        session,
        project_id=d.project_id,
        bidder_id=bidder_id,
        description=_proposal(d),
        amount=d.bid_amount,
        period=d.period_days or 1,
        milestone_percentage=100,
    )
    return {"project_id": d.project_id, "status": "BID_PLACED", "bid_id": getattr(bid, "id", None), "amount": d.bid_amount, "currency_code": d.currency_code}


def run(limit: int = 75, execute: bool = False):
    s = _session()
    user_id = get_self_user_id(s)
    sf = create_search_projects_filter(sort_field="time_updated", reverse_sort=True, or_search_query=True)
    pd = create_get_projects_project_details_object(full_description=True, jobs=True, upgrades=True)
    result = search_projects(
        s,
        query="Excel CSV spreadsheet data cleaning data entry data extraction PDF conversion deduplicate normalize reconcile merge transform",
        search_filter=sf,
        project_details=pd,
        active_only=True,
        limit=limit,
    )
    projects = result.get("projects", []) if isinstance(result, dict) else []
    decisions = sorted((_evaluate(p) for p in projects), key=lambda d: d.score, reverse=True)
    ready = [d for d in decisions if d.verdict == "AUTO_BID_READY"]

    # Enrich only the tiny ready set with duplicate-bid state.
    for d in ready[:10]:
        try:
            d.already_bid = _already_bid(s, d.project_id, user_id)
        except Exception:
            d.already_bid = None

    live_enabled = os.environ.get(LIVE_ENV, "").strip().lower() in {"1", "true", "yes", "on"}
    actions: List[Dict[str, Any]] = []
    if execute and live_enabled:
        for d in ready:
            if len([a for a in actions if a.get("status") == "BID_PLACED"]) >= MAX_BIDS_PER_RUN:
                break
            if d.already_bid:
                continue
            actions.append(_place_one(s, user_id, d))

    return {
        "ok": True,
        "authenticated_user_id": user_id,
        "mode": "LIVE_ARMED" if live_enabled else "DRY_RUN_DUPLICATE_SAFE",
        "execute_requested": execute,
        "live_enabled": live_enabled,
        "max_bids_per_run": MAX_BIDS_PER_RUN,
        "projects_seen": len(projects),
        "auto_bid_ready_count": len(ready),
        "auto_bid_ready": [asdict(d) for d in ready[:10]],
        "actions": actions,
        "top_decisions": [asdict(d) for d in decisions[:20]],
    }


class handler(BaseHTTPRequestHandler):
    def _respond(self, execute: bool):
        try:
            payload = run(execute=execute)
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

    def do_GET(self):
        self._respond(execute=False)

    def do_POST(self):
        self._respond(execute=True)
