# app/utils/image_utils.py
import os
from fastapi import UploadFile

UPLOAD_DIR = os.path.join(os.getcwd(), "uploads")
os.makedirs(UPLOAD_DIR, exist_ok=True)

def save_upload_file(upload_file: UploadFile, destination: str = None) -> str:
    if destination is None:
        destination = os.path.join(UPLOAD_DIR, upload_file.filename)
    with open(destination, "wb") as buffer:
        buffer.write(upload_file.file.read())
    return destination
