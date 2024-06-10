from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from src.auth.base_config import current_user
from src.auth.models import User
from src.database import get_async_session

from src.operations.product.models import product
from src.operations.product.schemas import ProductCreate, ProductRead

router = APIRouter(
    prefix="/product",
    tags=["Product"]
)

@router.get("/{product_id}", response_model=ProductRead)
async def get_product(
        product_id: int,
        session: AsyncSession = Depends(get_async_session)
):
    query = select(product).where(product.c.id == product_id)
    result = await session.execute(query)
    product_data = result.fetchone()

    if product_data is None:
        raise HTTPException(status_code=404, detail="Product not found")

    return product_data._asdict()

@router.get("/", response_model=List[ProductRead])
async def get_product(
        session: AsyncSession = Depends(get_async_session)
):
    query = select(product)
    result = await session.execute(query)
    product_data = result.fetchall()

    if product_data is None:
        raise HTTPException(status_code=404, detail="Product not found")

    return [product._asdict() for product in product_data]



@router.post("/")
async def add_product(
        new_product: ProductCreate,
        session: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_user)
):
    stmt = insert(product).values(new_product.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": f"success, добавлено пользователем {user.username}"}