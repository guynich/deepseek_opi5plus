"""Script for contextual chatting with the DeepSeek R1 model."""

from typing import List

import ollama

MODEL = "deepseek-r1:1.5b"
# Some of these prompt examples assume context is maintained.
PROMPTS = [
    "What is the sum of 3 + 2?",
    "What is the result if +1 is added to both numbers before summing them?",
    "What is the capital of France?",
    "Describe briefly a historical event from that city.",
]


class DeepSeekChat:
    def __init__(self, model: str):
        self.model = model
        self.messages = []

    def __call__(self, prompt_text):
        self.messages.append({"role": "user", "content": prompt_text})

        response = ollama.chat(model=self.model, messages=self.messages)
        self.messages.append(
            {"role": "assistant", "content": response["message"]["content"]}
        )

        return response["message"]["content"]


def main(prompts: List[str]) -> None:
    chat = DeepSeekChat(model=MODEL)
    for prompt in prompts:
        try:
            print(f"User:  {prompt}")
            print(f"Assistant:\n{chat(prompt)}\n")
        except Exception as e:
            print(f"An error occurred: {e}")
        except KeyboardInterrupt:
            print("User quit.")
            break


if __name__ == "__main__":
    main(PROMPTS)
