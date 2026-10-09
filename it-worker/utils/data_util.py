from typing import Dict

import requests
from requests.adapters import HTTPAdapter
from urllib3 import Retry

from enums.opt_enum import OptEnum

from enums.task_enum import TaskEnum


HEADERS: Dict[str, str] = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    )
}


def init_session() -> requests.Session:
    session: requests.Session = requests.Session()
    session.headers.update(HEADERS)

    retry: Retry = Retry(total=2, backoff_factor=1, status_forcelist=[429, 500, 502, 503, 504])
    adapter: HTTPAdapter = HTTPAdapter(max_retries=retry)
    session.mount("https://", adapter)
    session.mount("http://", adapter)

    return session


def format_task_param(task_param: str) -> str:
    if not task_param:
        return 'merge=country,tournament,standing;sync=team'

    if task_param == 'all':
        return 'merge=country,tournament,standing;sync=team'

    return task_param


def get_tasks(task_param: str) -> Dict[TaskEnum, OptEnum]:
    tasks = {}

    for item in task_param.split(';'):
        opt, task_names = item.split('=', 1)
        opt_enum = OptEnum(opt)

        for task_name in task_names.split(','):
            tasks[TaskEnum(task_name)] = opt_enum

    return tasks
