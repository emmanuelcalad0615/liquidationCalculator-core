from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import get_db
from schemas.user_schema import UserOut, UserCreate, TokenResponse, LoginRequest, UserDelete
from services.user_service import create_user, login_user, delete_user

router = APIRouter(prefix = "/auth", tags = ["auth"])

@router.post("/singup", response_model = UserOut)
def sing_up(payload: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, payload)
   

@router.post("/login", response_model=TokenResponse)
def login(payload: LoginRequest, db: Session = Depends(get_db)):
    return login_user(db, payload.email, payload.password)

@router.delete("/{email}", response_model=UserOut)
def delete(email: str, db: Session = Depends(get_db)):
    return delete_user(db, email)
