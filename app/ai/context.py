from abc import ABC, abstractmethod
from typing import Dict, Any


class ContextProvider(ABC):

    @abstractmethod
    def get_context(self) -> Dict[str, Any]:
        pass
