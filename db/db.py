from typing import Optional

from motor.motor_asyncio import AsyncIOMotorClient

from model.product import Product
from model.user import User


class DB:
    def __init__(self, client: AsyncIOMotorClient, db_name: str):
        self.client = client
        self.db = self.client[db_name]

    async def close(self):
        self.client.close()

    async def get_user(self, user_id: int) -> Optional[User]:
        user_data = await self.db["users"].find_one({"user_id": user_id})
        return User(**user_data) if user_data else None

    async def insert_user(self, user: User) -> User:
        await self.db["users"].insert_one(user.model_dump())
        return user

    async def update_user(self, user: User) -> User:
        await self.db["users"].update_one({"user_id": user.user_id},
                                          {"$set": user.model_dump()})
        return user

    async def get_product(self, product_id) -> Optional[Product]:
        product_data = await self.db["products"].find_one({"product_id": product_id})
        return Product(**product_data) if product_data else None

    async def insert_product(self, product) -> Product:
        await self.db["products"].insert_one(product.model_dump())
        return product

    async def update_product(self, product: Product) -> Product:
        await self.db["products"].update_one({"productK_id": product.product_id},
                                             {"$set": product.model_dump()})
        return product





