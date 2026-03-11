from fastapi import APIRouter
from pydantic import BaseModel

from backend.services.strategy_engine import StrategyEngine

router = APIRouter(prefix="/strategy", tags=["Strategy"])

engine = StrategyEngine()


class StrategyRequest(BaseModel):
    idea: str


@router.post("/generate")
def generate_strategy(request: StrategyRequest):

    result = engine.generate_strategy(request.idea)

    return result

from backend.data.tasks import TASK_LIBRARY

@router.get("/tasks")
def get_available_tasks():
    return list(TASK_LIBRARY.keys())