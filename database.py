from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

class Base(DeclarativeBase):
    pass

DATABASE_URL = ("mysql+pymysql://root:root@localhost:8889/clinique_vet")

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Test de connexion
with engine.connect() as connection:
    print("Successfully connected to database")
    print("="*100)