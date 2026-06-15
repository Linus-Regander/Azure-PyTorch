import os

from app.api.router.router import main_router

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

def app() -> FastAPI:
    app = FastAPI(
        title=os.getenv("SERVICE_NAME", "Example PyTorch Service"),
        version=os.getenv("SERVICE_VERSION", "1.0.0"),
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(main_router, prefix="/api/v1")

    return app

app = app()