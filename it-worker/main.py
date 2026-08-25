# This is a sample Python script.
from typing import List

from common.logger import setup_logging
from crawlers.task import crawls
from enums.task_enum import TaskEnum

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def parse_tasks(value: str) -> List[TaskEnum]:
    if not value:
        return list(TaskEnum)
    return [TaskEnum(item.strip()) for item in value.split(",") if item.strip()]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    setup_logging()

    task = ''

    crawls(task)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
