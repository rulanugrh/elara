import os
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

class Config:
    APP_HOST: str
    APP_PORT: str
    APP_SECRET: str

    DB_NAME: str
    DB_HOST: str
    DB_PORT: str
    DB_USER: str
    DB_PASS: str

app = Config()
Base = declarative_base()

def GetConnection():
    conf = GetConfig()
    SQLALCHENY_DATABASE_URL = f"postgresql://{conf.DB_USER}:{conf.DB_PASS}@{conf.DB_HOST}:{conf.DB_PORT}/{conf.DB_NAME}"
    engine = create_engine(SQLALCHENY_DATABASE_URL)

    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    base = declarative_base()
    Base = base

    return SessionLocal
    
def GetConfig() -> Config:
    if app is None:
        app = initConfig()
    
    return app

def initConfig() -> Config:
    conf = Config()
    conf.APP_HOST = os.getenv("APP_HOST")
    conf.APP_PORT = os.getenv("APP_PORT")
    conf.APP_SECRET = os.getenv("APP_SECRET")

    conf.DB_HOST = os.getenv("DB_HOST")
    conf.DB_PORT = os.getenv("DB_PORT")
    conf.DB_USER = os.getenv("DB_USER")
    conf.DB_PASS = os.getenv("DB_PASS")
    conf.DB_NAME = os.getenv("DB_NAME")
