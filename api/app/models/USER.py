from sqlalchemy import Column, Integer, String, Text, Date, Enum, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base
import enum

class RoleEnum(enum.Enum):
    admin = "admin"
    manager = "manager"
    worker = "worker"

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    role = Column(Enum(RoleEnum), default=RoleEnum.worker)
    created_at = Column(TIMESTAMP, server_default=func.now())

    projects = relationship("Project", back_populates="creator")
    reports = relationship("DailyReport", back_populates="user")