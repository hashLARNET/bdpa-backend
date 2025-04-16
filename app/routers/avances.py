from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from pydantic import BaseModel
from app.database import SessionLocal
from app.models.avance import Avance

router = APIRouter()

class AvanceCreate(BaseModel):
    obra: str
    piso: int
    departamento: str
    avances: List[str]
    observaciones: str = ""

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=dict)
def registrar_avance(avance: AvanceCreate, db: Session = Depends(get_db)):
    nuevo = Avance(
        obra=avance.obra,
        piso=avance.piso,
        departamento=avance.departamento,
        avances=",".join(avance.avances),
        observaciones=avance.observaciones
    )
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return {"mensaje": "Avance guardado", "id": nuevo.id}
