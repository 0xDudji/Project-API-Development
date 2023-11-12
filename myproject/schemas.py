from pydantic import BaseModel


class ItemBase(BaseModel):
    title: str
    description: str | None = None

class ReviewCreate(ItemBase):
    pass

class Review(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True



class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool
    Reviews: list[Review] = []

    class Config:
        orm_mode = True
