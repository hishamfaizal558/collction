# database.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "DATABASE_URL = "postgresql://collection_mkz6_user:nqYN9Ds0L3uds7DoYRcAC1kONzyKSfJW@dpg-d1p14ak9c44c73845kfg-a.oregon-postgres.render.com/collection_mkz6"
"  # or use PostgreSQL/MySQL

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
