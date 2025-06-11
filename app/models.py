from sqlalchemy import Integer, String
from sqlalchemy.orm import mapped_column, Mapped
from datetime import datetime

from app.database import Base



class User(Base):
    __tablename__="users"

    id: Mapped[int]=mapped_column(Integer, primary_key=True)
    username: Mapped[str]=mapped_column(String(50), unique=True)
    email: Mapped[str]=mapped_column(String(50), unique=True)
    password: Mapped[str]=mapped_column(String(50), nullable=False)
    created_at: Mapped[datetime]=mapped_column(default=datetime.utcnow)
    
class Car(Base):
    __tablename__="cars"
    id: Mapped[int]=mapped_column(Integer, primary_key=True)
    name: Mapped[str]=mapped_column(String(50),nullable=False)
    brand: Mapped[str]=mapped_column(String(50), nullable=False)
    published_year: Mapped[str]=mapped_column(String(50), nullable=False)

class Product(Base):
    __tablename__="product"
    id: Mapped[int]=mapped_column(Integer, primary_key=True)
    name: Mapped[str]=mapped_column(String(50),nullable=False)
    price: Mapped[str]=mapped_column(String(50), nullable=False)
    