from pydantic import BaseModel, Field



class CategoryIn(BaseModel):
    name: str
class CategoryOut(BaseModel):
    id: int
    name: str
class CategoryInUpdate(BaseModel):
    name: str| None=None
class BookIn(BaseModel):
    title: str
    description: str
    category_id: int
class BookOut(BaseModel):
    id: int
    title: str
    description: str
    category: CategoryOut
class BookInUpdate(BaseModel):
    title: str| None = None
    description: str | None = None
    category_id: int | None = None
class TagIn(BaseModel):
    name: str
class TagOut(BaseModel):
    id: int
    name: str
class TagInUpdate(BaseModel):
    name: str | None = None    

