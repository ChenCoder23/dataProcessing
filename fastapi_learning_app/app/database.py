"""数据库连接与会话管理。

本项目使用 SQLite。SQLite 是一个把数据保存在单个文件中的数据库，
非常适合学习和小型应用；生产环境再根据需求迁移到 PostgreSQL 等数据库。
"""

from collections.abc import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker


# SQLite 数据库文件会生成在项目根目录：fastapi_learning_app/tasks.db
DATABASE_URL = "sqlite:///./tasks.db"

# check_same_thread=False 是 SQLite 在 FastAPI 多线程场景下常用的配置。
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},
)

# sessionmaker 是“会话工厂”：每次请求可以从它得到一个独立数据库会话。
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)


class Base(DeclarativeBase):
    """所有 SQLAlchemy 模型的父类。"""


def get_db() -> Generator[Session, None, None]:
    """FastAPI 依赖：为一次请求提供数据库会话，并确保请求结束后关闭。

    yield 可以理解为“先把会话交给接口使用，接口结束后再执行 finally”。
    这能避免数据库连接没有关闭而逐渐耗尽。
    """

    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

