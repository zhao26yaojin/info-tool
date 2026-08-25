from typing import Dict

from enums.opt_enum import OptEnum

from enums.task_enum import TaskEnum


TASKS = {TaskEnum.TEAM: False}


def get_tasks(task_param: str | None) -> list[TaskEnum]:
    # 默认task（选择TASKS中value为True的item）
    if not task_param:
        return [k for k, v in TASKS.items() if v]

    if task_param == 'all':
        return list(TASKS.keys())

    return [TaskEnum(p) for p in task_param.split(',') if p.strip()]


def get_opt(opt_param: str | None) -> OptEnum:
    if not opt_param:
        return OptEnum.SYNC

    return OptEnum(opt_param)


HEADERS: Dict[str, str] = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    )
}