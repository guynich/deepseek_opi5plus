"""Script for chatting with history using distilled version of DeepSeek R1 model."""

from ollama import chat

MODEL = "deepseek-r1:1.5b"
# Some of these prompts require history to generate a response.
PROMPTS = [
    "What is the sum of 3 + 2?",
    "What is the result if +1 is added to both numbers before summing them?",
    "What is the capital of France?",
    "Describe an historical event from the 18th century in that city.",
]


class OllamaChat:
    """A chat interface with history for Ollama large language models."""

    def __init__(self, model: str):
        self.model = model
        self.messages = []

    def __call__(self, prompt):
        self.messages.append({"role": "user", "content": prompt})

        response = chat(model=self.model, messages=self.messages)

        self.messages.append({"role": "assistant", "content": response.message.content})
        return response.message.content


if __name__ == "__main__":
    deepseek_chat = OllamaChat(model=MODEL)

    for prompt in PROMPTS:
        try:
            print(f"User:  {prompt}\nRunning model ...")
            print(f"Assistant:\n{deepseek_chat(prompt)}\n")
        except Exception as e:
            print(f"An error occurred: {e}")
        except KeyboardInterrupt:
            print("\nUser quit.")
            break
