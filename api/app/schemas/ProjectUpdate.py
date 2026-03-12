from pydantic import BaseModel
from typing import Optional
from datetime import date
from app.models.PROJECTS import StatusEnum

class ProjectUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    status: Optional[StatusEnum] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None