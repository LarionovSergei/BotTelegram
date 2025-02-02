from typing import Dict

from pydantic import BaseModel

class Cart(BaseModel):
    user_id: int
    variations: Dict[str, int] = {}
