from fastapi import FastAPI
import os

app = FastAPI(
    title=os.getenv("SERVICE_NAME", "Example PyTorch Service"),
    version=os.getenv("SERVICE_VERSION", "1.0.0"),
)

@app.get("/")
def health():
    return {"status": "ok"}