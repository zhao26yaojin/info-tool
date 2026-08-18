import logging

from crawlers.league import LeagueCrawler
from crawlers.standing import StandingCrawler
from crawlers.team import TeamCrawler
from db import standing_repo, team_repo
from db.connection import get_connection

logger = logging.getLogger(__name__)


def _run(crawler, store_fn):
    results = crawler.crawl_all()

    summary = {}
    conn = get_connection()
    try:
        for league_name, result in results.items():
            if not result["ok"]:
                summary[league_name] = result
                continue
            try:
                summary[league_name] = {"ok": True, **store_fn(conn, result["data"])}
            except Exception as exc:
                logger.exception("failed to store league=%s", league_name)
                summary[league_name] = {"ok": False, "error": str(exc)}
    finally:
        conn.close()

    return summary


def run_team():
    return _run(TeamCrawler(), lambda conn, data: team_repo.insert_teams(conn, data["country_id"], data["team_names"]))


def run_standing():
    return _run(
        StandingCrawler(),
        lambda conn, data: standing_repo.save_standings(conn, data["country_id"], data["event_id"], data["standings"]),
    )


def run_league():
    LeagueCrawler().crawl_all()


def run_all():
    # 顺序很重要：积分榜按球队名查 team_id，球队信息要先入库
    return {
        "team": run_team(),
        "standing": run_standing(),
    }


TASKS = {
    "team": run_team,
    "standing": run_standing,
    "league": run_league,
    "all": run_all,
}


def has_errors(summary):
    for value in summary.values():
        if not isinstance(value, dict):
            continue
        if "ok" in value:
            if not value["ok"]:
                return True
        elif has_errors(value):
            return True
    return False
