from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import Optional, List
from ..database import get_db
from ..models.PROJECTS import Project
from ..models.USER import User
from ..schemas.ProjefctCreate import ProjectCreate
from ..schemas.ProjectUpdate import ProjectUpdate
from ..schemas.ProjectResponse import ProjectResponse
from ..auth import get_current_user, require_role

router = APIRouter(prefix="/projects", tags=["Projects"])

@router.post("", status_code=201)
def create_project(
    data: ProjectCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role("admin", "manager"))
):
    project = Project(**data.model_dump(), created_by=current_user.id)
    db.add(project)
    db.commit()
    db.refresh(project)
    return {"projectId": project.id, "message": "Project created"}

@router.get("", response_model=List[ProjectResponse])
def list_projects(
    status: Optional[str] = Query(None),
    limit: int = Query(10, ge=1, le=100),
    offset: int = Query(0, ge=0),
    db: Session = Depends(get_db),
    _: User = Depends(get_current_user)
):
    query = db.query(Project)
    if status:
        query = query.filter(Project.status == status)
    return query.offset(offset).limit(limit).all()

@router.get("/{id}", response_model=ProjectResponse)
def get_project(id: int, db: Session = Depends(get_db), _: User = Depends(get_current_user)):
    project = db.query(Project).filter(Project.id == id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return project

@router.put("/{id}")
def update_project(id: int,data: ProjectUpdate, db: Session = Depends(get_db),current_user: User = Depends(require_role("admin", "manager"))):
    project = db.query(Project).filter(Project.id == id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    for k, v in data.model_dump(exclude_unset=True).items():
        setattr(project, k, v)
    db.commit()
    return {"message": "Project updated"}

@router.delete("/{id}")
def delete_project(id: int,db: Session = Depends(get_db),_: User = Depends(require_role("admin"))):
    project = db.query(Project).filter(Project.id == id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    db.delete(project)
    db.commit()
    return {"message": "Project deleted"}