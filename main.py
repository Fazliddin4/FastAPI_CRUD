from fastapi import FastAPI, Response, Depends, HTTPException                       
from app.fake_db import users
from app.schemas import UserIn, UserOut

from app.routers.users import router as user_router
from app.routers.cars import router as car_router
from app.routers.products import router as product_router
app=FastAPI()



@app.get("/")
async def root():
    return {"massage" : "Hello World"}

app.include_router(user_router)
app.include_router(car_router)
app.include_router(product_router)
