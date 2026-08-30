# src/schemas/category.py

from pydantic import BaseModel


class CategoryCreate(BaseModel):
    name: str
    is_active: bool


class CategoryResponse(BaseModel):
    id: int
    name: str
    is_active: bool

    model_config = {
        "from_attributes": True,
    }
