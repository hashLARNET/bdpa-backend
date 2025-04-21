from sqlalchemy import Column, Integer, String
from app.database import Base

class AvanceTipo(Base):
    __tablename__ = "avance_tipos"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    obra = Column(String, nullable=False)
