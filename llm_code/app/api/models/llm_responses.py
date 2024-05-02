# models/prompts.py
from sqlalchemy import Table, Column, Integer, Text, String, DateTime, ForeignKey, JSON
import asyncio
import sys

sys.path.append('../..')
from llm_code.app.core.config.db import meta

# models/llm_responses.py
llm_responses = Table(
    'LLMResponses', meta,
    Column('response_id', Integer, primary_key=True),
    Column('prompt_id', Integer, ForeignKey('Prompts.prompt_id'), nullable=False),
    Column('response_text', Text, nullable=False),
    Column('llm_model', String(100), nullable=False),
    Column('evaluation_metrics', JSON)
)