from .db import users, database
from .models import usersModel
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto") # used to hash passwords

async def create_user(payload):
    hash_password=pwd_context.hash(payload.password)
    query =  users.insert().values(fullname = payload.fullname, email= payload.email, password = hash_password)
    return await database.execute(query=query)

async def check_user(user:usersModel.UserloginShema):
    
    query = users.select().where(user.email == users.c.email)
    selected_user =database.fetch_one(query=query)
    verify_password=pwd_context.verify(user.plain_password, selected_user.password)
    if selected_user.email == user.email and  verify_password==True:
        return True
    return False    