from database import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    name = Column(String, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    # Specify the foreign key relationship for the 'reviews' attribute
    reviews = relationship("Review", back_populates="owner", foreign_keys="[Review.owner_id]")

class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)
    stars = Column(Integer, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))
    name = Column(String, ForeignKey("users.name"))

    # Specify the foreign key relationship for the 'owner' attribute
    owner = relationship("User", back_populates="reviews", foreign_keys="[Review.owner_id]")
