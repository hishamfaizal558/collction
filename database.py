
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# ✅ Correct DATABASE_URL format
DATABASE_URL = "postgresql://collection_mkz6_user:nqYN9Ds0L3uds7DoYRcAC1kONzyKSfJW@dpg-d1p14ak9c44c73845kfg-a.oregon-postgres.render.com/collection_mkz6"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
