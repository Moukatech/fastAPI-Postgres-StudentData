
from .db import students, database
from .models.registerModel import registerSchema

async def create_student(payload:registerSchema):
    query = students.insert().values(first_name =payload.first_name, last_name=payload.last_name, email=payload.email,id_number=payload.id_number, year=payload.year)
    return await database.execute(query=query)

async def list_students():
    query = students.select()
    datas = await database.fetch_all(query = query)
    # studentlist =[]
    
    # for student in datas:
    #     studentlist.append(student)
    return datas

async def select_one_student(id_number):
    query = students.select().where(id_number == students.c.id_number)
    return await database.fetch_one(query=query)

async def update_student(id_number, payload:registerSchema):
    query = (students.update()
             .where(id_number == students.c.id_number)
             .values(first_name =payload.first_name, last_name=payload.last_name, email=payload.email,id_number=id_number, year=payload.year)
             ) 
    return await database.execute(query=query)

async def delete_student(id_number:int):
    query = (students.delete().where(id_number == students.c.id_number)) 
    return await database.execute(query=query)