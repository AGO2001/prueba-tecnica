# backend/main.py
from typing import Optional
from datetime import datetime
from fastapi import FastAPI, Depends, HTTPException, status, Query
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from pydantic import BaseModel, Field, field_validator

# Imports absolutos
from backend.database import engine, Base, get_db
from backend import models

# Crear las tablas en PostgreSQL automáticamente
Base.metadata.create_all(bind=engine)

app = FastAPI(title="API de Prueba Técnica")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Esquemas Pydantic
class TaskCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=120)
    priority: str = Field(default="medium")

    @field_validator("priority")
    def validate_priority(cls, value):
        allowed = ["low", "medium", "high"]
        if value not in allowed:
            raise ValueError("la prioridad debe ser low, medium, or high")
        return value
    @field_validator("title")
    def validate_title(cls, value):
        if not value or not value.strip():
            raise ValueError("el título no puede estar vacío")
        return value.strip()

class TaskUpdateStatus(BaseModel):
    done:bool

class TaskResponse(BaseModel):
    id: int
    title: str
    priority: str
    done: bool
    created_at: datetime

    class Config:
        from_attributes = True
# Endpoints
@app.get("/api/tasks", response_model=list[TaskResponse])
def get_tasks(done: Optional[bool] = Query(None), db: Session = Depends(get_db)):
    query = db.query(models.Task)
    if done is not None:
        query = query.filter(models.Task.done == done)
    tasks = query.order_by(models.Task.created_at.desc()).all()
    return tasks

@app.post("/api/tasks", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
def create_task(Task_data: TaskCreate, db: Session = Depends(get_db)):
    new_task = models.Task(
        title=Task_data.title,
        priority=Task_data.priority
    )
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

@app.patch("/api/tasks/{task_id}", response_model=TaskResponse)
def update_task_status(task_id: int, status_update: TaskUpdateStatus, db: Session = Depends(get_db)):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="tarea no encontrada")
    task.done = status_update.done
    db.commit()
    db.refresh(task)
    return task

@app.delete("/api/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="tarea no encontrada")
    db.delete(task)
    db.commit()
    return None