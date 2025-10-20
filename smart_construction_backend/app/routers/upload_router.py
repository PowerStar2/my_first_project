# app/routers/upload_router.py
from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.utils.image_utils import save_upload_file
from app.utils.yolo_detect import detect_image
from app import crud, schemas
from app.utils.notification import send_wechat_text
import json

router = APIRouter()

@router.post("/file", response_model=schemas.FireDetectionOut)
async def upload_file(user_id: int, file: UploadFile = File(...), db: Session = Depends(get_db)):
    # 1. save file
    file_path = save_upload_file(file)
    # 2. detect
    res = detect_image(file_path)
    result_str = json.dumps(res)
    confidence = res.get("confidence")
    # 3. persist
    detection = crud.create_fire_detection(db, image_path=file_path, result=result_str, confidence=str(confidence), user_id=user_id)
    # 4. notify if fire
    if res.get("result") == "fire":
        msg = f"火情报警！用户 {user_id} 检测到 fire，置信度 {confidence}，文件：{file_path}"
        send_wechat_text(msg)
    return detection
