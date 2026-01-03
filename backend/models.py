from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base, relationship
from pydantic import BaseModel

Base = declarative_base()


#Base user model
class UsersBase(BaseModel):
    id : int
    username : str
    disabled : bool
    model_config = {"from_attributes": True}

#table structure
class User(Base):

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False, unique=True)
    hashed_password = Column(String, nullable=False)
    disabled = Column(Boolean, default=True)

#user create model
class UserCreate(BaseModel):
    username : str
    password : str

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


class TokenData(BaseModel):
    id: int | None = None
