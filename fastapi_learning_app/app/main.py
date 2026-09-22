"""FastAPI 应用入口。

启动命令：uvicorn app.main:app --reload
其中 app.main:app 的含义是：从 app/main.py 导入名为 app 的 FastAPI 对象。
"""

from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from . import models
from .database import Base, engine
from .routers.tasks import router as tasks_router


# 应用启动时创建表。学习项目这样直观；正式项目通常使用 Alembic 做数据库迁移。
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="FastAPI 学习任务清单",
    description="一个带有 SQLite 和原生前端的教学项目",
    version="1.0.0",
)

BASE_DIR = Path(__file__).resolve().parent.parent
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")
app.include_router(tasks_router)


@app.get("/", include_in_schema=False)
def index():
    """返回前端页面。"""

    return FileResponse(BASE_DIR / "templates" / "index.html")


@app.get("/health", tags=["系统"])
def health_check():
    """健康检查接口：用来确认服务是否已经启动。"""

    return {"status": "ok", "message": "FastAPI 正在运行"}

