"""统一运行所有入门示例：python -m pytorch.python_starter.main"""

from .basics import main as basics_main
from .common_libs import main as common_libs_main
from .http_demo import main as http_main
from .pytorch_demo import main as pytorch_main


def main() -> None:
    print("=== 1. Python 基础 ===")
    basics_main()
    print("\n=== 2. 常见第三方库 ===")
    common_libs_main()
    print("\n=== 3. 文件与 HTTP ===")
    http_main()
    print("\n=== 4. PyTorch ===")
    pytorch_main()


if __name__ == "__main__":
    main()

