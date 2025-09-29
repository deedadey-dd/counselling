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


class UserBase(BaseModel): # input schema
    username: str = Field(max_length=30, min_length=4)
    firstname: str = Field(max_length=50)
    othernames: Optional[str] = None
    lastname: str = Field(max_length=50)
    email: EmailStr = Field(max_length=100)


class UserCreate(UserBase):
    password: str = Field(min_length=6)

    """ 
    # commenting these out because they are not needed in the initial user creation
    # probably upon first login, a user may be directed to fill these details like partner_id
    # the user may select class they belong to however that must be approved by a facilitator, counsellor or admin
    """

    # partner_id: Optional[int] # FK - this will be filled later
    # session_id: int = 0 # FK - This is defualt value is 0
    # class_id: int = 0 # FK - to the Class Table


class UserOut(UserBase): # output schema
    id: int
    partner_id: Optional[int] = None # FK - this will be filled later
    session_id: Optional[int] = None # FK - This is defualt value is 0
    class_id: Optional[int] = None # FK - to the Class Table
    counselling_status: UserStatus = UserStatus.NOT_STARTED
    role: UserRole = UserRole.COUNSELLEE
    last_submitted_at: datetime = Field(default_factory=datetime.now)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)
    last_submitted_at: datetime = Field(default_factory=datetime.now)

    class Config:
        from_attributes = True # this allows returning SQLAlchemy objects


class UserLogin(BaseModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    password: str = Field(min_length=6)
