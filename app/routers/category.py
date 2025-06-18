from fastapi import Response, HTTPException, APIRouter

from app.models import Category
from app.schemas import CategoryIn, CategoryOut,  CategoryInUpdate
from app.dependencies import db_dependency

category=APIRouter(
    prefix="/categories",
    tags=["categories"]
)

@category.get("/read/", response_model=list[CategoryOut])
async def get_category(db: db_dependency):
    category=db.query(Category).all()

    return category

@category.get("/read/{category_id}/", response_model=CategoryOut)
async def get_category(db: db_dependency, category_id: int):
    found_category=db.query(Category).filter(Category.id==category_id).first()
    if not found_category:
        raise HTTPException(status_code=404, detail="category not found")
    return found_category 

@category.post("/create/", response_model=CategoryOut)
def create_category(db: db_dependency, category: CategoryIn):

    new_category=Category(**category.model_dump())
    db.add(new_category)
    db.commit()
    db.refresh(new_category)
    return new_category

@category.put("/update/{category_id}/", response_model=CategoryOut)
async def update_category(db: db_dependency, category_id: int, category_in: CategoryInUpdate):
    found_category=db.query(Category).filter(Category.id==category_id).first()

    if not found_category:
        raise HTTPException(detail="category not found", status_code=404)
    
    found_category.name=category_in.name if category_in.name else found_category.name
    db.commit()
    db.refresh(found_category)
    
    
    return found_category


@category.delete("/delete/{category_id}/", response_model=CategoryOut)
async def delete_category(db: db_dependency, category_id: int ):
     found_category=db.query(Category).filter(Category.id==category_id).first()
     if found_category:
         db.delete(found_category)
         db.commit()
         return Response(status_code=204)
     return HTTPException(detail="category not found", status_code=404)


