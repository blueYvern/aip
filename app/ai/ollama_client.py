import requests
import os


class OllamaClient:
    def __init__(self, 
                 base_url=str(os.getenv("OLLAMA_URL")),
                 timeout=int(os.getenv("OLLAMA_TIMEOUT", 60))):
        self.base_url = base_url
        self.timeout = timeout

    def generate(self, model: str, prompt: str) -> str:
        response = requests.post(
            f"{self.base_url}/api/generate",
            json={"model": model,
                  "prompt": prompt,
                  "stream": False},
            timeout=self.timeout
        )
        response.raise_for_status()
        return response.json()["response"]

