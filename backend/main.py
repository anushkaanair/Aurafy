from fastapi import FastAPI
from backend.routers.strategy_router import router as strategy_router

app = FastAPI(
    title="Aurafy AI Strategy API",
    version="1.0"
)

@app.get("/")
def home():
    return {
        "message": "Aurafy AI Strategy Engine is running",
        "docs": "/docs"
    }

app.include_router(strategy_router)