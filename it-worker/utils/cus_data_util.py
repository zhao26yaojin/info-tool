from typing import Dict, List, Any

EVENT_DICT: Dict[str, Dict[str, List[str]]] = {"欧洲联赛": {'德国': ['德甲', '德乙'], '意大利': ['意甲', '意乙'], '英格兰': ['英超', '英冠'],
                                                            '西班牙': ['西甲', '西乙'], '法国': ['法甲', '法乙'], '荷兰': ['荷甲'], '葡萄牙': ['葡超'], '土耳其': ['土超']},
                                               "亚洲联赛": {"中国": ["中超"], "日本": ["J联赛"], "泰国": ["泰超"], "澳大利亚": ["澳超"],
                                                            "越南": ["越南联"], "韩国": ["K联赛"], "马来西亚": ["马来超"]},
                                               "美洲联赛": {"乌拉圭": ["乌拉圭甲级联赛"], "巴西": ["巴甲"], "阿根廷": ["阿超"],
                                                            "美国": ["美职联"]}}

MATCH_URL: str = "https://db.qiumibao.com/f/index/matchs?_platform=web"

TEAM_URL: str = "https://db.qiumibao.com/f/index/teams?_platform=web"

STANDING_URL: str = "https://stats.qiumibao.com/shuju/public/index.php"
STANDING_PARAMS: Dict[str, str] = {
    "_url": "/data/index", "tab": "积分榜", "_platform": "web",
}