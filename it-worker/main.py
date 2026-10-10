# This is a sample Python script.
import argparse
from typing import List

from common.logger import setup_logging
from crawlers.task import crawls

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    setup_logging()

    # 创建参数解析器
    parser = argparse.ArgumentParser(description="爬虫任务启动脚本")

    # 添加 --task 参数，默认值设为空字符串 ''
    parser.add_argument(
        "-t",
        "--task",
        type=str,
        default="",
        help="指定执行的任务名称，多个任务用逗号分割（例如: task1,task2）。不传则执行默认任务。"
    )

    # 解析命令行输入的参数
    args = parser.parse_args()

    # args.task = '=,;'

    # 执行爬虫逻辑
    crawls(args.task)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
