from fastapi import Response, HTTPException, APIRouter

from app.models import Book, Category
from app.schemas import BookIn, BookOut,  BookInUpdate
from app.dependencies import db_dependency


book=APIRouter(
    prefix="/books",
    tags=["books"]
)

@book.get("/read/", response_model=list[BookOut])
async def get_book(db: db_dependency):
    book=db.query(Book).all()
    return book

@book.get("/read/{book_id}/", response_model=BookOut)
async def get_books(db: db_dependency, book_id: int):
    found_book=db.query(Book).filter(Book.id==book_id).first()

    if not found_book:
        raise HTTPException(
            status_code=404,
            detail="book not found"   
        )
    return found_book

@book.post("/create/", response_model=BookOut)
async def create_book(db: db_dependency, book: BookIn):

    if db.query(Book).filter(Book.title == book.title).first():
        raise HTTPException(
            status_code=400,
            detail = "Book with this title already exist"
        )
    
    if not db.query(Category).filter(Category.id==book.category_id).first():
        raise HTTPException(
            status_code=404,
            detail="category not found"
        )

    new_book=Book(**book.model_dump())
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book

@book.put("/update/{book_id}/", response_model=BookOut)
async def update_book(db: db_dependency, book_id: int, book_in: BookInUpdate):
    found_book=db.query(Book).filter(Book.id==book_id).first()
    if not found_book:
        raise HTTPException(detail="book not found", status_code=404)
    
    if db.query(Book).filter(Book.title == book.title).first():
        raise HTTPException(
            status_code=400,
            detail = "Book with this title already exist"
        )
    
    found_book.title=book_in.title if book_in.title else found_book.title
    found_book.description=book_in.description if book_in.description else found_book.description
    found_book.category_id=book_in.category_id if book_in.category_id else found_book.category_id

    db.commit()
    db.refresh(found_book)
    
    return found_book


@book.delete("/delete/{book_id}/", response_model=BookOut)
async def delete_book(db: db_dependency, book_id: int ):
    found_book=db.query(Book).filter(Book.id==book_id).first()
    if found_book:
        db.delete(found_book)
        db.commit()
        return Response(status_code=204)
    return HTTPException(detail="book not found", status_code=404)

