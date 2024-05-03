from sqlalchemy import Table, Column, Integer, String, ForeignKey
import asyncio
import sys

sys.path.append('../..')
from llm_code.app.core.config.db import meta


llm_models = Table(
    'LLMModels', meta,
    Column('model_id', Integer, primary_key=True),
    Column('model_name', String(100), nullable=False),
    Column('developer_id', Integer, ForeignKey('Users.user_id'), nullable=False)
)