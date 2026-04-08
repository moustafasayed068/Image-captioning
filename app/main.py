from fastapi import FastAPI

from app.api.router import api_router
from app.core.config import Settings

settings = Settings()

app = FastAPI(
    title=settings.app_name,
    description="Image caption generation API using FastAPI.",
    version="0.1.0",
)

app.include_router(api_router, prefix=settings.api_prefix)


@app.get("/", tags=["health"])
async def health_check() -> dict:
    return {"status": "ok", "message": "Image Captioning API is running."}
