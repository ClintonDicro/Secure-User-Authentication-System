from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from __init__ import get_db
from schemas.user import UserCreate, LoginRequest
from models.user import User
from utils.security import hash_password, verify_password, create_access_token, get_current_user

router = APIRouter()

@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.username == user.username).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already exists")
    db_user = User(username=user.username, hashed_password=hash_password(user.password))
    db.add(db_user)
    db.commit()
    return {"msg":"User register successfully"}

@router.post("/login")
def login(user: LoginRequest, db: Session=Depends(get_db)):
    db_user = db.query(User).filter(User.username==user.username).first()
    if not db_user or not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid username or password")
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer","msg":"Login successfully"}

@router.get("/profile")
def get_profile(current_user: dict = Depends(get_current_user)):
    return {"msg":f"Welcome {current_user['username']}!"}

