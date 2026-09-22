"""常见第三方库的最小示例：NumPy、Pandas、Rich、Pydantic。"""

import numpy as np
import pandas as pd
from pydantic import BaseModel, Field
from rich import print
from rich.table import Table


class Product(BaseModel):
    name: str
    price: float = Field(gt=0, description="价格必须大于 0")
    tags: list[str] = Field(default_factory=list)


def main() -> None:
    # NumPy：适合高效处理数组和矩阵。
    numbers = np.array([10, 20, 30, 40])
    print(f"[cyan]NumPy[/cyan] 平均值：{numbers.mean():.1f}，乘 2：{numbers * 2}")

    # Pandas：适合表格数据清洗和分析。
    orders = pd.DataFrame(
        {"product": ["键盘", "鼠标", "显示器"], "price": [199, 99, 1299]}
    )
    print(f"[green]Pandas[/green] 总价：{orders['price'].sum()}，行数：{len(orders)}")

    # Pydantic：运行时校验外部输入，并转换成类型安全的对象。
    product = Product(name="键盘", price=199, tags=["办公"])
    print(f"[yellow]Pydantic[/yellow]：{product.model_dump()}")

    # Rich：让终端输出更易读。
    table = Table(title="商品示例")
    table.add_column("商品")
    table.add_column("价格", justify="right")
    for row in orders.itertuples(index=False):
        # 用纯数字避免部分 Windows GBK 终端无法输出货币符号。
        table.add_row(row.product, f"{row.price}")
    print(table)


if __name__ == "__main__":
    main()
