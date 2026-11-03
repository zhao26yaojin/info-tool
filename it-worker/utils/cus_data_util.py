from typing import Dict, List, Any

EVENT_DICT: Dict[str, Dict[str, List[str]]] = {"欧洲联赛": {'德国': ['德甲', '德乙'], '意大利': ['意甲', '意乙'], '英格兰': ['英超', '英冠'],
                                                            '西班牙': ['西甲', '西乙'], '法国': ['法甲', '法乙'], '荷兰': ['荷甲'], '葡萄牙': ['葡超'], '土耳其': ['土超']},
                                               "亚洲联赛": {"中国": ["中超"], "日本": ["J联赛"], "泰国": ["泰超"], "澳大利亚": ["澳超"],
                                                            "越南": ["越南联"], "韩国": ["K联赛"], "马来西亚": ["马来超"]},
                                               "美洲联赛": {"乌拉圭": ["乌拉圭甲级联赛"], "巴西": ["巴甲"], "阿根廷": ["阿超"],
                                                            "美国": ["美职联"]}}

# 积分榜接口使用的联赛名与基础数据(name_cn)不一致的联赛映射
STANDING_LEAGUE_ALIAS: Dict[str, str] = {"澳超": "澳A联", "阿超": "阿甲", "乌拉圭甲级联赛": "乌拉圭甲"}

# 积分榜接口 teamId 不可用(大量为0/与球队接口不一致)的联赛：按积分榜球队名映射到球队接口的 team id(source_id)
# 键为 normalize_team_name 后的名称；未映射的球队会被丢弃
STANDING_TEAM_SOURCE_ID: Dict[str, Dict[str, str]] = {
    "乌拉圭甲级联赛": {
        "peñarol": "2175", "danubio": "2177", "danubiofc": "2177", "defensorsporting": "3634",
        "cerro": "5198", "nacional": "5201", "racing(u)": "5202", "racing(montevideo)": "5202",
        "progreso": "5204", "bostonriver": "5205", "wanderers": "5207", "torque": "5208",
        "利物浦": "5212", "liverpool": "5212",
    },
}


def normalize_team_name(name: str) -> str:
    return name.strip().lower().replace(" ", "").replace(".", "")


MATCH_URL: str = "https://db.qiumibao.com/f/index/matchs?_platform=web"

TEAM_URL: str = "https://db.qiumibao.com/f/index/teams?_platform=web"

STANDING_URL: str = "https://stats.qiumibao.com/shuju/public/index.php"
STANDING_PARAMS: Dict[str, str] = {
    "_url": "/data/index", "tab": "积分榜", "_platform": "web",
}