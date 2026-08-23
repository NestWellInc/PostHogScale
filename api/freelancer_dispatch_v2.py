import json
import os
import re
from dataclasses import asdict, dataclass
from http.server import BaseHTTPRequestHandler
from typing import Any, Dict, List, Optional

from freelancersdk.session import Session
from freelancersdk.resources.projects import get_bids, place_project_bid, search_projects
from freelancersdk.resources.projects.helpers import create_get_projects_project_details_object, create_search_projects_filter
from freelancersdk.resources.users import get_self_user_id

TOKEN_ENV = "FLN_OAUTH_TOKEN"
LIVE_ENV = "FLN_LIVE_BID"
MAX_BIDS_PER_RUN = 1
SEARCH_QUERIES = [
    "Excel cleanup CSV conversion spreadsheet merge deduplicate",
    "PDF to Excel CSV table extraction",
    "spreadsheet normalize reconcile transform consolidate",
]

BLOCK = [
    r"survey", r"focus group", r"personal experience", r"mystery shop", r"in-person", r"on-site", r"onsite",
    r"captcha", r"manual only", r"must be done manually", r"phone calls?", r"cold call", r"virtual assistant",
    r"lead gen", r"lead sourcing", r"marketing", r"seo", r"bookkeep", r"accounting", r"investment", r"forex",
    r"crypto", r"trading bot", r"legal", r"medical", r"illustrat", r"graphic design", r"dashboard", r"analysis",
    r"wordpress", r"web development", r"mobile app", r"flutter", r"react native", r"full.?stack", r"tensorflow",
    r"machine learning", r"ai agent", r"fake review", r"fake account", r"bypass captcha", r"bypass.*paywall",
]
TITLE_OK = [
    r"\b(?:excel|csv|spreadsheet)\b.*\b(?:clean|cleanup|format|merge|combine|consolidat|convert|transform|deduplic|duplicate|normalize|standardiz|reconcil|extract|extraction|import|export)\b",
    r"\b(?:clean|cleanup|format|merge|combine|consolidat|convert|transform|deduplic|duplicate|normalize|standardiz|reconcil|extract|extraction|import|export)\b.*\b(?:excel|csv|spreadsheet)\b",
    r"\bpdf\b.*\b(?:excel|csv|table|extract|conversion|convert)\b",
    r"\b(?:excel|csv|table)\b.*\bpdf\b",
    r"\bdata\s+(?:cleaning|cleansing|extraction|conversion|transformation|deduplication|normalization|reconciliation)\b",
]
DESC_OK = [
    r"(?:clean|cleaning|cleanse|cleansing).*(?:excel|csv|spreadsheet|data)",
    r"(?:excel|csv|spreadsheet|data).*(?:clean|cleaning|cleanse|cleansing)",
    r"deduplic|remove duplicates?", r"normaliz|reconcil|standardiz",
    r"pdf.*(?:excel|csv|spreadsheet|table|extract)", r"(?:excel|csv|spreadsheet|table).*pdf",
    r"(?:extract|extraction).*(?:excel|csv|spreadsheet|table|structured data)",
    r"(?:excel|csv|spreadsheet).*(?:extract|transform|conversion|convert)",
    r"(?:csv|excel|spreadsheet).*(?:format|merge|combine|consolidat)",
]
AUTO = [r"automate", r"automation", r"unattended", r"script", r"python", r"vba", r"batch", r"pipeline"]

@dataclass
class Decision:
    project_id: int
    title: str
    verdict: str
    score: float
    reason: str
    bid_amount: Optional[float] = None
    period_days: Optional[int] = None
    currency_code: Optional[str] = None
    description_excerpt: Optional[str] = None
    already_bid: Optional[bool] = None
    proposal_preview: Optional[str] = None


def _session() -> Session:
    token = os.environ.get(TOKEN_ENV)
    if not token:
        raise RuntimeError(f"Missing {TOKEN_ENV}")
    return Session(oauth_token=token)


def _has(text: str, pats: List[str]) -> bool:
    return any(re.search(p, text, re.I | re.S) for p in pats)


def _count(text: str, pats: List[str]) -> int:
    return sum(1 for p in pats if re.search(p, text, re.I | re.S))


def _proposal(d: Decision) -> str:
    return (
        f"I can complete {d.title} with a validation-first workflow. I will process the supplied files, preserve the requested structure, "
        "check duplicates/formatting and reconcile outputs before delivery. You will receive the completed file plus a concise note covering assumptions or exceptions."
    )


