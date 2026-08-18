import functools
import hmac
import logging

from flask import Flask, jsonify, request

import tasks
from config import API_TOKEN, HTTP_PORT, setup_logging

setup_logging()
logger = logging.getLogger(__name__)

app = Flask(__name__)


def require_token(view):
    @functools.wraps(view)
    def wrapped(*args, **kwargs):
        token = request.headers.get("X-API-Token", "")
        if not API_TOKEN or not hmac.compare_digest(token, API_TOKEN):
            return jsonify({"error": "unauthorized"}), 401
        return view(*args, **kwargs)

    return wrapped


@app.get("/health")
def health():
    return jsonify({"status": "ok"})


@app.post("/crawl/<task_name>")
@require_token
def crawl(task_name):
    if task_name not in tasks.TASKS:
        return jsonify({"error": "unknown task '{}'".format(task_name)}), 404

    logger.info("triggered task=%s", task_name)
    try:
        result = tasks.TASKS[task_name]()
    except NotImplementedError as exc:
        return jsonify({"error": str(exc)}), 501

    status_code = 207 if result and tasks.has_errors(result) else 200
    return jsonify(result), status_code


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=HTTP_PORT)
