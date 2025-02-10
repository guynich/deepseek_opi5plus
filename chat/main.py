"""Script for chatting with history using distilled version of DeepSeek R1 model."""

from ollama import chat

MODEL = "deepseek-r1:1.5b"
# Some of these prompts require history to generate a response.
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

    def __call__(self, prompt) -> str:
        self.messages.append({"role": "user", "content": prompt})

        response = chat(model=self.model, messages=self.messages)
        self.eval_counts.append(response.eval_count)
        self.total_duration_secs.append(response.total_duration / 1E9)
        
        self.messages.append({"role": "assistant", "content": response.message.content})
        return response.message.content

    def get_tokens_per_second(self) -> float:
        if len(self.eval_counts) > 0:
            return self.eval_counts[-1] / self.total_duration_secs[-1]
        return 0.0
    
    def get_average_tokens_per_second(self) -> float:
        if len(self.eval_counts) > 0:
            return sum(self.eval_counts) / sum(self.total_duration_secs)
        return 0.0


if __name__ == "__main__":
    deepseek_chat = OllamaChat(model=MODEL)

    for prompt in PROMPTS:
        try:
            print(f"""
User:  {prompt}
generating ...
Assistant:
{deepseek_chat(prompt)}
Rate:          {deepseek_chat.get_tokens_per_second():.1f} tokens per second
Average rate:  {deepseek_chat.get_average_tokens_per_second():.1f} tokens per second
""")
        except Exception as e:
            print(f"An error occurred: {e}")
        except KeyboardInterrupt:
            print("\nUser quit.")
            break