def _evaluate(p: Dict[str, Any]) -> Decision:
    title = (p.get("title") or "").strip()
    desc = (p.get("description") or "").strip()
    blob = f"{title}\n{desc}".lower()
    currency = p.get("currency") or {}
    code = currency.get("code") if isinstance(currency, dict) else None
    excerpt = re.sub(r"\s+", " ", desc)[:420]
    pid = int(p["id"])

    if _has(blob, BLOCK):
        return Decision(pid, title, "REVIEW", 0, "blocked/review-only class", currency_code=code, description_excerpt=excerpt)

    title_hits = _count(title.lower(), TITLE_OK)
    desc_hits = _count(blob, DESC_OK)
    auto_hits = _count(blob, AUTO)
    if title_hits < 1 or desc_hits < 1:
        return Decision(pid, title, "REVIEW", title_hits * 25 + desc_hits * 10 + auto_hits * 2, "title/description do not both confirm exact data-file work", currency_code=code, description_excerpt=excerpt)

    # Generic 'data entry specialist' is not autonomous unless the title itself names Excel/CSV/spreadsheet.
    if re.search(r"\bdata entry\b", title, re.I) and not re.search(r"\b(?:excel|csv|spreadsheet)\b", title, re.I):
        return Decision(pid, title, "REVIEW", 0, "generic data-entry title requires human review", currency_code=code, description_excerpt=excerpt)

    if _has(blob, [r"manual data entry", r"type.*manually", r"human data entry"]):
        return Decision(pid, title, "REVIEW", 0, "manual-entry wording requires review", currency_code=code, description_excerpt=excerpt)

    bid_count = int((p.get("bid_stats") or {}).get("bid_count") or 0)
    score = title_hits * 25 + desc_hits * 10 + auto_hits * 2 + max(0, 5 - min(5, bid_count / 5))
    budget = p.get("budget") or {}
    lo, hi = budget.get("minimum"), budget.get("maximum")
    amount = float(hi or lo or 20)
    if lo is not None and hi is not None:
        amount = round(float(lo) + 0.20 * (float(hi) - float(lo)), 2)
    period = 3 if auto_hits >= 2 else 1
    d = Decision(pid, title, "AUTO_BID_READY", score, "exact deterministic data/file scope", amount, period, code, excerpt)
    d.proposal_preview = _proposal(d)
    return d


def _already_bid(session: Session, project_id: int, bidder_id: int) -> bool:
    result = get_bids(session, project_ids=[project_id], limit=100, offset=0)
    bids = result.get("bids", []) if isinstance(result, dict) else []
    return any(int(b.get("bidder_id") or 0) == int(bidder_id) and not b.get("retracted") for b in bids)


def _search_all(session: Session) -> List[Dict[str, Any]]:
    sf = create_search_projects_filter(sort_field="time_updated", reverse_sort=True, or_search_query=True)
    pd = create_get_projects_project_details_object(full_description=True, jobs=True, upgrades=True)
    by_id: Dict[int, Dict[str, Any]] = {}
    for q in SEARCH_QUERIES:
        result = search_projects(session, query=q, search_filter=sf, project_details=pd, active_only=True, limit=25)
        for p in (result.get("projects", []) if isinstance(result, dict) else []):
            by_id[int(p["id"])] = p
    return list(by_id.values())


def _place_one(session: Session, bidder_id: int, d: Decision) -> Dict[str, Any]:
    if _already_bid(session, d.project_id, bidder_id):
        d.already_bid = True
        return {"project_id": d.project_id, "status": "SKIPPED_ALREADY_BID"}
    bid = place_project_bid(session, project_id=d.project_id, bidder_id=bidder_id, description=_proposal(d), amount=d.bid_amount, period=d.period_days or 1, milestone_percentage=100)
    return {"project_id": d.project_id, "status": "BID_PLACED", "bid_id": getattr(bid, "id", None), "amount": d.bid_amount, "currency_code": d.currency_code}


def run(execute: bool = False):
    s = _session()
    uid = get_self_user_id(s)
    projects = _search_all(s)
    decisions = sorted((_evaluate(p) for p in projects), key=lambda d: d.score, reverse=True)
    ready = [d for d in decisions if d.verdict == "AUTO_BID_READY"]
    for d in ready[:10]:
        try:
            d.already_bid = _already_bid(s, d.project_id, uid)
        except Exception:
            d.already_bid = None
    live = os.environ.get(LIVE_ENV, "").strip().lower() in {"1", "true", "yes", "on"}
    actions: List[Dict[str, Any]] = []
    if execute and live:
        for d in ready:
            if any(a.get("status") == "BID_PLACED" for a in actions):
                break
            if d.already_bid:
                continue
            actions.append(_place_one(s, uid, d))
    return {
        "ok": True,
        "authenticated_user_id": uid,
        "mode": "LIVE_ARMED_V2" if live else "DRY_RUN_MULTI_QUERY_V2",
        "execute_requested": execute,
        "live_enabled": live,
        "projects_seen": len(projects),
        "auto_bid_ready_count": len(ready),
        "auto_bid_ready": [asdict(d) for d in ready[:10]],
        "actions": actions,
        "top_decisions": [asdict(d) for d in decisions[:20]],
    }


class handler(BaseHTTPRequestHandler):
    def _respond(self, execute: bool):
        try:
            payload, code = run(execute=execute), 200
        except Exception as exc:
            payload, code = {"ok": False, "error_type": type(exc).__name__, "error": str(exc)[:500]}, 500
        body = json.dumps(payload, default=str).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        self._respond(False)

    def do_POST(self):
        self._respond(True)
