# app/main.py
from fastapi import FastAPI
from app.database import engine, Base
from app import models  # ensure models are imported so metadata has tables
from app.routers import user_router, upload_router, fire_router, alert_router

# create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Smart Construction Backend")

app.include_router(user_router.router, prefix="/users", tags=["users"])
app.include_router(upload_router.router, prefix="/upload", tags=["upload"])
app.include_router(fire_router.router, prefix="/fire", tags=["fire_detection"])
app.include_router(alert_router.router, prefix="/alert", tags=["alert"])

@app.get("/")
def root():
    return {"message": "Smart Construction Backend running"}
