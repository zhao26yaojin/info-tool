import logging
from abc import ABC
from typing import Dict, Any, TypeVar, Generic, List

import requests

from config import REQUEST_TIMEOUT
from utils.data_util import init_session

logger = logging.getLogger(__name__)

# 定义泛型类型变量 T
T = TypeVar("T")


class CrawlerBase(ABC, Generic[T]):
    def __init__(self, table: str = ""):
        self.table = table

        self.results: List[T] = []

        self.keys = set()

        self.session: requests.Session = init_session()

    def get_json(self, url: str, params: Dict[str, Any] | None = None) -> Any:
        logger.info("GET %s params=%s", url, params)
        response: requests.Response = self.session.get(url, params=params, timeout=REQUEST_TIMEOUT)
        response.raise_for_status()
        return response.json()

    def add_result(self, result: T, key) -> None:
        if key in self.keys:
            return

        self.results.append(result)
        self.keys.add(key)