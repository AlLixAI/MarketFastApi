from pydantic import BaseModel, ConfigDict


class ProductCreate(BaseModel):
    name: str
    price: int
    stock: int
    image_url: str

    model_config = ConfigDict(from_attributes=True)

class ProductRead(BaseModel):
    id: int
    name: str
    price: int
    stock: int
    image_url: str

    model_config = ConfigDict(from_attributes=True)