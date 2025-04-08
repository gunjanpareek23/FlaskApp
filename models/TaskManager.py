from sqlalchemy import Column, Integer, String, Date, Boolean, Enum, ForeignKey
from sqlalchemy.orm import relationship
from app import db
import enum

class PriorityEnum(enum.Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    CRITICAL = "CRITICAL"

class TaskManager(db.Model):
    __tablename__ = 'task_manager'

    id = Column(Integer, primary_key=True)
    task_name = Column(String(100), nullable=False, index=True)
    description = Column(String(255))
    status = Column(Boolean, default=True)
    priority = Column(Enum(PriorityEnum), nullable=False)
    created_at = Column(Date, nullable=False)

    # Foreign Key to User
    assigned_user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'))
    assigned_user = relationship("User", back_populates="tasks", lazy='joined')

    # Relationship with logs
    logs = relationship("TaskLogger", back_populates="task", cascade="all, delete", lazy='dynamic')

