from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

SQLALCHEMY_DATABASE_URL = "sqlite:///ecommerce.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    print("Starting init_db...")
    print("Registered tables:", Base.metadata.tables.keys())
    Base.metadata.create_all(bind=engine, checkfirst=True)
    print("Finished init_db. Tables created:", Base.metadata.tables.keys())