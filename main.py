from fastapi import FastAPI, Response, Depends, HTTPException                       
from app.dependencies import db_dependency
from app.routers import book, category, tags
from app.models import Book, Tag, BookTag
from app.routers.tags import tag
from app.routers.book import book as b
from app.routers.category import category as c

app=FastAPI(
    docs_url="/",
)



@app.get("/")
async def root():
    return {"massage" : "Hello World"}

app.include_router(c)
app.include_router(b)
app.include_router(tag)




@app.post("/bind_tag_to_book/")
async def bind_tag_to_book(db: db_dependency, tag_id: int, book_id: int):
    found_tag=db.query(Tag).filter(Tag.id==tag_id).first()

    if not found_tag:
        raise HTTPException(detail="tag not found", status_code=404)
    found_book=db.query(Book).filter(Book.id==book_id).first()

    if not found_book:
        raise HTTPException(detail="book not found", status_code=404)
    
    if db.query(BookTag).filter(BookTag.book_id==book_id and BookTag.tag_id==tag_id):
        raise HTTPException(detail="this tag is already exists in this book", status_code=404)
    
    new_booktag=BookTag(tag_id=tag_id, book_id=book_id)
    db.add(new_booktag)
    db.commit()
    db.refresh(new_booktag)
    return new_booktag


