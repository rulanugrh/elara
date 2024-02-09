from sqlalchemy import Column, Integer, String, Boolean
from config.config import *

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    name = Column(String)
    password = Column(String)

    def __repr__(self):
        return "<User(id={id}, email={email}, name={name}, password={password})>".format(
            id = self.id,
            email = self.email,
            name = self.name,
            password = self.password,
        )