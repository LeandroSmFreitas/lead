from sqlalchemy import Column, Integer, DateTime, String
from dataclasses import dataclass

from app.configs.database import db


@dataclass
class LeadsModel(db.Model):
    name: str
    email: str
    phone: str
    creation_date: str
    last_visit: str
    visits: int

    __tablename__ = "leads"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    phone = Column(String, unique=True, nullable=False)
    creation_date = Column(DateTime, nullable=False)
    last_visit = Column(DateTime, nullable=True)
    visits = Column(Integer, nullable=True, default=1)
