# app/utils/notification.py
import os, requests, json
from dotenv import load_dotenv
load_dotenv()

WECHAT_WEBHOOK = os.getenv("WECHAT_WEBHOOK")  # 必须在 .env 设置

def send_wechat_text(msg: str):
    if not WECHAT_WEBHOOK:
        print("[notify] WECHAT_WEBHOOK not configured, message:", msg)
        return False
    payload = {"msgtype": "text", "text": {"content": msg}}
    try:
        r = requests.post(WECHAT_WEBHOOK, json=payload, timeout=5)
        return r.status_code == 200 and r.json().get("errcode", 0) == 0
    except Exception as e:
        print("[notify] exception:", e)
        return False
