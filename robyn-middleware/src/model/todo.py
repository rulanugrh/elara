from sqlalchemy import Column, Integer, String, Time
from config.config import Base

class Todo(Base):
    __tablename__ = "todos"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    desc = Column(String)
    time = Column(Time)
    