from typing import Dict, Any, List, TypeVar

from crawlers.base import CrawlerBase
from utils.cus_data_util import MATCH_URL

# 定义泛型类型变量 T
T = TypeVar("T")

class CusCrawlerBase(CrawlerBase[T]):
    def __init__(self):
        super().__init__()

        self._match_datas: List[Dict[str, Any]] = []

    @property
    def match_datas(self):
        if not self._match_datas:
            # 获取联赛/国家基础数据信息
            data: Dict[str, Any] = super().get_json(MATCH_URL)
            self._match_datas = data.get("data")

        if not self._match_datas:
            raise ValueError("fetch match datas error.")

        return self._match_datas