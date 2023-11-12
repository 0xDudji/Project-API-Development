from pydantic import BaseModel, Field, EmailStr


class ItemBase(BaseModel):
    description: str | None = None
    stars: int = Field(ge=1, le=10)
    name: str

class ReviewCreate(ItemBase):
    pass

class Review(ItemBase):
    id: int
    owner_id: int


    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: EmailStr
    name: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool
    Reviews: list[Review] = []

    class Config:
        orm_mode = True
