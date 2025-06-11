from fastapi import Response, HTTPException, APIRouter
from app.fake_db import cars
from app.schemas import CarIn, CarOut

router=APIRouter(
    prefix="/cars",
    tags=["cars"]
)
@router.get("/")
async def get_cars():
    return cars

@router.get("/{car_id}")
async def get_car(car_id: int):
    res_car: dict = None
    for car in cars:
        if car["id"]==car_id:
            res_car=car
            break
    if not res_car:
        raise HTTPException( status_code=404)
    
    return res_car

@router.post("/create/", response_model=CarOut)
async def create_car(car: CarIn):
    res_car=car.model_dump()
    res_car.update({"id": len(cars)+1})
    cars.append(car.model_dump())
    return res_car

@router.put("/{car_id}/update", response_model=CarOut)
async def update_car(car_id: int, car_in: CarIn):
    res_car: dict=None

    for car in cars:
        if car["id"]==car_id:
            res_car=car
            break

    if not res_car:
        raise HTTPException(detail={"message": "car not found"}, status_code=404)
    res_car.update(car_in.model_dump())
    return res_car



@router.delete("/{car_id}/delete")
async def delete_car(car_id: int):
    for car in cars:    
        if car["id"]==car_id:
            cars.remove(car)
            return Response(status_code=204)
        else:
             return HTTPException(detail="car not found", status_code=404)
