from config import current_season_year

STATS_URL = "https://stats.qiumibao.com/shuju/public/index.php"


def fetch_standings_rows(crawler, league):
    """联赛积分榜原始数据，一次返回该联赛所有球队（含 teamId + 名称），标准/球队信息都从这里派生。"""
    params = {
        "_url": "/data/index",
        "year": str(current_season_year()),
        "type": "积分榜",
        "tab": "积分榜",
        "league_id": league["league_id"],
        "league": league["league_cn"],
        "_platform": "web",
        "_env": "pc",
    }
    data = crawler.get_json(STATS_URL, params=params)
    rows = data.get("data") or []
    if not rows:
        raise ValueError("empty standings for league={}".format(league["name"]))
    return rows
