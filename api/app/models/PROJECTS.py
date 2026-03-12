from sqlalchemy import Column, Integer, String, Text, Date, Enum, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base
import enum


class StatusEnum(str, enum.Enum):
    planned = "planned"
    active = "active"
    completed = "completed"


class Project(Base):
    __tablename__ = "projects"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200), nullable=False)
    description = Column(Text)
    start_date = Column(Date)
    end_date = Column(Date)
    status = Column(Enum(StatusEnum), default=StatusEnum.planned)
    created_by = Column(Integer, ForeignKey("users.id"))
    created_at = Column(TIMESTAMP, server_default=func.now())
    creator = relationship("User", back_populates="projects")
    reports = relationship("DailyReport", back_populates="project")