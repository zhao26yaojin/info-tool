import logging

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

from config import REQUEST_TIMEOUT

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    )
}

logger = logging.getLogger(__name__)


class CrawlerBase:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update(HEADERS)

        retry = Retry(total=3, backoff_factor=1, status_forcelist=[429, 500, 502, 503, 504])
        adapter = HTTPAdapter(max_retries=retry)
        self.session.mount("https://", adapter)
        self.session.mount("http://", adapter)

    def get_json(self, url, params=None):
        logger.info("GET %s params=%s", url, params)
        response = self.session.get(url, params=params, timeout=REQUEST_TIMEOUT)
        response.raise_for_status()
        return response.json()

    def fetch_all(self, leagues, fetch_one):
        """对 LEAGUES 里每个联赛调用 fetch_one(league)，单个联赛失败不影响其它联赛。"""
        results = {}
        for league in leagues:
            try:
                results[league["name"]] = {"ok": True, "data": fetch_one(league)}
            except Exception as exc:
                logger.exception("failed to crawl league=%s", league["name"])
                results[league["name"]] = {"ok": False, "error": str(exc)}
        return results
