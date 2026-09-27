from crawlers.common.country_crawler import CountryCrawler
from crawlers.fb.team_crawler import TeamCrawler
from db.common.country_db import CountryDb
from db.fb.team_db import TeamDb
from enums.task_enum import TaskEnum

import logging
from typing import Dict, Type, Any
from enums.opt_enum import OptEnum
from utils.data_util import get_tasks, format_task_param


logger = logging.getLogger(__name__)

# 1. 建立 任务 -> (爬虫类, 数据库类) 的映射表，消除 match/case 冗余
CRAWLER_MAP = {
    TaskEnum.COUNTRY: (CountryCrawler, CountryDb),
    TaskEnum.TEAM: (TeamCrawler, TeamDb)
    # TaskEnum.STANDING: (StandingCrawler, StandingDb),
    # TaskEnum.TEAM: (TeamCrawler, TeamDb)
}


def crawls(task_param: str) -> None:
    task_param = format_task_param(task_param)
    tasks: Dict[TaskEnum, OptEnum] = get_tasks(task_param)

    # 2. 统一循环执行
    for task, opt in tasks.items():
        if task not in CRAWLER_MAP:
            logger.info(f"未知的任务类型: {task}")
            continue

        crawler_cls, db_cls = CRAWLER_MAP[task]

        # 实例化并运行爬虫
        crawler = crawler_cls()
        crawler.crawl()

        # 统一保存数据
        save_data(db_cls, crawler.results, opt)


def save_data(save_cls: Type, results: Any, opt: OptEnum):
    if not results:
        logger.info(f"results为空: {save_cls.__name__}")
        return

    # 提前实例化数据库对象，避免在循环中重复创建连接
    db_handler = save_cls()

    if isinstance(results, list):
        db_handler.save(results, opt)
    elif isinstance(results, dict):
        for batch_id, sub_results in results.items():
            if not sub_results:
                logger.info(f"sub results为空{batch_id}: {save_cls.__name__}")

            # 将 batch_id 作为过滤范围（如 country_id）传给 save 方法
            db_handler.save(sub_results, opt, batch_id=batch_id)