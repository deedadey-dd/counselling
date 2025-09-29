from pydantic import BaseModel, Field, field_validator
from typing import Optional, List
from datetime import datetime
from enum import Enum


class ClassesBase(BaseModel):
    class_name: str
    class_year: int = Field(max_digits=4, default_factory=datetime.now().year)


class ClassesCreate(ClassesBase):
    # this is going to be the same as the base so no need to add nything
    pass


class ClassesOut(ClassesBase):
    id: int
    sessions: list["SessionsOut"] = []
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)

    class Config:
        from_attributes = True


class SessionsBase(BaseModel):
    session_topic: str
    session_number: int


class SessionsCreate(SessionsBase):
    # same as base
    pass


class SessionsOut(SessionsBase):
    id: int
    questions: List[int] # FK from the questions table providing the list of questions for the session

    class Config:
        from_attributes = True


class QuestionBase(BaseModel):
    question: str


class QuestionCreate(QuestionBase):
    session_id: int # FK to Session


class QuestionOut(QuestionBase):
    id: int

    class Config:
        from_attributes = True


class AnswerType(str, Enum):
    INITIAL = "initial_views"
    NEW = "new_understanding"
    EXTRA = "extra"


class AnswerBase(BaseModel):
    answer: str
    answer_type: AnswerType


class AnswerCreate(AnswerBase):
    question_id: int # FK - from questions table
    user_id: int # FK - from the Users table 


class AnswerOut(AnswerBase):
    id:int
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)

    class Config:
        from_attributes = True
