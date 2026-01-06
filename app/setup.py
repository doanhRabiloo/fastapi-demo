from fastapi import FastAPI
from app.middlewares.logging import log_request_time

def setup(app: FastAPI):
  app.middleware("http")(log_request_time)
