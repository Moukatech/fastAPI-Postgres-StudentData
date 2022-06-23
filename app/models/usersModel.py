
from pydantic import BaseModel, EmailStr, Field

class UserSchema(BaseModel):
    fullname: str = Field(...)
    email : EmailStr =Field(...)
    password : str = Field(...)
    
class UserloginShema(BaseModel):
    email : EmailStr =Field(...)
    password : str = Field(...)