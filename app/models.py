from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship
from datetime import datetime

from app.database import Base




class Category(Base):
    __tablename__="categories"

    id: Mapped[int]=mapped_column(Integer, primary_key=True)
    name: Mapped[str]=mapped_column(String(50), nullable=False, unique=True)

    books = relationship("Book", back_populates="category")

class Book(Base):
    __tablename__="books"

    id: Mapped[int]=mapped_column(Integer, primary_key=True)
    title: Mapped[str]=mapped_column(String(100), unique=True, nullable=False)
    description: Mapped[str]=mapped_column(String(100), nullable=False)
    category_id: Mapped[int]=mapped_column(Integer, ForeignKey("categories.id"))
    
    category = relationship("Category", back_populates="books")
    tags: Mapped[list["BookTag"]]=relationship(back_populates="books")

class Tag(Base):
    __tablename__ = "tags"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, unique=True, nullable=False)

    books: Mapped[list["BookTag"]]=relationship(back_populates="tags")



class BookTag(Base):
    __tablename__ = "book_tags"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    book_id: Mapped[int] = mapped_column(Integer, ForeignKey("books.id"))
    tag_id: Mapped[int] = mapped_column(Integer, ForeignKey("tags.id"))

    books: Mapped["Book"] = relationship(back_populates="tags")
    tags: Mapped["Tag"]=relationship(back_populates="books")

