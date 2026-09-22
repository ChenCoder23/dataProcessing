"""任务 API 路由。

路由就是“URL + HTTP 方法”到 Python 函数的映射。
这里的函数负责：接收请求、调用 CRUD、决定返回什么状态码。
"""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from .. import crud, schemas
from ..database import get_db


router = APIRouter(prefix="/api/tasks", tags=["任务"])


@router.get("", response_model=list[schemas.TaskRead])
def list_tasks(db: Session = Depends(get_db)):
    """获取任务列表。

    Depends(get_db) 是 FastAPI 的依赖注入：FastAPI 会自动创建并传入 db。
    """

    return crud.get_tasks(db)


@router.post("", response_model=schemas.TaskRead, status_code=status.HTTP_201_CREATED)
def add_task(task_in: schemas.TaskCreate, db: Session = Depends(get_db)):
    """创建一条新任务。"""

    return crud.create_task(db, task_in)


@router.get("/{task_id}", response_model=schemas.TaskRead)
def read_task(task_id: int, db: Session = Depends(get_db)):
    """按 id 获取一条任务。"""

    task = crud.get_task(db, task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="任务不存在")
    return task


@router.put("/{task_id}", response_model=schemas.TaskRead)
def edit_task(
    task_id: int,
    task_in: schemas.TaskUpdate,
    db: Session = Depends(get_db),
):
    """完整更新任务标题、说明和完成状态。"""

    task = crud.get_task(db, task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="任务不存在")
    return crud.update_task(db, task, task_in)


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def remove_task(task_id: int, db: Session = Depends(get_db)):
    """删除一条任务；成功时返回 204，不返回 JSON 内容。"""

    task = crud.get_task(db, task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="任务不存在")
    crud.delete_task(db, task)

