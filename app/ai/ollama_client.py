import requests


class OllamaClient:
    def __init__(self, base_url="http://localhost:11434"):
        self.base_url = base_url

    def generate(self, model: str, prompt: str) -> str:
        response = requests.post(
            f"{self.base_url}/api/generate",
            json={"model": model,
                  "prompt": prompt,
                  "stream": False},
            timeout=600
        )
        response.raise_for_status()
        return response.json()["response"]
    