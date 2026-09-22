"""Requests 和 pathlib 的一个可复用示例。默认不发起网络请求。"""

from pathlib import Path
from typing import Any

import requests


def fetch_json(url: str, timeout: float = 5.0) -> dict[str, Any]:
    """请求 JSON 接口；异常会被保留给调用方处理。"""
    response = requests.get(url, timeout=timeout)
    response.raise_for_status()
    return response.json()


def main() -> None:
    project_root = Path(__file__).resolve().parents[3]
    print(f"当前练习模块：{Path(__file__).parent}")
    print(f"项目根目录：{project_root}")
    print("需要请求接口时，在代码中调用 fetch_json(url) 即可。")


if __name__ == "__main__":
    main()

