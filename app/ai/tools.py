from abc import ABC, abstractmethod
from typing import Dict, Any


class Tool(ABC):

    @abstractmethod
    def execute(self, params: Dict[str, Any]) -> Any:
        pass
