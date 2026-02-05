from typing import List
from app.ai.context import ContextProvider
from app.ai.tools import Tool
from app.ai.ollama_client import OllamaClient
import json


class AiOrchestrator:

    def __init__(self,
                 context_providers: List[ContextProvider],
                 tools: List[Tool]):
        self.context_providers = context_providers
        self.tools = tools
        self.llm = OllamaClient()

    def build_context(self):
        context = {}
        for provider in self.context_providers:
            context.update(provider.get_context())
        return context

    def analyze(self, question: str):
        context = self.build_context()

        prompt = f""" 
        You are an AI agent analysing given json dumps. 

        Context:
        {json.dumps(context, indent=2)}

        Question:
        {question}

        Give short concise and clear answers only.
        """

        answer = self.llm.generate(
                            model="llama3",
                            prompt=prompt)

        return {
            "question": question,
            "context": context,
            "answer": answer,
        }
