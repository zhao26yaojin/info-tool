import argparse
import json
import sys

import tasks
from config import setup_logging


def main():
    parser = argparse.ArgumentParser(description="it-worker crawler CLI")
    parser.add_argument("--task", choices=sorted(tasks.TASKS), required=True)
    args = parser.parse_args()

    setup_logging()
    result = tasks.TASKS[args.task]()
    print(json.dumps(result, ensure_ascii=False, indent=2))

    sys.exit(1 if result and tasks.has_errors(result) else 0)


if __name__ == "__main__":
    main()
