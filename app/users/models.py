from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from services import Base


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


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=False)
    firstname = Column(String, nullable=False)
    othernames = Column(String, nullable=True)
    lastname = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    partner_id =  Column(Integer, ForeignKey("users.id"), nullable=True) # not all users will have partners
    partner = relationship("User", remote_side=[id], backref="partners")
    session_id = Column(Integer, ForeignKey("session.id")) # FK - This is defualt value is 0
    class_id =  Column(Integer, ForeignKey("classes.id")) # FK - to the Class Table
    class_ = relationship("Class", back_populates="users")
    role: UserRole
    counselling_status: UserStatus
    created_at = Column(DateTime(timezone=True), server_default=function.now())
    updated_at = Column(DateTime(timezone=True), server_default=function.now())
    last_submitted_at = Column(DateTime(timezone=True), server_default=function.now())


    # # This is how to create custom validators

    # @validator("age")
    # def validate_age(cls, value):
    #     if value < 0:
    #         raise ValueError(f"age must be positive; you entered {age}")
    #     return value


class Classes(Base):
    id = Column(Integer, primary_key=True, index=True)
    class_name: str
    class_year: int = Field(max_digits=4)
    created_at = Column(DateTime(timezone=True), server_default=function.now())
    updated_at = Column(DateTime(timezone=True), server_default=function.now())


class Session(Base):
    id = Column(Integer, primary_key=True, index=True)
    session_topic = Column(String, nullable=False)
    session_number = Column(Integer, nullable=False)
    questions: list[int] # FK from the questions table providing the list of questions for the session


class Question(Base):
    id = Column(Integer, primary_key=True, index=True)
    question = Column(String, nullable=False)


class Answer(Base):
    id = Column(Integer, primary_key=True, index=True)
    question = Column(Integer, ForeignKey("classes.id")) # FK - to the Class Table
    question_ = relationship("Question", back_populates="question") # FK - from questions table
    user = Column(Integer, ForeignKey("users.id")) # FK - from the Users table 
    user_ = relationship("User", back_populates="users")
    answer = Column(String, nullable=False)