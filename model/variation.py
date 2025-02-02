from pydantic import BaseModel
from typing_extensions import Optional

class Content(BaseModel):
    type: str
    url: str

class Variation(BaseModel):
    variation_id: str
    name: Optional[str] = None
    content: Content = Content(type="photo", url="https://google.com")
    button_text: Optional[str] = None
    unit_price: float = 0
    stock_quantity: int = 0

