import psycopg2
from pydantic import BaseModel, Field, EmailStr, validator
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


class User(BaseModel):
    id: int 
    username: str = Field(max_length=30)
    firstname: str = Field(max_length=50)
    othernames: Optional[str] = None
    lastname: str = Field(max_length=50)
    email: EmailStr = Field(max_length=100)
    partner_id: Optional[int] # FK - this will be filled later
    session_id: int = 0 # FK - This is defualt value is 0
    class_id: int # FK - to the Class Table
    role: UserRole
    counselling_status: UserStatus
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)
    last_submitted_at: datetime = Field(default_factory=datetime.now)


    # # This is how to create custom validators

    # @validator("age")
    # def validate_age(cls, value):
    #     if value < 0:
    #         raise ValueError(f"age must be positive; you entered {age}")
    #     return value


class Classes(BaseModel):
    id: int
    class_name: str
    class_year: int = Field(max_digits=4)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)


class Session(BaseModel):
    id: int
    session_topic: str
    session_number: int
    questions: list[int] # FK from the questions table providing the list of questions for the session


class Question(BaseModel):
    id: int
    question: str


class Answer(BaseModel):
    id:int
    question: int # FK - from questions table
    user: int # FK - from the Users table 
    answer: str

