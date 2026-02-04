from app.routers import health, pipeline
from app.db import engine, Base
from fastapi import FastAPI

Base.metadata.create_all(bind=engine)

app = FastAPI(title="AIP Demo application")
app.include_router(health.router)
app.include_router(pipeline.router)
