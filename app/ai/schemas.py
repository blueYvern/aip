from pydantic import BaseModel


class AiAnalyzeRequest(BaseModel):
    question: str


class AiAnalyzeResponse(BaseModel):
    question: str
    answer: str
