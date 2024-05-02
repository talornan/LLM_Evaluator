from sqlalchemy import Table, Column, Integer, String, ForeignKey
import asyncio
import sys

sys.path.append('../..')
from llm_code.app.core.config.db import meta

# models/user_permissions.py
user_permissions = Table(
    'UserPermissions', meta,
    Column('permission_id', Integer, primary_key=True),
    Column('user_id', Integer, ForeignKey('Users.user_id'), nullable=False),
    Column('prompt_id', Integer, ForeignKey('Prompts.prompt_id')),
    Column('model_id', Integer, ForeignKey('LLMModels.model_id'))
)