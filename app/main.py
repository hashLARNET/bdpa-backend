from fastapi import FastAPI
from app.database import Base, engine
from app import models
from app.routers import avances
from app.routers import avance_tipo
from app.routers import auth


Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="BDPA Backend",
    description="Base de Datos de Progreso Automatizado",
    version="1.0.0"
)

app.include_router(auth.router, prefix="/auth", tags=["Autenticación"])
app.include_router(avances.router, prefix="/avances", tags=["Avances"])
app.include_router(avance_tipo.router, prefix="/avances-tipo", tags=["Avances Tipo"])

@app.get("/")
def root():
    return {"mensaje": "Prueba de servidor prendido"}