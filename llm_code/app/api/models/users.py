from sqlalchemy import Table, Column, Integer, String, Enum
import asyncio
import sys

sys.path.append('../..')
from llm_code.app.core.config.db import meta

users = Table(
    'Users', meta,
    Column('user_id', Integer, primary_key=True),
    Column('username', String(100), nullable=False),
    Column('password', String(100), nullable=False),
    Column('user_type', Enum('prompt_engineer', 'model_developer', name='user_types'), nullable=False),
    Column('email', String(255), nullable=False)
)