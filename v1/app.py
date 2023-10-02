from fastapi import FastAPI

from v1 import src

app = FastAPI(
    title="Template FastAPI",
    docs_url="/api/v1/docs",
    redoc_url="/api/v1/redoc",
    version="1"
)

app.include_router(src.router)
