import boto3

import config

_s3 = boto3.client(
    "s3",
    endpoint_url=config.MINIO_ENDPOINT,
    aws_access_key_id=config.MINIO_ACCESS_KEY,
    aws_secret_access_key=config.MINIO_SECRET_KEY,
)


def upload_icon(key: str, content: bytes, content_type: str = "image/png") -> str:
    """上传原图到 MinIO, 返回 s3://bucket/key 引用 (不是可访问 URL)。
    展示缩略图时由 imgproxy 按需从该引用生成, 数据库里只存这个引用字符串。"""
    _s3.put_object(Bucket=config.MINIO_BUCKET, Key=key, Body=content, ContentType=content_type)
    return f"s3://{config.MINIO_BUCKET}/{key}"
