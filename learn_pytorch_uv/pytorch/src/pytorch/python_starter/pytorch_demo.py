"""PyTorch 入门：张量、形状、广播和简单计算。"""

import torch


def main() -> None:
    x = torch.arange(12, dtype=torch.float32).reshape(3, 4)
    weights = torch.tensor([1.0, 2.0, 3.0, 4.0])
    print("x =\n", x)
    print("x.shape =", x.shape)
    print("每一行与 weights 的点积 =", (x * weights).sum(dim=1))


if __name__ == "__main__":
    main()

