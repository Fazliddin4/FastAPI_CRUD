from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
import os



DB_NAME=os.getenv("DB_NAME")
DB_USER=os.getenv("DB_USER")
DB_PASSWORD=os.getenv("DB_PASSWORD")
DB_HOST=os.getenv("DB_HOST")
DB_PORT=os.getenv("DB_PORT")
DB_URL=f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine=create_engine(DB_URL, echo=True)
sessionLocal=sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass

def get_db():
    db=sessionLocal()
    try:
        yield db
    finally:
        db.close()

