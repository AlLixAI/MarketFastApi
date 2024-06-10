from sqlalchemy import MetaData, Table, Column, Integer, String, CheckConstraint

from src.database import metadata

product = Table(
    "product",
    metadata,
    Column("id", Integer, primary_key=True, index=True, autoincrement=True),
    Column("name", String, unique=True, nullable=False, index=True),
    Column("price", Integer, nullable=False),
    Column("stock", Integer, CheckConstraint("price >= 0"), nullable=False),
    Column("image_url", String, nullable=False)
)
