from sqlalchemy import Column, Integer, String
from app.db import Base


class Pipeline(Base):
    __tablename__ = "pipeline"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    status = Column(String)
