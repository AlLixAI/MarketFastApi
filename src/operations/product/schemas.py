from pydantic import BaseModel


class ProductCreate(BaseModel):
    name: str
    price: int
    stock: int
    image_url: str

    class Config:
        orm_mode = True

class ProductRead(BaseModel):
    id: int
    name: str
    price: int
    stock: int
    image_url: str

    class Config:
        orm_mode = True