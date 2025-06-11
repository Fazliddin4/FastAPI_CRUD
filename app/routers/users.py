from fastapi import Response, HTTPException, APIRouter
from app.fake_db import users
from app.schemas import UserIn, UserOut
router=APIRouter(
    prefix="/users",
    tags=["users"]
)


@router.get("/")
async def get_users():
    return users
 

@router.get("/{user_id}")
async def get_user(user_id: int):
    res_user: dict = None
    for user in users:
        if user["id"]==user_id:
            res_user=user
            break
    if not res_user:
        raise HTTPException( status_code=404)
    
    return res_user

@router.post("/create/", response_model=UserOut)
async def create_user(user: UserIn):
    res_user=user.model_dump()
    res_user.update({"id": len(users)+1})
    users.append(user.model_dump())
    return res_user

 

@router.put("/{user_id}/update", response_model=UserOut)
async def update_user(user_id: int, user_in: UserIn):
    res_user: dict=None

    for user in users:
        if user["id"]==user_id:
            res_user=user
            break

    if not res_user:
        raise HTTPException(detail={"message": "user not found"}, status_code=404)
    res_user.update(user_in.model_dump())
    return res_user



@router.delete("/{user_id}/delete")
async def delete_user(user_id: int):
    for user in users:
        if user["id"]==user_id:
            users.remove(user)
            return Response(status_code=204)
        else:
             return HTTPException(detail="user notfound", status_code=404)