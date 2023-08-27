from fastapi import APIRouter, Response
from database import *
from models import *
from typing import List

router = APIRouter()
PRICE_IND = 1000


@router.get("/fake_products/{count}")
async def create_products(count: int):
    for i in range(count):
        query = products.insert().values(name=f'product{i}', desc=f'Some good product', price=i+PRICE_IND)
        await database.execute(query)
    return {'message': f'{count} fake products created'}


@router.post("/products/", response_model=Product)
async def create_prod(prod: ProductIn):
    query = products.insert().values(name=prod.name, desc=prod.desc, price=prod.price)
    last_record_id = await database.execute(query)
    return {**prod.model_dump(), "id": last_record_id}


@router.get("/products/", response_model=List[Product])
async def read_products():
    query = products.select()
    return await database.fetch_all(query)


@router.get("/products/{id}", response_model=Product)
async def read_prod(id: int):
    query = products.select(). where(products.c.id == id)
    return await database.fetch_one(query)


@router.put("/products/{id}", response_model=Product)
async def update_product(id: int, new_prod: ProductIn):
    query = products.update().where(products.c.id == id).values(**new_prod.model_dump())
    await database.execute(query)
    return {**new_prod.model_dump(), "id": id}


@router.delete("/products/{id}")
async def delete_product(id: int):
    query = products.delete().where(products.c.id == id)
    await database.execute(query)
    return {'message': 'Product deleted'}