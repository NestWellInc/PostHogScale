import json
import os
import re
from dataclasses import asdict, dataclass
from http.server import BaseHTTPRequestHandler
from typing import Any, Dict, List, Optional

from freelancersdk.session import Session
from freelancersdk.resources.projects import search_projects
from freelancersdk.resources.projects.helpers import create_search_projects_filter
from freelancersdk.resources.users import get_self_user_id

TOKEN_ENV = "FLN_OAUTH_TOKEN"

HUMAN_SPECIFIC = [
    r"survey", r"focus group", r"personal experience", r"mystery shop",
    r"video of yourself", r"voice sample", r"record yourself", r"in-person",
    r"on-site", r"onsite", r"captcha", r"different ip", r"human judgment",
]
PROHIBITED = [r"fake review", r"fake account", r"bypass captcha", r"evade", r"private customer database"]
MACHINE_POSITIVE = [
    r"excel", r"csv", r"python", r"data processing", r"data entry", r"data extraction",
    r"data cleansing", r"web scraping", r"mysql", r"automation", r"pdf", r"json", r"xml",
    r"pivot", r"spreadsheet", r"api", r"database", r"vba", r"power automate", r"zapier",
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


def _session() -> Session:
    token = os.environ.get(TOKEN_ENV)
    if not token:
        raise RuntimeError(f"Missing {TOKEN_ENV}")
    return Session(oauth_token=token)


def _has(blob: str, pats: List[str]) -> bool:
    return any(re.search(p, blob, re.I) for p in pats)


def _evaluate(p: Dict[str, Any]) -> Decision:
    blob = f"{p.get('title','')}\n{p.get('description','')}".lower()
    pid = int(p['id'])
    title = p.get('title', '')
    if _has(blob, PROHIBITED):
        return Decision(pid, title, "REJECT", -100, "policy/risk pattern")
    if _has(blob, HUMAN_SPECIFIC):
        return Decision(pid, title, "REJECT", -50, "specifically human/personal work")
    hits = sum(1 for pat in MACHINE_POSITIVE if re.search(pat, blob, re.I))
    score = hits * 3
    bid_stats = p.get('bid_stats') or {}
    bid_count = bid_stats.get('bid_count') or 0
    score += max(0, 10 - min(10, bid_count / 3))
    budget = p.get('budget') or {}
    minimum = budget.get('minimum')
    maximum = budget.get('maximum')
    if maximum:
        score += min(float(maximum), 300) / 30
    if hits < 2:
        return Decision(pid, title, "REVIEW", score, "machine suitability not strong enough")
    amount = float(maximum or minimum or 20)
    if maximum is not None and minimum is not None:
        amount = round(float(minimum) + 0.55 * (float(maximum) - float(minimum)), 2)
    period = 3 if any(k in blob for k in ["automation", "script", "mysql", "database"]) else 1
    return Decision(pid, title, "GREEN_GATE", score, "objective machine-executable deliverable", amount, period)


def run(limit: int = 25):
    s = _session()
    user_id = get_self_user_id(s)
    sf = create_search_projects_filter(sort_field="time_updated", or_search_query=True, languages="en")
    result = search_projects(
        s,
        query="Excel CSV Python data automation",
        search_filter=sf,
        active_only=True,
        limit=limit,
    )
    projects = result.get("projects", []) if isinstance(result, dict) else []
    decisions = sorted((_evaluate(p) for p in projects), key=lambda d: d.score, reverse=True)
    return {
        "ok": True,
        "authenticated_user_id": user_id,
        "mode": "DRY_RUN",
        "projects_seen": len(projects),
        "green_count": sum(d.verdict == "GREEN_GATE" for d in decisions),
        "decisions": [asdict(d) for d in decisions[:20]],
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
