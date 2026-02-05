from pydantic import BaseModel


class PipelineCreate(BaseModel):
    name: str
    status: str


class PipelineResponse(BaseModel):
    id: int
    name: str
    status: str

    class Config:
        from_attributes = True
