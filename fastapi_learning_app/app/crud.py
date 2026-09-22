"""CRUD 数据操作层。

CRUD 是 Create、Read、Update、Delete 的缩写。
把数据库细节放在这里，路由文件就只需要关注 HTTP 请求和响应，职责更清晰。
"""

from sqlalchemy import select
from sqlalchemy.orm import Session

from . import models, schemas


def get_tasks(db: Session) -> list[models.Task]:
    """查询全部任务，最新创建的排在前面。"""

    statement = select(models.Task).order_by(models.Task.id.desc())
    return list(db.scalars(statement).all())


def get_task(db: Session, task_id: int) -> models.Task | None:
    """按主键查询单个任务；找不到时返回 None。"""

    return db.get(models.Task, task_id)


def create_task(db: Session, task_in: schemas.TaskCreate) -> models.Task:
    """把 Pydantic 输入对象转换成数据库对象并保存。"""

    task = models.Task(**task_in.model_dump())
    db.add(task)
    db.commit()
    db.refresh(task)  # 重新读取数据库生成的 id、created_at 等字段
    return task


def update_task(
    db: Session, task: models.Task, task_in: schemas.TaskUpdate
) -> models.Task:
    """更新任务字段并返回更新后的对象。"""

    for field, value in task_in.model_dump().items():
        setattr(task, field, value)
    db.commit()
    db.refresh(task)
    return task


def delete_task(db: Session, task: models.Task) -> None:
    """删除任务。"""

    db.delete(task)
    db.commit()

