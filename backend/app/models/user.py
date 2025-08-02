from typing import Optional, List
from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from enum import Enum

class UserRole(str, Enum):
    PATIENT = "patient"
    DOCTOR = "doctor"
    ADMIN = "admin"

class UserBase(BaseModel):
    email: EmailStr
    full_name: str
    role: UserRole

class UserCreate(UserBase):
    password: str

class UserUpdate(BaseModel):
    email: Optional[EmailStr] = None
    full_name: Optional[str] = None
    password: Optional[str] = None

class UserInDB(UserBase):
    id: str = Field(..., alias="_id")
    hashed_password: str
    is_active: bool = True
    created_at: datetime = Field(default_factory=datetime.utcnow)
    blockchain_address: Optional[str] = None

    model_config = {
        "populate_by_name": True,
        "json_schema_extra": {
            "examples": [
                {
                    "email": "user@example.com",
                    "full_name": "John Doe",
                    "role": "patient",
                    "hashed_password": "secret",
                    "is_active": True,
                    "blockchain_address": None
                }
            ]
        }
    }

class User(UserBase):
    id: str
    is_active: bool
    created_at: datetime
    blockchain_address: Optional[str] = None

    model_config = {
        "populate_by_name": True,
        "json_schema_extra": {
            "examples": [
                {
                    "email": "user@example.com",
                    "full_name": "John Doe",
                    "role": "patient",
                    "is_active": True,
                    "blockchain_address": None
                }
            ]
        }
    } 