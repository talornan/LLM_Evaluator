import asyncio
import sys

sys.path.append('../..')
from pydantic import BaseModel


# schemas/user_permissions.py
class UserPermissionBase(BaseModel):
    user_id: int
    prompt_id: int = None
    model_id: int = None


class UserPermission(UserPermissionBase):
    permission_id: int

    class Config:
        orm_mode = True
