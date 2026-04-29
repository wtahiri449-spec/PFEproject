from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from pydantic import BaseModel
from .database import SessionLocal, init_db
from .models import User
from .security import hash_password, verify_password
from .auth_utils import create_access_token

router = APIRouter()

class UserCreate(BaseModel):
    apogee: str
    email: str
    password: str
    full_name: str
    is_prof: bool = False

class UserLogin(BaseModel):
    apogee: str
    password: str

@router.on_event("startup")
def on_startup():
    init_db()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    if db.query(User).filter((User.apogee == user.apogee) | (User.email == user.email)).first():
        raise HTTPException(status_code=400, detail="Apogee or email already registered")
    db_user = User(
        apogee=user.apogee,
        email=user.email,
        hashed_password=hash_password(user.password),
        full_name=user.full_name,
        is_prof=user.is_prof
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return {"msg": "User registered successfully"}

@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.apogee == user.apogee).first()
    if not db_user or not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    access_token = create_access_token({"sub": db_user.apogee, "is_prof": db_user.is_prof})
    return {"access_token": access_token, "token_type": "bearer", "is_prof": db_user.is_prof, "full_name": db_user.full_name}
