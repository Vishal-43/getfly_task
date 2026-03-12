from pydantic import BaseModel
from typing import Optional
from datetime import date

class DPRCreate(BaseModel):
    date: date
    work_description: str
    weather: Optional[str] = None
    worker_count: int = 0