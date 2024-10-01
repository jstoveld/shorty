from sqlalchemy import Column, Integer, String
from .db import Base

class Url(Base):
    __tablename__ = "urls"

    id = Column(Integer, primary_key=True, index=True)
    original_url = Column(String, index=True)
    shortened_url = Column(String, index=True)