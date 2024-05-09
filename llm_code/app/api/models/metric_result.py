from sqlalchemy import Table, Column, Integer, String, Enum, Float
import asyncio
import sys

sys.path.append('../..')
from llm_code.app.core.config.db import meta

metric_result = Table(
    'metric_result', meta,
    Column('username', String(100), primary_key=True),
    Column('metric_name', String(100), nullable=False),
    Column('prompt', String(100), nullable=False),
    Column('prompt_generation', Enum('prompt_engineer', 'model_developer', name='user_types'), nullable=False),
    Column('metric_value', Float, nullable=False),
    Column('model_id', String(100), nullable=False)

)


