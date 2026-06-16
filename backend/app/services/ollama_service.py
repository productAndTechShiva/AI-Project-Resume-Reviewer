"""
ollama_service.py

Responsible for communicating
with the local Ollama server.

Flow:

Prompt
   ↓
Ollama API
   ↓
Llama3
   ↓
Response
"""

import requests


class OllamaService:

    OLLAMA_URL = "http://localhost:11434/api/generate"

    MODEL_NAME = "llama3"

    @staticmethod
    def generate(
        prompt: str
    ) -> str:
        """
        Send prompt to Llama3.

        Parameters:
            prompt (str)

        Returns:
            str
        """

        try:

            payload = {
                "model": OllamaService.MODEL_NAME,
                "prompt": prompt,
                "stream": False
            }

            response = requests.post(
                OllamaService.OLLAMA_URL,
                json=payload,
                timeout=300
            )

            response.raise_for_status()

            data = response.json()

            return data.get(
                "response",
                ""
            )

        except requests.exceptions.ConnectionError:

            raise Exception(
                "Could not connect to Ollama. Is Ollama running?"
            )

        except requests.exceptions.Timeout:

            raise Exception(
                "Ollama request timed out."
            )

        except Exception as e:

            raise Exception(
                f"Ollama Error: {str(e)}"
            )