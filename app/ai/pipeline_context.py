from app.ai.context import ContextProvider
from app.db import SessionLocal
from app.models import Pipeline


class PipelineContextProvider(ContextProvider):

    def __init__(
            self, limit: int = 5):
        self.limit = limit

    def get_context(self):
        db = SessionLocal()      
        try:
            pipelines = (
                db.query(Pipeline)
                  .order_by(Pipeline.id.desc())
                  .limit(self.limit)
                  .all()
                )
            return {
                "recent_pipelines":
                [
                    {
                        "name": p.name,
                        "status": p.status
                    }
                    for p in pipelines
                ]
            }
        finally:
            db.close()
            

