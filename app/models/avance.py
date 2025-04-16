from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime
from app.database import Base

class Avance(Base):
    __tablename__ = "avances"

    id = Column(Integer, primary_key=True, index=True)
    obra = Column(String)
    piso = Column(Integer)
    departamento = Column(String)
    avances = Column(Text)
    observaciones = Column(Text)
    fecha = Column(DateTime, default=datetime.utcnow)
