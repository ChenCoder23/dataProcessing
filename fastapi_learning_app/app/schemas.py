"""API 的请求和响应数据结构。

Pydantic 模型负责“校验和转换客户端传来的 JSON”。
例如 title 不能为空、最长 100 个字符，这些规则会自动变成 422 错误响应。
"""

from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class TaskBase(BaseModel):
    """创建和更新任务时都会使用的公共字段。"""

    title: str = Field(..., min_length=1, max_length=100, description="任务标题")
    description: str | None = Field(default=None, max_length=1000, description="详细说明")


class TaskCreate(TaskBase):
    """POST /api/tasks 接收的请求体。"""


class TaskUpdate(TaskBase):
    """PUT /api/tasks/{task_id} 接收的请求体。"""

    completed: bool = False


class TaskRead(TaskBase):
    """接口返回给前端的任务结构。"""

    id: int
    completed: bool
    created_at: datetime

    # 允许 Pydantic 从 SQLAlchemy 对象属性中读取数据。
    model_config = ConfigDict(from_attributes=True)

