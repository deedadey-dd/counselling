from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from ..services import Base


class Classes(Base):
    __tablename__ = "classes"

    id = Column(Integer, primary_key=True, index=True)
    class_name = Column(String, nullable=True)
    class_year = Column(Integer)
    created_at = Column(DateTime(timezone=True), server_default=function.now())
    updated_at = Column(DateTime(timezone=True), server_default=function.now())


class Session(Base):
    __tablename__ = "session"

    id = Column(Integer, primary_key=True, index=True)
    session_topic = Column(String, nullable=False)
    session_number = Column(Integer, nullable=False)
    questions: list[int] # FK from the questions table providing the list of questions for the session


class Question(Base):
    __tablename__ = "question"

    id = Column(Integer, primary_key=True, index=True)
    question = Column(String, nullable=False)


class Answer(Base):
    __tablename__ = "answer"

    id = Column(Integer, primary_key=True, index=True)
    question = Column(Integer, ForeignKey("classes.id")) # FK - to the Class Table
    question_ = relationship("Question", back_populates="question") # FK - from questions table
    user = Column(Integer, ForeignKey("users.id")) # FK - from the Users table 
    user_ = relationship("User", back_populates="users")
    answer = Column(String, nullable=False)