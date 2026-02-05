from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db import SessionLocal
from app.models import Pipeline
from app.schemas import PipelineResponse


router = APIRouter(prefix="/pipelines", tags=["pipelines"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=PipelineResponse)
def create_pipeline(name: str, status: str, db: Session = Depends(get_db)):
    pipeline = Pipeline(name=name, status=status)
    db.add(pipeline)
    db.commit()
    db.refresh(pipeline)
    return pipeline


@router.get("/", response_model=list[PipelineResponse])
def get_list_pipelines(db: Session = Depends(get_db)):
    return db.query(Pipeline).all()
