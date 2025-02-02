from datetime import datetime
from typing import Dict

from pydantic import BaseModel

from model.delivery import Delivery


class Order(BaseModel):
    order_id: str
    user_id: int
    date: datetime
    status: str
    payment_url: str
    variations: Dict[str, int]
    delivery: Delivery
    amount: float
    cost_delivery: float
    total_amount: float