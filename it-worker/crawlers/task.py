from typing import List

from crawlers.standing import StandingCrawler
from crawlers.team import TeamCrawler
from db.team import TeamDb
from enums.task_enum import TaskEnum
from utils.data_util import get_tasks, get_opt


def crawls(task_param: str, opt_param: str) -> None:
    tasks: List[TaskEnum] = get_tasks(task_param)

    for task in tasks:
        match task:
            case TaskEnum.STANDING:
                standing_crawler = StandingCrawler()
                standing_crawler.crawl()
            case TaskEnum.TEAM:
                team_crawler = TeamCrawler()
                team_crawler.crawl()
                TeamDb().save(team_crawler.results, opt_param)
