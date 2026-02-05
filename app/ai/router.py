from fastapi import APIRouter
from app.ai.schemas import AiAnalyzeRequest, AiAnalyzeResponse
from app.ai.pipeline_context import PipelineContextProvider
from app.ai.orchestrator import AiOrchestrator

router = APIRouter(prefix="/ai", tags=["ai"])


@router.post("/analyze", response_model=AiAnalyzeResponse)
def analyze(request: AiAnalyzeRequest):
    providers = PipelineContextProvider(limit=5)
    orch = AiOrchestrator(context_providers=[providers], tools=[])

    return orch.analyze(question=request.question)
