from crawlers.base import CrawlerBase
from crawlers.leagues import LEAGUES
from crawlers.qiumibao import fetch_standings_rows


class StandingCrawler(CrawlerBase):
    def crawl_all(self):
        return self.fetch_all(LEAGUES, self.fetch_one)

    def fetch_one(self, league):
        rows = fetch_standings_rows(self, league)

        standings = []
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
