from sqlalchemy import Column, Integer, DateTime, String, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app import db

class TaskLogger(db.Model):
    __tablename__ = 'task_logger'

    id = Column(Integer, primary_key=True)
    task_id = Column(Integer, ForeignKey('task_manager.id', ondelete='CASCADE'))
    status_change = Column(String(50))
    timestamp = Column(DateTime, default=datetime.utcnow)

    task = relationship("TaskManager", back_populates="logs", lazy='joined')

