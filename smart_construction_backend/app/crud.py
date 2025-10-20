# app/crud.py
from sqlalchemy.orm import Session
from . import models
from .utils.hash import hash_password

def create_user(db: Session, username: str, email: str, password: str):
    hashed = hash_password(password)
    user = models.User(username=username, email=email, hashed_password=hashed)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def create_fire_detection(db: Session, image_path: str, result: str, confidence: str, user_id: int):
    item = models.FireDetection(image_path=image_path, result=result, confidence=confidence, user_id=user_id)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item

def get_fire_detections_by_user(db: Session, user_id: int):
    return db.query(models.FireDetection).filter(models.FireDetection.user_id == user_id).order_by(models.FireDetection.detected_at.desc()).all()
