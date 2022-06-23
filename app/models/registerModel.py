from pydantic import BaseModel, EmailStr, Field

class registerSchema(BaseModel):
    first_name : str = Field(...)
    last_name : str= Field(...)
    email : EmailStr = Field(...)
    id_number: int = Field(..., gt=0, lt=9)
    course : str = Field(...)
    year :int= Field(..., gt=0, lt=9)
    