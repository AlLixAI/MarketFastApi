import pytest
from sqlalchemy import insert, select
from httpx import AsyncClient
from src.auth.models import role
from tests.conftest import client, async_session_maker, ac


@pytest.mark.asyncio
async def test_add_role():
    async with async_session_maker() as session:
        stmt = insert(role).values(id=1, name="randomchik", permissions=None)
        await session.execute(stmt)
        await session.commit()

        query = select(role)
        result = await session.execute(query)
        assert result.all() == [(1, 'randomchik', None)], "Роль не добавилась"

@pytest.mark.asyncio
async def test_register(ac: AsyncClient):
    response = await ac.post("/auth/register", json={
        "email": "string",
        "password": "string",
        "is_active": True,
        "is_superuser": False,
        "is_verified": False,
        "username": "string",
        "role_id": 1
    })

    assert response.status_code == 201