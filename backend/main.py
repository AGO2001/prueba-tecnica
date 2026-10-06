# backend/main.py
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from pydantic import BaseModel

# Imports absolutos
from backend.database import engine, Base, get_db
from backend import models

# Crear las tablas en PostgreSQL automáticamente
Base.metadata.create_all(bind=engine)

app = FastAPI(title="API de Prueba Técnica")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Esquemas Pydantic
class ItemCreate(BaseModel):
    nombre: str
    descripcion: str
    precio: float

class ItemResponse(ItemCreate):
    id: int

    class Config:
        from_attributes = True

# Endpoints
@app.get("/api/items", response_model=list[ItemResponse])
def get_items(db: Session = Depends(get_db)):
    return db.query(models.Item).all()

@app.post("/api/items", response_model=ItemResponse, status_code=status.HTTP_201_CREATED)
def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    db_item = models.Item(**item.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item