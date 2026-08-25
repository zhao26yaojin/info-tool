import functools
import hmac
import logging
from typing import Any, Callable, Tuple, Union

from flask import Flask, Response, jsonify, request

from common.logger import setup_logging
from config import API_TOKEN, HTTP_PORT
from crawlers.task import crawls

setup_logging()
logger = logging.getLogger(__name__)

app = Flask(__name__)


def require_token(view: Callable[..., Any]) -> Callable[..., Any]:
    @functools.wraps(view)
    def wrapped(*args: Any, **kwargs: Any) -> Any:
        token: str = request.headers.get("X-API-Token", "")
        if not API_TOKEN or not hmac.compare_digest(token, API_TOKEN):
            return jsonify({"error": "unauthorized"}), 401
        return view(*args, **kwargs)

    return wrapped


@app.get("/health")
def health() -> Response:
    return jsonify({"status": "ok"})


@app.post("/crawl/<task_name>")
@require_token
def crawl(task_name: str) -> Union[Response, Tuple[Response, int]]:
    logger.info("triggered task=%s", task_name)
    try:
        crawls(task_name)
    except NotImplementedError as exc:
        return jsonify({"error": str(exc)}), 501

    return 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=HTTP_PORT)