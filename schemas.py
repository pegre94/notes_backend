from typing import List

from pydantic import BaseModel


class ItemBase(BaseModel):
    name: str = None
    content: str = None
    creationDate: str
    creationTime: str
    editionDate: str
    editionTime: str
    public: bool



class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: str

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    items: List[Item] = []

    class Config:
        orm_mode = True