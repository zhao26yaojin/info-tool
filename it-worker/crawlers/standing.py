from crawlers.cus_base import CusCrawlerBase


class StandingCrawler(CusCrawlerBase):
    def crawl(self):
        pass

    def crawl_all(self) -> Dict[str, Dict[str, Any]]:
        return self.fetch_all(LEAGUES, self.fetch_one)

    def fetch_one(self, league: League) -> Dict[str, Any]:
        rows = fetch_standings_rows(self, league)

        standings: List[Dict[str, Any]] = []
        for row in rows:
            goals_for, goals_against = row["进/失球"].split("/")
            standings.append(
                {
                    "team_name": row["球队名称"].strip(),
                    "game_play": row["场次"],
                    "win": row["胜"],
                    "draw": row["平"],
                    "loss": row["负"],
                    "goals_for": goals_for,
                    "goals_against": goals_against,
                    "goals_differential": row["净胜球"],
                    "points": row["积分"],
                }
            )

        return {
            "country_id": league["country_id"],
            "event_id": league["event_id"],
            "standings": standings,
        }

    def fetch_all(
        self,
        leagues: List[League],
        fetch_one: Callable[[League], Any],
    ) -> Dict[str, Dict[str, Any]]:
        """对 LEAGUES 里每个联赛调用 fetch_one(league)，单个联赛失败不影响其它联赛。"""
        results: Dict[str, Dict[str, Any]] = {}
        for league in leagues:
            try:
                results[league["name"]] = {"ok": True, "data": fetch_one(league)}
            except Exception as exc:
                logger.exception("failed to crawl league=%s", league["name"])
                results[league["name"]] = {"ok": False, "error": str(exc)}
        return results