from pydantic import BaseModel
from typing_extensions import Optional


class User(BaseModel):
    user_id: int
    username: Optional[str] = None
