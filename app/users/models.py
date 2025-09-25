from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Enum as SqlEnum
from sqlalchemy.orm import relationship
from ..services import Base
from .schema import UserRole, UserStatus


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=False)
    firstname = Column(String, nullable=False)
    othernames = Column(String, nullable=True)
    lastname = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String) # must be hashed before saving
    partner_id =  Column(Integer, ForeignKey("users.id"), nullable=True) # not all users will have partners
    partner = relationship("User", remote_side=[id], backref="partners")
    session_id = Column(Integer, ForeignKey("session.id")) # FK - This is defualt value is 0
    class_id =  Column(Integer, ForeignKey("classes.id")) # FK - to the Class Table
    class_ = relationship("Class", back_populates="users")
    role = Column(SqlEnum(UserRole), default=UserRole.COUNSELLEE, nullable=False)
    counselling_status = Column(SqlEnum(UserStatus), default=UserStatus.NOT_STARTED)
    created_at = Column(DateTime(timezone=True), server_default=function.now())
    updated_at = Column(DateTime(timezone=True), server_default=function.now())
    last_submitted_at = Column(DateTime(timezone=True), server_default=function.now())

