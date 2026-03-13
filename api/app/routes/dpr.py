from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import Optional, List
from datetime import date
from ..database import get_db
from ..models.DRP import DailyReport
from ..models.PROJECTS import Project
from ..models.USER import User
from ..schemas.DPRCreate import DPRCreate
from ..schemas.DPRRespoinse import DPRResponse
from ..auth import get_current_user, require_role

router = APIRouter(prefix="/projects", tags=["DPR"])

@router.post("/{id}/dpr", status_code=201)
def create_dpr(
    id: int,
    data: DPRCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role("admin", "manager", "worker"))
):
    if not db.query(Project).filter(Project.id == id).first():
        raise HTTPException(status_code=404, detail="Project not found")
    
    report = DailyReport(**data.model_dump(), project_id=id, user_id=current_user.id)
    db.add(report)
    db.commit()
    db.refresh(report)
    return {"dprId": report.id, "message": "DPR created"}

@router.get("/{id}/dpr", response_model=List[DPRResponse])
def list_dprs(
    id: int,
    date: Optional[date] = Query(None),
    db: Session = Depends(get_db),
    _: User = Depends(get_current_user)
):
    query = db.query(DailyReport).filter(DailyReport.project_id == id)
    if date:
        query = query.filter(DailyReport.date == date)
    return query.all()