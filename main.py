import os

from fastapi import FastAPI

import uvicorn

app = FastAPI(
    title = os.getenv("SERVICE_NAME", "Example PyTorch Service"),
    version = os.getenv("SERVICE_VERSION", "1.0.0"),
)

if __name__ == "__main__":
    uvicorn.run("main:app", host=os.getenv("SERVICE_HOST", "0.0.0.0"), port=int(os.getenv("SERVICE_PORT", 8000)), reload=True)
