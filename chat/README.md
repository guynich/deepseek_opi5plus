Chat example using Ollama's Python API.

# Installation

Follow the steps in the [top level README](/README.md#installation).

# Run chat session

Several chat prompts with context are stored in a list in the main script.
```bash
cd
source ./venv_ollama/bin/activate

cd deepseek_opi5plus/chat

python3 main.py
```

The example prompts.
```console
PROMPTS = [
    "What is the sum of 3 + 2?",
    "What is the result if +1 is added to both numbers before summing them?",
    "What is the capital of France?",
    "Describe briefly a historical event from that city.",
]
```

# Result.
```console
(venv_ollama) orangepi@orangepi5-plus:~/deepseek_opi5plus/chat$ python3 main.py
User:  What is the sum of 3 + 2?
Assistant:
<think>
First, I need to identify the two numbers in the addition problem: 3 and 2.

Next, I will add these two numbers together by combining their values.

Finally, I can express the result as a number.
</think>

To find the sum of \(3 + 2\), follow these simple steps:

1. **Identify the Numbers:**
   \[
   3 \quad \text{and} \quad 2
   \]

2. **Add the Numbers Together:**
   \[
   3 + 2 = 5
   \]

Therefore, the sum of \(3 + 2\) is:

\[
\boxed{5}
\]

User:  What is the result if +1 is added to both numbers before summing them?
Assistant:
<think>
Okay, so I have this math problem: What is the result if +1 is added to both numbers before summing them?

Alright, let me try to make sense of it. The original question was about adding 3 and 2. But now, we're modifying those numbers by adding 1 to each one first. So instead of doing \(3 + 2\), I need to do \((3 + 1) + (2 + 1)\).

Let me write that down:

\[
(3 + 1) + (2 + 1)
\]

Now, let's compute what's inside the parentheses first.

Starting with the first part:
\[
3 + 1 = 4
\]

Then, for the second part:
\[
2 + 1 = 3
\]

So now I have:
\[
4 + 3
\]

Finally, adding those together:
\[
4 + 3 = 7
\]

Wait a minute. That seems straightforward. But let me double-check to make sure I didn't make any mistakes.

Original numbers: \(3\) and \(2\).

Adding \(1\) to each:
\[
3 + 1 = 4 \quad \text{and} \quad 2 + 1 = 3
\]

Summing those results:
\[
4 + 3 = 7
\]

Yes, that looks correct. So the final answer is:

\[
\boxed{7}
\]
</think>

To solve the problem of adding \(+1\) to both numbers before summing them, follow these steps:

1. **Original Numbers:** \(3\) and \(2\)

2. **Add \(+1\) to Each Number:**
   \[
   3 + 1 = 4 \quad \text{and} \quad 2 + 1 = 3
   \]

3. **Sum the Adjusted Numbers:**
   \[
   4 + 3 = 7
   \]

**Final Answer:** \(\boxed{7}\)

User:  What is the capital of France?
Assistant:
<think>

Alright, so I need to figure out which city is the capital of France. Let me think about this step by step.

1. **Understanding Capital Cities:** A capital city is typically the largest and most populous city in a country. It's where the capital is officially designated based on its population size.

2. **Thinking About France:** France is one of the seven countries in Europe, known for being a beautiful and diverse nation with a rich history.

3. **Quick Recall:** I believe Paris is the capital of France. I've heard it referred to as the "capital of the world," which makes sense because of its location and growth over time.

4. **Double-Checking the Name:** To make sure, I'll think about any other cities associated with France. Lyon comes to mind, but that's a major city in southern France. Paris is definitely more commonly recognized as the capital.

5. **Quick Fact Check:** Yes, Paris is indeed the country's capital. It's home to the Eiffel Tower and has been a bustling city in recent years due to its economic success.

6. **Final Answer:** The capital of France is **Paris**.

\[
\boxed{\text{Paris}}
\]

User:  Describe briefly a historical event from that city.
Assistant:
<think>

Okay, so I need to describe a brief historical event from Paris. Let's break this down step by step:

1. **Understanding Historical Events in Paris:** Paris has a rich history with significant historical events throughout its history.

2. **Identifying a Relevant Event:** The Great Truce was an important event where two neighboring countries, France and Russia, came together to end the War of the Spanish Succession in 1638. This marked a turning point in the fight for Paris from the Spanish domination.

3. **Breaking Down the Great Truce:** The agreement led to political changes that kept Paris neutral until the French Revolution of 1789. It was a significant step in the development of modern France and highlighted the power of the Parisians under Napoleon Bonaparte.

4. **Contextualizing the Event:** This event happened before the French Revolution, showing how Paris had grown from a vulnerable city into an important political center after the Treaty of Le May 1868.

5. **Brief Summary of the Event:** The Great Truce between France and Russia in 1638 marked the end of the Spanish dominance, established Paris as an independent and powerful capital, and laid the groundwork for future political and economic changes in France.

**Final Answer:** In 1638, the French and Spanish Wars led to the signing of the Great Truce between France and Castile. This event ended the prolonged conflict and established Paris as a significant neutral city during the transition to neutral before the French Revolution.
\[
\boxed{\text{The signing of the Great Truce in 1638 marked the end of the Spanish Wars, establishing Paris as a neutral city.}}
\]

(venv_ollama) orangepi@orangepi5-plus:~/deepseek_opi5plus/chat$
```

# Next steps

* [ ] Print chat in realtime, see https://github.com/ollama/ollama-python/blob/main/examples/generate-stream.py.
