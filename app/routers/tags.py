from fastapi import Response, HTTPException, APIRouter

from app.models import Tag
from app.schemas import TagIn, TagOut,  TagInUpdate
from app.dependencies import db_dependency

tag=APIRouter(
    prefix="/tags",
    tags=["tags"]
)

@tag.get("/read/", response_model=list[TagOut])
async def get_tag(db: db_dependency):
    tag=db.query(Tag).all()
    return tag

@tag.get("/read/{tag_id}/", response_model=TagOut)
async def get_tags(db: db_dependency, tag_id: int):
    found_tag=db.query(Tag).filter(Tag.id==tag_id).first()
    if not found_tag:
        raise HTTPException(status_code=404, detail="tag not found")
    return found_tag

@tag.post("/create/", response_model=TagOut)
async def create_tag(db: db_dependency, tag: TagIn):
    new_tag=Tag(**tag.model_dump())
    db.add(new_tag)
    db.commit()
    db.refresh(new_tag)
    return new_tag

@tag.put("/update/{tag_id}/", response_model=TagOut)
async def update_tag(db: db_dependency, tag_id: int, tag_in: TagInUpdate):
    found_tag=db.query(Tag).filter(Tag.id==tag_id).first()
    if not found_tag:
        raise HTTPException(detail="tag not found", status_code=404)
    found_tag.name=tag_in.name if tag_in.name else found_tag.name

    db.commit()
    db.refresh(found_tag)
    
    res_tag=db.query(Tag).filter(Tag.id==tag_id).first()
    return res_tag


@tag.delete("/delete/{tag_id}/", response_model=TagOut)
async def delete_tag(db: db_dependency, tag_id: int ):
     found_tag=db.query(Tag).filter(Tag.id==tag_id).first()
     if found_tag:
         db.delete(found_tag)
         db.commit()
         return Response(status_code=204)
     return HTTPException(detail="tag not found", status_code=404)