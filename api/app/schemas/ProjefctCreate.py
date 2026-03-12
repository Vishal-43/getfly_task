from pydantic import BaseModel
from typing import Optional
from datetime import date
from ..models.PROJECTS import StatusEnum



class ProjectCreate(BaseModel):
    name: str
    description: Optional[str] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    status: Optional[StatusEnum] = StatusEnum.planned