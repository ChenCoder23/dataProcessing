# Python 入门练习

这个文件夹是一个可以直接运行、逐步修改的练习模块。

## 先用 uv 跑起来

在当前目录（包含 `pyproject.toml` 的目录）执行：

```powershell
# 同步虚拟环境和锁定文件中的依赖
uv sync

# 运行全部示例
uv run python -m pytorch.python_starter.main

# 单独运行某一个示例
uv run python -m pytorch.python_starter.basics
uv run python -m pytorch.python_starter.common_libs
uv run python -m pytorch.python_starter.pytorch_demo
```

## 建议学习顺序

1. `basics.py`：函数、类型提示、`dataclass`、`pathlib`、JSON。
2. `common_libs.py`：NumPy 数组、Pandas 表格、Pydantic 数据校验、Rich 终端输出。
3. `http_demo.py`：Requests 发 HTTP 请求，理解超时和异常处理。
4. `pytorch_demo.py`：张量、形状、广播和维度计算。

## 常用 uv 命令

```powershell
uv venv                         # 创建虚拟环境
uv add 包名                     # 添加运行依赖并更新锁文件
uv add --dev pytest             # 添加开发依赖
uv remove 包名                  # 移除依赖
uv lock                         # 重新生成 uv.lock
uv run python your_file.py      # 在项目环境中运行脚本
uv run pytest                   # 在项目环境中运行测试
```

## 练习建议

- 把 `Student` 增加 `email` 字段，并在保存前做校验。
- 给 Pandas 表格增加 `quantity` 列，计算每种商品的小计。
- 为 `calculate_average` 编写测试。
- 把 `fetch_json` 改造成带重试次数的函数。
- 在 `pytorch_demo.py` 中尝试 `reshape`、切片和矩阵乘法 `@`。

