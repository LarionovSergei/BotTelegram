from typing import Optional, List

from pydantic import BaseModel

from model.variation import Variation


#TODO Добавить артикл
class Product(BaseModel):
    product_id: str
    name: Optional[str] = None
    description: Optional[str] = None
    thumbnail_url: Optional[str] = "https://google.com"
    variations: List[Variation] = []
