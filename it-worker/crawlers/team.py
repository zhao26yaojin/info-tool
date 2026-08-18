from crawlers.base import CrawlerBase
from crawlers.leagues import LEAGUES
from crawlers.qiumibao import fetch_standings_rows


class TeamCrawler(CrawlerBase):
    def crawl_all(self):
        return self.fetch_all(LEAGUES, self.fetch_one)

    def fetch_one(self, league):
        rows = fetch_standings_rows(self, league)
        team_names = [row["球队名称"].strip() for row in rows]
        return {"country_id": league["country_id"], "team_names": team_names}
