from pydantic import BaseModel
from typing import Optional
from datetime import date, datetime


class DPRResponse(BaseModel):
    id: int
    project_id: int
    user_id: int
    date: date
    work_description: str
    weather: Optional[str]
    worker_count: int
    created_at: datetime

    class Config:
        from_attributes = True