from fastapi import FastAPI
from app.api.v1.api import router as api_router
from app.setup import setup

app = FastAPI(title="FastAPI Demo")

setup(app)

app.include_router(api_router, prefix="/api/v1")