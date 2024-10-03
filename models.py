from sqlalchemy import Column, Integer, String, DateTime
from db import Base
import datetime

class URL(Base):
    __tablename__ = "urls"

    id = Column(Integer, primary_key=True, index=True)
    original_url = Column(String(2048), index=True)
    shortened_url = Column(String(50), index=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
    access_count = Column(Integer, default=0)