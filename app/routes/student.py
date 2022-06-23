
from fastapi import APIRouter, HTTPException, Body, Depends
from ..dbquery import *
from ..models.registerModel import *
from ..auth import auth_hundler, auth_bearer

router = APIRouter(tags=["Students"], prefix="/student")
@router.post("/add_student",dependencies=[Depends(auth_bearer.JWTBearer())])
async def add_student(student: registerSchema= Body(...)):
    add_student = await create_student(student)
    return {"Message": "Added Student successfully"}

@router.get("/studentList")
async def all_students():
    all_student = await list_students()
    return {"List": all_student}

@router.get("/{name}")
async def get_student(student_name):
    student = await select_one_student(student_name)
    if not student:
        raise HTTPException(status_code = 404, detail = "Student Not found")
    return {"List": student}


@router.put("/update/{id_number}")
async def student_update(id_number:int,payload:registerSchema):
    student = await select_one_student(id_number)
    if student:
        await update_student(id_number,payload)
        return {"Message": "Updated successfully"}
    raise HTTPException(status_code = 404, detail = "Student Not found")

@router.delete("/delete/{id_number}")
async def student_delete(id_number:int):
    student = await select_one_student(id_number)
    if  student:
        await delete_student(id_number)
        return {"Message": "Deleted successfully"}
    raise HTTPException(status_code = 404, detail = "Student Not found")