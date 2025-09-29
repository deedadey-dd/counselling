from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Enum as SqlEnum, func
from sqlalchemy.orm import relationship, Mapped, mapped_column
from ..services import Base
from .schema import UserRole, UserStatus
# from app.models import Answer


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    username: Mapped[str] = mapped_column(String(30), nullable=False)
    firstname: Mapped[str] = mapped_column(String(50), nullable=False)
    othernames: Mapped[str] = mapped_column(String(50), nullable=True)
    lastname: Mapped[str] = mapped_column(String(50), nullable=False)
    email: Mapped[str] = mapped_column(String, unique=True, index=True, nullable=False)
    password: Mapped[str] = mapped_column(String) # must be hashed before saving
    
    partner_id: Mapped[int | None] =  mapped_column(ForeignKey("users.id"), nullable=True) # not all users will have partners esp. facilitators
    partner: Mapped["User"] = relationship("User", remote_side="User.id", backref="partners")
    
    session_id: Mapped[int] = mapped_column(ForeignKey("session.id"), nullable=True) # FK - This is defualt value is 0
    session: Mapped["Session"] = relationship("Session", back_populates="users")

    class_id: Mapped[int] =  mapped_column(ForeignKey("classes.id"), nullable=True) # FK - to the Class Table
    class_:Mapped["Classes"]= relationship("Classes", back_populates="users")

    role: Mapped[UserRole] = mapped_column(
        SqlEnum(UserRole, name="userrole", native_enum=False), 
        default=UserRole.COUNSELLEE, nullable=False
        )
    
    counselling_status: Mapped[UserStatus] = mapped_column(SqlEnum(UserStatus), default=UserStatus.NOT_STARTED.value, nullable=False)
    
    answers: Mapped[list["Answer"]] = relationship("Answer", back_populates="user", cascade="all, delete-orphan")

    created_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    last_submitted_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True), server_default=func.now())

    

