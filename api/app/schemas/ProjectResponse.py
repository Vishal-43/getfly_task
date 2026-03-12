from pydantic import BaseModel
from datetime import date, datetime
from typing import Optional
from app.models.PROJECTS import StatusEnum

class ProjectResponse(BaseModel):
    id: int
    name: str
    description: Optional[str]
    status: StatusEnum
    start_date: Optional[date]
    end_date: Optional[date]
    created_by: Optional[int]
    created_at: datetime
    class Config:
        from_attributes = True