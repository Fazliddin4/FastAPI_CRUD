from pydantic import BaseModel, Field

class UserIn(BaseModel):
    username: str
    password: str=Field(min_length=8, max_length=16)

class UserOut(BaseModel):
    id: int
    username: str
    password: str=Field(min_length=8, max_length=16)

class CarIn(BaseModel):
    name: str
    brand: str
    published_year: str

class CarOut(BaseModel):
    id: int
    name: str
    brand: str
    published_year: str

class ProductIn(BaseModel):
    name: str
    price: str

class ProductOut(BaseModel):
    id: int
    name: str
    price: str