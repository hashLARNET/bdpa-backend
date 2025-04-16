from fastapi import FastAPI
from app.database import Base, engine
from app import models
from app.routers import avances

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="BDPA Backend",
    description="Base de Datos de Progreso Automatizado",
    version="1.0.0"
)

app.include_router(avances.router, prefix="/avances", tags=["Avances"])

@app.get("/")
def root():
    return {"mensaje": "Prueba de servidor prendido"}
