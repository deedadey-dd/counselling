import psycopg2
from pydantic import BaseModel, Field, EmailStr, field_validator
from typing import Optional
from datetime import datetime
from enum import Enum

class Classes(BaseModel):
    id: int
    class_name: str
    class_year: int = Field(max_digits=4, default_factory=datetime.now().year)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)


class Sessions(BaseModel):
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
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)
