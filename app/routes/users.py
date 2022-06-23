from fastapi import APIRouter, HTTPException, Body, Depends
from ..crud_users import *
from ..models import usersModel
from ..auth import auth_hundler, auth_bearer


router = APIRouter(tags=["Users"], prefix="/user")

@router.post("/add_user",dependencies=[Depends(auth_bearer.JWTBearer())])
async def add_new_user(userData: usersModel.UserSchema):
    add= await create_user(userData)
    return {"Message": "User added successfully"}

@router.post("/login")
async def user_login(user:usersModel.UserloginShema):
    if check_user(user):
        return auth_hundler.signJWT(user.email)
    return{
        "Error": "Wrong login credentials"
    }
