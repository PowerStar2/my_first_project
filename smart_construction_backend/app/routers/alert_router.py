# app/routers/alert_router.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.utils.notification import send_wechat_text

router = APIRouter()

@router.post("/send")
def send_alert(message: str):
    ok = send_wechat_text(message)
    return {"ok": ok}
