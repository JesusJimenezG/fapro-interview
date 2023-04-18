from typing import Union

from fastapi import FastAPI

from app.uf.router import router

app = FastAPI()

app.include_router(router, prefix="/api")


@app.get("/health-check")
def health_check():
    return {"status": "ok"}
