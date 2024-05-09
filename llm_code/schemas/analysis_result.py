# schemas/prompts.py
import asyncio
import sys
from typing import List

sys.path.append('../..')
from pydantic import BaseModel


class Analysis_Result(BaseModel):
    prompt: str
    response: str
    metric_name: str
    metric_value: str
    model_name: str


class AggRequest(BaseModel):
    model_ids: List[str]
    metrics_name: List[str]


class AggResponse(BaseModel):
    model_id: str
    metric_name: str
    average: float
    maximum: float
    minimum: float
    total: float
    count: float
