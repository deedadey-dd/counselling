from pydantic import BaseModel, Field, EmailStr
from typing import Optional
from datetime import datetime
from enum import Enum


# 
class UserRole(str, Enum):
    COUNSELLOR = "counsellor"
    COUNSELLEE = "counsellee"
    FACILITATOR = "facilitator"
    ADMINISTRATOR = "admin"


class UserStatus(str, Enum):
    NOT_STARTED = "not started"
    LAGGING = "lagging"
    UP_TO_DATE = "up to date"
    COMPLETED = "completed"


class UserCreate(BaseModel): # input schema
    username: str = Field(max_length=30)
    firstname: str = Field(max_length=50)
    othernames: Optional[str] = None
    lastname: str = Field(max_length=50)
    email: EmailStr = Field(max_length=100)
    password: str
    partner_id: Optional[int] # FK - this will be filled later
    session_id: int = 0 # FK - This is defualt value is 0
    class_id: int = 0 # FK - to the Class Table
    role: UserRole = "counsellee"
    counselling_status: UserStatus = "not started"
    last_submitted_at: datetime = Field(default_factory=datetime.now)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)


class UserOut(BaseModel): # output schema
    id: int
    username: str = Field(max_length=30)
    firstname: str = Field(max_length=50)
    othernames: Optional[str] = None
    lastname: str = Field(max_length=50)
    email: EmailStr = Field(max_length=100)
    password: str
    partner_id: Optional[int] # FK - this will be filled later
    session_id: int = 0 # FK - This is defualt value is 0
    class_id: int # FK - to the Class Table
    role: UserRole
    counselling_status: UserStatus
    last_submitted_at: datetime = Field(default_factory=datetime.now)

    class Config:
        orm_mode = True # this allows returning SQLAlchemy objects



