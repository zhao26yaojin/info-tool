import logging
from abc import ABC
from typing import Dict, Any, TypeVar, Generic, List

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

from config import REQUEST_TIMEOUT
from utils.data_util import HEADERS

logger = logging.getLogger(__name__)

# 定义泛型类型变量 T
T = TypeVar("T")


class CrawlerBase(ABC, Generic[T]):
    def __init__(self) -> None:
        self.results: List[T] = []

        self.session: requests.Session = requests.Session()
        self.session.headers.update(HEADERS)

        retry: Retry = Retry(total=2, backoff_factor=1, status_forcelist=[429, 500, 502, 503, 504])
        adapter: HTTPAdapter = HTTPAdapter(max_retries=retry)
        self.session.mount("https://", adapter)
        self.session.mount("http://", adapter)

    def get_json(self, url: str, params: Dict[str, Any] | None = None) -> Any:
        logger.info("GET %s params=%s", url, params)
        response: requests.Response = self.session.get(url, params=params, timeout=REQUEST_TIMEOUT)
        response.raise_for_status()
        return response.json()