"""Script for benchmarking tokens per second."""

import time

import ollama
from transformers import AutoTokenizer

MODEL_OLLAMA = "deepseek-r1:1.5b"
MODEL_TRANSFORMERS = "deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B"
PROMPT = "What is the sum of 3 + 2?"

tokenizer = AutoTokenizer.from_pretrained(MODEL_TRANSFORMERS)

start_time = time.time()

response = ollama.chat(
    model=MODEL_OLLAMA, messages=[{"role": "user", "content": PROMPT}]
)

time_took = time.time() - start_time

text_output = response["message"]["content"]
print(f"{text_output}\n")

tokens_per_second = response["eval_count"] / time_took

# Test the field `eval_count` is the number of tokens using tokenizer
token_count = len(tokenizer.encode(text_output))
if token_count != response["eval_count"]:
    raise ValueError(
        f"estimated tokens per second {tokens_per_second:0.1f} may be incorrect"
    )
else:
    print(f"tokens per second: {tokens_per_second:.1f} tps")
