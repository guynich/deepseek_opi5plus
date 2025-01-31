DeepSeek R1 model generates tokens.  Tokens can be parts of words, subwords,
punctuation, or entire words depending on the "tokenizer" used by this model.

The speed of the model on a computer can be quantified with counting the number
tokens generated per second.

# Installation

In this section python requirements for ollama are installed.

First check ollama is installed and the DeepSeek model version "1.5b" is
available.  You may have done this in the folder above.
```bash
cd
curl -fsSL https://ollama.com/install.sh | sh
ollama pull deepseek-r1:1.5b
```

Clone this repo from GitHub.
```bash
cd
git clone git@github.com:guynich/deepseek_opi5plus
```

Next create a virtual environment called `venv_ollama` and install Python 
packages.
```bash
cd
python3 -m venv venv_ollama
source ./venv_ollama/bin/activate

python3 -m pip install -r deepseek_opi5plus/benchmark/requirements.txt
```

# Run the benchmark

In this section we run the benchmark script to see the model speed expressed in
tokens per second.
```bash
cd
cd deepseek_opi5plus/benchmark

python3 main.py
```

Result on OrangePi 5 Plus single board computer.
```bash
(venv_ollama) orangepi@orangepi-plus:~$ python3 deepseek_opi5plus/benchmark/main.py
None of PyTorch, TensorFlow >= 2.0, or Flax have been found. Models won't be available and only tokenizers, configuration and file/data utilities can be used.
<think>
To find the sum of 3 and 2, I start by identifying the two numbers involved in the addition.

Next, I add these two numbers together to obtain their total.

Finally, I conclude that the result of adding 3 and 2 is 5.
</think>

To find the sum of \(3 + 2\), follow these simple steps:

1. **Identify the Numbers:**

   - The first number is **3**.
   - The second number is **2**.

2. **Add the Numbers Together:**

   \[
   3 + 2 = 5
   \]

3. **Final Answer:**

   \[
   \boxed{5}
   \]

tokens per second: 7.8 tps
```
This rate is equivalent to approximately 5-6 words per second.  Note the model
has generated less tokens and less reasoning text than in the first run.
