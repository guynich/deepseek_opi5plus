Chat session example using Ollama's Python API and DeepSeek-R1 1.5B model.

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
    "What is the capital city of France?",
    "Describe briefly a historical event from that city.",
]
```

# Result.

This example was run on an OrangePi 5 single board computer with 8GB RAM.  The
model rate dropped from ~7 to above 4 tokens per second as the session 
progressed. Suspected root cause for this slowdown is SoC CPU clock throttling 
under sustained load: more thermal cooling may mitigate.
```console
(venv_ollama) orangepi@orangepi5-desktop:~/deepseek_opi5plus/chat$ python3 main.py

User:  What is the sum of 3 + 2?
generating ...
Assistant:
<think>
First, I need to add the numbers 3 and 2 together.

Next, I will perform the addition step by step. Starting with 3 and adding 2 makes it 5 in total.

Finally, the sum of 3 and 2 is 5.
</think>

To find the sum of **3 + 2**, follow these simple steps:

1. **Start with the first number:**  
   You begin with **3**.

2. **Add the second number:**  
   Next, add **2** to **3**:  
   \[
   3 + 2 = 5
   \]

3. **Final Answer:**  
   The sum of 3 and 2 is **5**.

\[
\boxed{5}
\]
Rate:          7.3 tokens per second
Average rate:  7.3 tokens per second


User:  What is the result if +1 is added to both numbers before summing them?
generating ...
Assistant:
<think>
Okay, let's try to figure this out step by step. 

First, we're adding two numbers together, which are 3 and 2. That part is straightforward:

\[ 3 + 2 = 5 \]

Now, the question asks us to add **+1** before summing them. Hmm, does that mean we should first add 1 to each number before adding them together? 

Wait a second—if I add 1 to both numbers first, it would look like this:

\[ (3 + 1) + (2 + 1) \]

Calculating inside the parentheses first:

\[ 4 + 3 = 7 \]

So, if we add 1 before summing, the result is **7**. 

Alternatively, does "adding +1 to both numbers" mean adding it to just one of them? That would change things entirely. If I only added 1 to 3:

\[ 3 + 1 = 4 \]

Then add 2:

\[ 4 + 2 = 6 \]

In this case, the result is **6**.

I think the correct interpretation depends on how "adding +1 before summing them" is meant. It could either mean adding 1 to each number first or just one of them. To ensure clarity, it's important to specify whether we're modifying both numbers equally or only one.

If we consider that we need to add **+1** to both numbers equally, the total would be:

\[ (3 + 1) + (2 + 1) = 4 + 3 = 7 \]

Therefore, the result of adding +1 before summing is **7**. 

To summarize:

- If you adjust each number by adding 1 first:
  
\[
\boxed{7}
\]

- If you add 1 to just one number and then sum them:
  
\[
\boxed{6}
\]

Depending on the intended interpretation, either **7** or **6** would be the correct answer.
Rate:          6.1 tokens per second
Average rate:  6.4 tokens per second


User:  What is the capital city of France?
generating ...
Assistant:
<think>

</think>

The capital city of France is **Paris**.
Rate:          4.2 tokens per second
Average rate:  6.3 tokens per second


User:  Describe an historical event from the 18th century in that city.
generating ...
Assistant:
<think>

To describe a historical event from the 18th century in Paris, I can focus on its importance during that era:

**The Formation and Growth of the French Republic:**

In the early 1700s, Paris was the capital of France, and the country began to transition from a centrally planned economy to a more democratic system. The establishment of the **Empire State** (1694–1732) in the 17th century laid the foundation for this new government.

A significant event during this period was Paris's involvement in the **Treaty between France and Russia (1680-1691)**, which marked a pivotal moment in France's independence. This treaty helped formalize Paris' role as an independent political and economic center.

Beyond its political status, Paris became a hub for various social movements, including the French Revolution of 1789, which reshaped modern European history with its violent overthrow of the monarchy and its emphasis on individual rights and freedoms.
Rate:          4.7 tokens per second
Average rate:  5.8 tokens per second

(venv_ollama) orangepi@orangepi5-desktop:~/deepseek_opi5plus/chat$ 
```
