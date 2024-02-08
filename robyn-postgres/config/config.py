import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

class Config:
    DB_PASS: str
    DB_HOST: str
    DB_USER: str
    DB_PORT: str
    DB_NAME: str

    APP_HOST: str
    APP_PORT: str

app = Config

Base = declarative_base()

def GetConnection():
    conf = GetConfig()
    SQLALCHEMY_DATABASE_URL = f"postgresql://{conf.DB_USER}:{conf.DB_PASS}@{conf.DB_HOST}:{conf.DB_PORT}/{conf.DB_NAME}"
    engine = create_engine(SQLALCHEMY_DATABASE_URL)

    SessionLocal = sessionmaker(autocommit=false, autoflush=false, bind=engine)
    base = declarative_base()
    Base = base
    
    return SessionLocal

def GetConfig() -> Config:
    if app == "":
        app = initConfig()
    
    return app

def initConfig() -> Config:
    conf = Config
    conf.APP_HOST = os.getenv("APP_HOST")
    conf.APP_PORT = os.getenv("APP_PORT")

    conf.DB_HOST = os.getenv("DB_HOST")
    conf.DB_NAME = os.getenv("DB_NAME")
    conf.DB_PASS = os.getenv("DB_PASS")
    conf.DB_USER = os.getenv("DB_USER")
    conf.DB_PORT = os.getenv("DB_PORT")

    return conf