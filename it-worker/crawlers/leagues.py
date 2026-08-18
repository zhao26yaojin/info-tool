# league_id / league 是 stats.qiumibao.com 积分榜接口需要的参数（从浏览器 devtools 网络请求里抓的）
# country_id / event_id 对应 fb_team.country_id 和 fb_standings.event_id 里已有的取值
LEAGUES = [
    {"name": "english-premier-league", "league_id": "24", "league_cn": "英超", "country_id": 2, "event_id": 100},
    {"name": "spanish-laliga", "league_id": "36", "league_cn": "西甲", "country_id": 5, "event_id": 102},
    {"name": "italian-serie-a", "league_id": "48", "league_cn": "意甲", "country_id": 9, "event_id": 108},
    {"name": "german-bundesliga", "league_id": "59", "league_cn": "德甲", "country_id": 8, "event_id": 104},
    {"name": "french-ligue-1", "league_id": "80", "league_cn": "法甲", "country_id": 4, "event_id": 110},
]
