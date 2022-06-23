
from fastapi import FastAPI 
from .db import metadata, database, engine
from .routes import student, users

metadata.create_all(engine)
app = FastAPI()
app.include_router(student.router)
app.include_router(users.router)


@app.on_event("startup")
async def db_connect():
    await database.connect()

@app.on_event("shutdown")
async def close_connection():\
    await database.disconnect()

@app.get("/", tags=["Home Page"])
async def homepage():
    return{"Message" : "Welcome We are awesome"}