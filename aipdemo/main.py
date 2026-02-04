from aipdemo.routers import health
from fastapi import FastAPI


app = FastAPI(title="AIP Demo application")
app.include_router(health.router)
