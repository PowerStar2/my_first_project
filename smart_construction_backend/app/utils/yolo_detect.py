# app/utils/yolo_detect.py
import os, json

def detect_image(path: str):
    """
    Try to use ultralytics if installed; otherwise return a dummy result.
    Return: dict { "result": "smoke"|"fire"|"none", "confidence": "0.87" }
    """
    try:
        from ultralytics import YOLO
        model = YOLO("yolov8n.pt")  # adjust model path if you have a custom model
        res = model(path)[0]
        # rudimentary: check classes names for fire or smoke (depends on your trained model)
        labels = [x.names.get(int(int(box.cls))) if hasattr(box, 'cls') else None for box in [res.boxes]]
        # simpler approach: derive from res.boxes.cls if available
        # We'll instead produce a simple summary:
        if len(res.boxes) > 0:
            # pick top box
            conf = float(res.boxes.conf[0]) if hasattr(res.boxes, "conf") else 0.0
            # model-specific class mapping needed; fallback to "fire"
            return {"result": "fire", "confidence": f"{conf:.2f}"}
        return {"result": "none", "confidence": "0.00"}
    except Exception:
        # fallback: mock detection
        return {"result": "smoke", "confidence": "0.75"}
