from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func, Enum
from sqlalchemy.orm import relationship, Mapped, mapped_column
from ..services import Base
import enum


class Classes(Base):
    __tablename__ = "classes"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    class_name: Mapped[str] = mapped_column(String, nullable=True)
    class_year: Mapped[int] = mapped_column(Integer)
    sessions: Mapped[list["Session"]] = relationship("Session", secondary="class_session", back_populates="classes")
    users: Mapped[list["User"]] = relationship("User", back_populates="class_")
    created_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True), server_default=func.now())


class Session(Base):
    __tablename__ = "session"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    session_topic: Mapped[str] = mapped_column(String, nullable=False)
    session_number: Mapped[int] = mapped_column(Integer, nullable=False)

    classes: Mapped[list["Classes"]] = relationship("Classes", secondary="class_session", back_populates="sessions")
    questions: Mapped[list["Question"]] = relationship("Question", back_populates="session", cascade="all, delete-orphan") # FK from the questions table providing the list of questions for the session

    users: Mapped[list["User"]] = relationship("User", back_populates="session")


class ClassSession(Base):
    __tablename__ = "class_session"

    class_id = mapped_column(ForeignKey("classes.id"), primary_key=True)
    session_id = mapped_column(ForeignKey("session.id"), primary_key=True)


class Question(Base):
    __tablename__ = "question"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    question: Mapped[str] = mapped_column(String, nullable=False)
    session_id: Mapped[int] = mapped_column(ForeignKey("session.id"))
    session: Mapped["Session"] = relationship("Session", back_populates="questions")
    answers: Mapped[list["Answer"]] = relationship("Answer", back_populates="question", cascade="all, delete-orphan")


class AnswerType(enum.Enum):
    INITIAL = "initial_views"
    NEW = "new_understanding"
    EXTRA = "extra"

class Answer(Base):
    __tablename__ = "answer"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    question_id: Mapped[int] = mapped_column(ForeignKey("question.id")) # FK - to the Class Table
    question: Mapped["Question"] = relationship("Question", back_populates="answers") # FK - from questions table
    
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id")) # FK - from the Users table 
    user: Mapped["User"] = relationship("User", back_populates="answers")
    
    answer: Mapped[str] = mapped_column(String, nullable=False)
    answer_type: Mapped[AnswerType] = mapped_column(Enum(AnswerType), nullable=False)