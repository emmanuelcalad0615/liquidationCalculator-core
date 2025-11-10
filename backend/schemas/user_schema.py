from pydantic import BaseModel, EmailStr
from schemas.empleado_schema import EmpleadoCreate 
from schemas.empleado_schema import EmpleadoOut

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str
    empleado: EmpleadoCreate

class UserOut(BaseModel):
    id: int
    username: str
    email: str
    empleado: EmpleadoOut
    class Config:
        orm_mode = True
class LoginRequest(BaseModel):
    email: EmailStr
    password: str

class UserDelete(BaseModel):
    email: EmailStr

class TokenResponse(BaseModel):
    id: int
    access_token: str
    token_type: str 
    username: str 
    email: str
    

