# models/prompts.py
import sqlalchemy
from sqlalchemy import Table, Column, Integer, Text, String, DateTime, ForeignKey,select
import asyncio
import sys

sys.path.append('../..')
from llm_code.app.core.config.db import meta

prompts = Table(
    'Prompts', meta,
    Column('prompt_id', Integer, primary_key=True),
    Column('prompt_text', Text, nullable=False)
)

