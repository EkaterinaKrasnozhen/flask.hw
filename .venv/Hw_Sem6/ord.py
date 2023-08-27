from fastapi import APIRouter
from database import *
from models import *
from typing import List

router = APIRouter()


@router.get("/fake_orders/")
async def create_post():
    query = orders.insert().values(user_id=2, product_id=1)
    await database.execute(query)
    return {'ok'}


@router.get("/orders/")
async def read_orders():
    query = orders.select()
    return await database.fetch_all(query)
    
    
@router.post("/orders/", response_model=Order)
async def new_order(order: OrderIn):
    query = orders.insert().values(user_id=order.user_id, product_id=order.product_id)
    last_record_id = await database.execute(query)
    return {**order.model_dump(), "id": last_record_id}


@router.put("/orders/{order_id}", response_model=Order)
async def update_order(order_id: int, new_order: OrderIn):
    query = orders.update().where(orders.c.id == order_id).values(**new_order.model_dump())
    await database.execute(query)
    return {**new_order.model_dump(), "id": order_id}


@router.delete("/orders/{order_id}")
async def delete_order(order_id: int):
    query = orders.delete().where(orders.c.id == order_id)
    await database.execute(query)
    return {'message': 'Order deleted'}