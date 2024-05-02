# schemas/prompts.py
import asyncio
import sys

sys.path.append('../..')
from pydantic import BaseModel


class Prompt(BaseModel):
    prompt_id: int
    prompt_text: str
