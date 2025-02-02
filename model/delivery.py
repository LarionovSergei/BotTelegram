from pydantic import BaseModel

class Delivery(BaseModel):
    user_id: int
    fullname: str
    method: str
    address: str
    phone: str
    email: str


