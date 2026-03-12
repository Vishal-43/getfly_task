from sqlalchemy import Column, Integer, String, Text, Date, Enum, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base
import enum


class DailyReport(Base):
    __tablename__ = "daily_reports"
    id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer, ForeignKey("projects.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    date = Column(Date, nullable=False)
    work_description = Column(Text)
    weather = Column(String(100))
    worker_count = Column(Integer, default=0)
    created_at = Column(TIMESTAMP, server_default=func.now())
    project = relationship("Project", back_populates="reports")
    user = relationship("User", back_populates="reports")