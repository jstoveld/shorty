from sqlalchemy import Column, Integer, String
from db import Base

class URL(Base):
    __tablename__ = "urls"

    id = Column(Integer, primary_key=True, index=True)
    original_url = Column(String(2048), index=True)
    shortened_url = Column(String(50), index=True)
    access_count = Column(Integer, default=0)