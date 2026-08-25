from crawlers.base import CrawlerBase
from crawlers.cus_base import CusCrawlerBase
from models.team import Team


class TeamCrawler(CusCrawlerBase[Team]):
    def crawl(self) -> Dict[str, Dict[str, Any]]:
        return self.fetch_all(LEAGUES, self.fetch_one)

    def fetch_one(self, league: League) -> Dict[str, Any]:
        rows = fetch_standings_rows(self, league)
        team_names: List[str] = [row["球队名称"].strip() for row in rows]
        return {"country_id": league["country_id"], "team_names": team_names}

    def fetch_standings_rows(crawler: CrawlerBase, league: League) -> List[Dict[str, Any]]:
        """联赛积分榜原始数据，一次返回该联赛所有球队（含 teamId + 名称），标准/球队信息都从这里派生。"""
        params: Dict[str, str] = {
            "_url": "/data/index",
            "year": str(current_season_year()),
            "type": "积分榜",
            "tab": "积分榜",
            "league_id": league["league_id"],
            "league": league["league_cn"],
            "_platform": "web",
            "_env": "pc",
        }
        data: Dict[str, Any] = crawler.get_json(STATS_URL, params=params)
        rows: List[Dict[str, Any]] = data.get("data") or []
        if not rows:
            raise ValueError("empty standings for league={}".format(league["name"]))
        return rows