"""Chatting with history using distilled DeepSeek-R1 reasoning model."""

from ollama import chat as ollama_chat

MODEL = "deepseek-r1:1.5b"
PROMPTS = [
    ("What is the sum of 3 + 2?"),
    ("What is the result if +1 is added to both numbers before summing them?"),
    # Mathematical reasoning.
    (
        "A car travels 60 miles in 1 hour. It then travels an additional "
        "90 miles in 2 hours.  What is the car's average speed for the entire "
        "trip?"
    ),
    (
        "What if the car had traveled 30 miles in the first hour instead of "
        "60 miles?"
    ),
    # Logical Deduction.
    (
        "Alice, Bob, and Charlie each have a different favorite color: red, "
        "blue, or green.  Alice's favorite color is not red. Bob's favorite "
        "color is not blue. Charlie's favorite color is not green. "
        "Who likes which color?"
    ),
    # Code Debugging.
    (
        "The following Python function is supposed to identify even numbers, "
        "but there is a bug. Identify and fix it. "
        "`def is_even(num): return num % 2 == 1` "
        "Explain the mistake and provide a corrected version."
    ),
    # Physics Problem Solving.
    (
        "A ball is dropped from a height of 100 meters. Assuming no air "
        "resistance, how long will it take to reach the ground? Use g = 9.8m/s² "
        "and show your step-by-step calculations."
    ),
    # Pattern Recognition.
    (
        "What is the next number in the sequence? "
        "2, 6, 12, 20, 30, ___ "
        "Explain your reasoning."
    ),
]


class ChatMetrics:
    """Track performance metrics for chat interactions."""

    duration: float = 0.0
    tokens: int = 0

    def tokens_per_second(self) -> float:
        """Return tokens processed per second."""
        return self.tokens / self.duration if self.duration > 0 else 0.0


class OllamaChat:
    """A chat interface with history for Ollama large language models."""

    def __init__(self, model: str):
        self.model = model
        self.messages = []
        self.current_metrics = ChatMetrics()
        self.total_metrics = ChatMetrics()

    def __call__(self, prompt: str) -> None:
        self.messages.append({"role": "user", "content": prompt})

        content = ""
        for part in ollama_chat(
            model=self.model,
            messages=self.messages,
            options={
                "seed": 42,
                "temperature": 0.6,
            },
            stream=True,
        ):
            chunk = part["message"]["content"]
            print(chunk, end="", flush=True)
            content += chunk

        self.messages.append({"role": "assistant", "content": content})

        # Update metrics
        self.current_metrics.duration = part.total_duration / 1e9
        self.current_metrics.tokens = part.eval_count
        self.total_metrics.duration += self.current_metrics.duration
        self.total_metrics.tokens += self.current_metrics.tokens

    def print_metrics(self) -> None:
        print(f"""
Last response:
  Duration:      {self.current_metrics.duration:.1f}s
  Tokens:        {self.current_metrics.tokens}
  Speed:         {self.current_metrics.tokens_per_second():.1f} tokens/s

Session total:
  Duration:      {self.total_metrics.duration:.1f}s
  Tokens:        {self.total_metrics.tokens}
  Average speed: {self.total_metrics.tokens_per_second():.1f} tokens/s
        """)


if __name__ == "__main__":
    deepseek_chat = OllamaChat(model=MODEL)
    print(f"Model:   {MODEL}\n")
    try:
        for prompt in PROMPTS:
            print(f"Prompt:  {prompt}")
            deepseek_chat(prompt)
            deepseek_chat.print_metrics()

        while True:
            user_input = input("Chat with history:  ")
            deepseek_chat(user_input)
            deepseek_chat.print_metrics()
    except Exception as e:
        print(f"An error occurred: {e}")
    except KeyboardInterrupt:
        print("")
