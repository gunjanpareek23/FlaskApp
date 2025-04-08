from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.orm import relationship
from app import db
import enum

class RoleEnum(enum.Enum):
    ADMIN = "admin"
    MANAGER = "manager"
    USER = "user"

class User(db.Model):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, index=True, nullable=False)
    role = Column(Enum(RoleEnum), default=RoleEnum.USER, nullable=False)

    # Relationship
    tasks = relationship("TaskManager", back_populates="assigned_user", lazy='dynamic', cascade="all, delete")
