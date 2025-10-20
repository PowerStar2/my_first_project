# app/routers/user_router.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import timedelta
from app import crud, schemas, auth
from app.database import get_db

router = APIRouter()

@router.post("/register", response_model=schemas.UserOut)
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    if crud.get_user_by_username(db, user.username):
        raise HTTPException(status_code=400, detail="username exists")
    if crud.get_user_by_email(db, user.email):
        raise HTTPException(status_code=400, detail="email exists")
    created = crud.create_user(db, user.username, user.email, user.password)
    return created

@router.post("/login", response_model=schemas.Token)
def login(form: schemas.UserLogin, db: Session = Depends(get_db)):
    user = crud.get_user_by_username(db, form.username)
    if not user:
        raise HTTPException(status_code=401, detail="bad credentials")
    from app.utils.hash import verify_password
    if not verify_password(form.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="bad credentials")
    token = auth.create_access_token(subject=user.username, expires_delta=timedelta(minutes=60))
    return {"access_token": token, "token_type": "bearer"}

@router.get("/me", response_model=schemas.UserOut)
def me(current_user = Depends(auth.get_current_user)):
    return current_user
