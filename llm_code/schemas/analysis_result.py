# schemas/prompts.py
import asyncio
import sys

sys.path.append('../..')
from pydantic import BaseModel


class Analysis_Result(BaseModel):
    prompt: str
    response: str
    metric_name: str
    metric_value: str
    model_name: str
