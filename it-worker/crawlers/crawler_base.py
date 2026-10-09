import logging
from abc import ABC, abstractmethod
from typing import Dict, Any, TypeVar, Generic, List

import requests

from common.constant import LOGO
from config import REQUEST_TIMEOUT
from storage.storage_handle import StorageHandle
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

    def crawl(self):
        self.handle_request()

        self.handle_storage()

        self.handle_rel_id()

    @abstractmethod
    def handle_request(self):
        pass

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

    def handle_storage(self):
        if self.results and hasattr(self.results[0], LOGO):
            storage = StorageHandle()

            logos = [r.logo for r in self.results]

            # 一次性拉取已存在的 key, 避免每个 logo 都发一次 head_object
            key_prefix = f'logo/{self.table}/'

            existing_keys = storage.get_exist_keys(key_prefix)
            logo_refs = storage.save_files(set(logos), existing_keys, key_prefix)

            # 上传失败的丢弃; 成功的把原始 URL 替换为 s3://bucket/key 引用
            self.results = [r for r in self.results if r.logo in logo_refs]
            for r in self.results:
                r.logo = logo_refs[r.logo]

    def handle_rel_id(self):
        pass