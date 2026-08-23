import os
import re
from dataclasses import dataclass
from typing import Any, Dict, List, Optional

from freelancersdk.session import Session
from freelancersdk.resources.projects import search_projects, get_project_details, place_project_bid
from freelancersdk.resources.users import get_self_user_id

TOKEN_ENV = "FLN_OAUTH_TOKEN"

HUMAN_SPECIFIC_PATTERNS = [
    r"survey", r"focus group", r"personal experience", r"mystery shop",
    r"video of yourself", r"voice sample", r"record yourself", r"in-person",
    r"on-site", r"onsite", r"captcha", r"different ip", r"human judgment",
]

PROHIBITED_PATTERNS = [
    r"fake review", r"fake account", r"bypass captcha", r"evade", r"private customer database",
]

MACHINE_POSITIVE_PATTERNS = [
    r"excel", r"csv", r"python", r"data processing", r"data entry", r"data extraction",
    r"data cleansing", r"web scraping", r"mysql", r"automation", r"pdf", r"json", r"xml",
    r"pivot", r"spreadsheet", r"report", r"api", r"database",
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
    proposal: Optional[str] = None


def session() -> Session:
    token = os.environ.get(TOKEN_ENV)
    if not token:
        raise RuntimeError(f"Missing {TOKEN_ENV}")
    return Session(oauth_token=token)


def text(project: Dict[str, Any]) -> str:
    return f"{project.get('title','')}\n{project.get('description','')}".lower()


def contains_any(blob: str, patterns: List[str]) -> bool:
    return any(re.search(p, blob, re.I) for p in patterns)


def evaluate_project(project: Dict[str, Any]) -> Decision:
    blob = text(project)
    pid = int(project['id'])
    title = project.get('title', '')

    if contains_any(blob, PROHIBITED_PATTERNS):
        return Decision(pid, title, "REJECT", -100, "Policy/risk pattern detected")
    if contains_any(blob, HUMAN_SPECIFIC_PATTERNS):
        return Decision(pid, title, "REJECT", -50, "Work appears to require a specifically human/personal response")

    score = 0.0
    hits = sum(1 for p in MACHINE_POSITIVE_PATTERNS if re.search(p, blob, re.I))
    score += hits * 3

    bid_stats = project.get('bid_stats') or {}
    bid_count = bid_stats.get('bid_count') or 0
    score += max(0, 10 - min(10, bid_count / 3))

    budget = project.get('budget') or {}
    minimum = budget.get('minimum')
    maximum = budget.get('maximum')
    if maximum:
        score += min(float(maximum), 300) / 30

    if hits < 2:
        return Decision(pid, title, "REVIEW", score, "Machine suitability not strong enough from project text")

    bid_amount = float(maximum or minimum or 20)
    if maximum and minimum:
        # stay competitive without blindly racing to the floor
        bid_amount = round(float(minimum) + 0.55 * (float(maximum)-float(minimum)), 2)

    period = 3 if any(k in blob for k in ["automation", "script", "mysql", "database"]) else 1
    proposal = generate_proposal(project)
    return Decision(pid, title, "GREEN_GATE", score, "Objective machine-executable deliverable detected", bid_amount, period, proposal)


def generate_proposal(project: Dict[str, Any]) -> str:
    title = project.get('title','your project')
    return (
        f"I can handle {title} with a machine-first workflow focused on accuracy, validation, and a clean handoff. "
        "I will preserve the source inputs, validate the requested output, document material changes/exceptions, and test the final deliverable before submission. "
        "If the work is repetitive, I will use a reusable automated process rather than manual entry where appropriate."
    )


def discover(limit: int = 50) -> List[Decision]:
    s = session()
    # Official SDK search helper. Search newest open projects; downstream filters are conservative.
    result = search_projects(s, query="Excel data Python automation", limit=limit, active_only=True)
    projects = result.get('projects', result if isinstance(result, list) else [])
    decisions = [evaluate_project(p) for p in projects]
    return sorted(decisions, key=lambda d: d.score, reverse=True)


def submit_bid(decision: Decision, dry_run: bool = True) -> Dict[str, Any]:
    if decision.verdict != "GREEN_GATE":
        raise ValueError("Only GREEN_GATE decisions may be bid")
    if dry_run:
        return {"dry_run": True, "decision": decision.__dict__}

    s = session()
    bidder_id = get_self_user_id(s)
    return place_project_bid(
        s,
        project_id=decision.project_id,
        bidder_id=bidder_id,
        amount=decision.bid_amount,
        period=decision.period_days,
        milestone_percentage=100,
        description=decision.proposal,
    )


if __name__ == "__main__":
    for d in discover():
        print(d)
