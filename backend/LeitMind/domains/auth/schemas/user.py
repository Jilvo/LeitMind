from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class UserCreationRequest(BaseModel):
    username: str
    email: str
    password: str
    country: str


class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    country: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class UserUpdateRequest(BaseModel):
    username: Optional[str]
    email: Optional[str]
    country: Optional[str]
    password: Optional[str]
    new_password: Optional[str]
    confirm_password: Optional[str]
    user_id: Optional[int]


class UserRecuperationRequest(BaseModel):
    id: Optional[int]
    username: Optional[str]
    email: Optional[str]


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None


class UserLoginRequest(BaseModel):
    username: str
    password: str
