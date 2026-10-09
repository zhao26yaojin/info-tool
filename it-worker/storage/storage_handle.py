import logging
import os

import boto3
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib.parse import urlparse

import config
from utils.data_util import init_session

LOGO_UPLOAD_WORKERS = 8

logger = logging.getLogger(__name__)


class StorageHandle:
    def __init__(self) -> None:
        self.session: requests.Session = init_session()

        self.s3_client = boto3.client(
            "s3",
            endpoint_url=config.MINIO_ENDPOINT,
            aws_access_key_id=config.MINIO_ACCESS_KEY,
            aws_secret_access_key=config.MINIO_SECRET_KEY,
        )

    @staticmethod
    def file_store_url(key: str) -> str:
        return f"s3://{config.MINIO_BUCKET}/{key}"

    def get_exist_keys(self, prefix: str) -> set:
        """一次性列出 bucket 下指定前缀的所有 key, 用于批量判断是否已存在,
        避免对每个资源都发一次 head_object。"""
        keys = set()
        paginator = self.s3_client.get_paginator("list_objects_v2")
        for page in paginator.paginate(Bucket=config.MINIO_BUCKET, Prefix=prefix):
            for obj in page.get("Contents", []):
                keys.add(obj["Key"])
        return keys

    def save_files(self, logo_urls: set, existing_keys: set, key_prefix: str) -> dict:
        """并发下载/上传去重后的 logo 列表, 返回 {logo_url: logo_ref}。"""
        logos = {}
        with ThreadPoolExecutor(max_workers=LOGO_UPLOAD_WORKERS) as pool:
            futures = {pool.submit(self._save_file, url, existing_keys, key_prefix): url for url in logo_urls}
            for future in as_completed(futures):
                url = futures[future]
                try:
                    logos[url] = future.result()
                except Exception:
                    logger.exception("save logo failed: %s", url)
        return logos

    def _save_file(self, file_url: str, existing_keys: set, key_prefix: str) -> str:
        key = f"{key_prefix}{os.path.basename(urlparse(file_url).path)}"
        if key in existing_keys:
            return self.file_store_url(key)

        # 此处是解析图片，以后支持其他类型的文件时这里需要扩展
        content = self._get_bytes(file_url)
        return self._upload_file(key, content)

    def _upload_file(self, key: str, content: bytes, content_type: str = "image/png") -> str:
        """上传原图到 MinIO, 返回 s3://bucket/key 引用 (不是可访问 URL)。
        展示缩略图时由 imgproxy 按需从该引用生成, 数据库里只存这个引用字符串。"""
        self.s3_client.put_object(Bucket=config.MINIO_BUCKET, Key=key, Body=content, ContentType=content_type)
        return self.file_store_url(key)

    def _get_bytes(self, url: str) -> bytes:
        logger.info("GET %s", url)
        response: requests.Response = self.session.get(url, timeout=config.REQUEST_TIMEOUT)
        response.raise_for_status()
        return response.content