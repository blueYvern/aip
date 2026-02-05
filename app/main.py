from app.routers import health, pipeline
from app.ai.router import router as ai_router
from app.db import engine, Base
from fastapi import FastAPI

Base.metadata.create_all(bind=engine)

app = FastAPI(title="AIP Demo application")
app.include_router(health.router)
app.include_router(pipeline.router)
app.include_router(ai_router)
