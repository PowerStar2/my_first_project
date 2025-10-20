# app/schemas.py
from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

# Pydantic v2 style: use model_config for from_attributes
class _ORMConfig:
    model_config = {"from_attributes": True}

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    username: str
    password: str

class UserOut(BaseModel, _ORMConfig):
    id: int
    username: str
    email: EmailStr
    created_at: datetime

class FireDetectionCreate(BaseModel):
    user_id: int
    # either upload on /upload or provide image_path externally
    image_path: Optional[str] = None

class FireDetectionOut(BaseModel, _ORMConfig):
    id: int
    image_path: str
    result: str
    confidence: Optional[str]
    detected_at: datetime
    user_id: int

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"
