"""Script for chatting with history using distilled DeepSeek-R1 model."""

from ollama import chat

MODEL = "deepseek-r1:1.5b"
PROMPTS = [
    "What is the sum of 3 + 2?",
    "What is the result if +1 is added to both numbers before summing them?",
    "What is the capital city of France?",
    "Describe an historical event from the 18th century in that city.",
]


class OllamaChat:
    """A chat interface with history for Ollama large language models."""

    def __init__(self, model: str):
        self.model = model
        self.messages = []
        self.eval_counts = []
        self.total_duration_secs = []

    def __call__(self, prompt: str) -> None:
        self.messages.append({"role": "user", "content": prompt})

        content = ""
        for part in chat(model=self.model, messages=self.messages, stream=True):
            print(part["message"]["content"], end="", flush=True)
            content += part["message"]["content"]

        self.messages.append({"role": "assistant", "content": content})

        self.eval_counts.append(part.eval_count)
        self.total_duration_secs.append(part.total_duration / 1e9)

    def get_tokens_per_second(self) -> float:
        if len(self.eval_counts) > 0:
            return self.eval_counts[-1] / self.total_duration_secs[-1]
        return 0.0

    def get_average_tokens_per_second(self) -> float:
        if len(self.eval_counts) > 0:
            return sum(self.eval_counts) / sum(self.total_duration_secs)
        return 0.0

    def print_rate(self) -> None:
        print(f"""
Rate:          {self.get_tokens_per_second():.1f} tokens per second
Average rate:  {self.get_average_tokens_per_second():.1f} tokens per second
        """)


if __name__ == "__main__":
    deepseek_chat = OllamaChat(model=MODEL)

    try:
        for prompt in PROMPTS:
            print(f"Prompt:  {prompt}")
            deepseek_chat(prompt)
            deepseek_chat.print_rate()
        while True:
            user_input = input("Chat with history:  ")
            deepseek_chat(user_input)
            deepseek_chat.print_rate()
    except Exception as e:
        print(f"An error occurred: {e}")
    except KeyboardInterrupt:
        print("")
