import time
import logging
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware

logger = logging.getLogger("app.middleware")
logging.basicConfig(level=logging.INFO)

async def log_request_time(request: Request, call_next):
    start_time = time.perf_counter()
    response = await call_next(request)
    process_time = time.perf_counter() - start_time
    
    logger.info(
        f"Request: {request.method} {request.url.path} - "
        f"Status: {response.status_code} - "
        f"Completed in {process_time:.4f}s"
    )
    
    return response
