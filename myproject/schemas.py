from pydantic import BaseModel, Field


class ItemBase(BaseModel):
    title: str
    description: str | None = None

class ReviewCreate(ItemBase):
    stars: int = Field(ge=1, le=10)

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
