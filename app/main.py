from fastapi import FastAPI

from .db import init_db
from . import models  # noqa: F401

app = FastAPI(title="FastAPI + SQLModel + Alembic")


@app.on_event("startup")
def on_startup() -> None:
    init_db()


@app.get("/health")
def health() -> dict[str, bool]:
    return {"ok": True}
