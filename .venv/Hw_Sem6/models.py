
from pydantic import BaseModel, Field


class UserIn(BaseModel):
    name: str = Field(max_length=32)
    lastname: str = Field(max_length=32)
    mail: str = Field(max_length=128)
    password: str = Field(min_length=6)
    
class User(UserIn):
    id: int
    
class ProductIn(BaseModel):
    name: str = Field(max_length=128)
    desc: str = Field(max_length=128)
    price: int
    
class Product(ProductIn):
    id: int
    
class OrderIn(BaseModel):
    user_id: int
    product_id: int
    
class Order(OrderIn):
    id: int