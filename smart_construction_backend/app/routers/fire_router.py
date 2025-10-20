# app/routers/fire_router.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app import crud, schemas

router = APIRouter()

@router.get("/records/{user_id}", response_model=list[schemas.FireDetectionOut])
def get_records(user_id: int, db: Session = Depends(get_db)):
    items = crud.get_fire_detections_by_user(db, user_id)
    if items is None:
        raise HTTPException(status_code=404, detail="no records")
    return items
