from typing import Dict, List, Any

EVENT_DICT: Dict[str, Dict[str, List[str]]] = {"欧洲联赛": {'德国': ['德甲'], '意大利': ['意甲'], '英格兰': ['英超']}}

MATCH_URL: str = "https://db.qiumibao.com/f/index/matchs?_platform=web"

TEAM_URL: str = "https://db.qiumibao.com/f/index/teams?_platform=web"

STANDING_URL: str = "https://stats.qiumibao.com/shuju/public/index.php"
STANDING_PARAMS: Dict[str, str] = {
    "_url": "/data/index", "tab": "积分榜", "_platform": "web",
}