Running [DeepSeek](https://github.com/deepseek-ai) R1 reasoning model using [ollama](https://ollama.com) on an Ubuntu single board computer.

No user login nor registration is needed for the following steps.

- [SBC hardware and setup](#sbc-hardware-and-setup)
- [Install ollama](#install-ollama)
- [Run the model.](#run-the-model)
  - [A simple problem](#a-simple-problem)
- [Examples](#examples)
  - [Installation](#installation)
  - [Benchmarking](#benchmarking)
  - [Chat](#chat)
- [References](#references)
- [Next steps](#next-steps)

# SBC hardware and setup

I tested several single board computers rather like Raspberry Pi.

[OrangePi 5 Plus](http://www.orangepi.org/html/hardWare/computerAndMicrocontrollers/details/Orange-Pi-5-plus.html)
* ~150USD retail
* RK3588 SOC (ARM)
* 16GB RAM
* 1TB SSD

[OrangePi 5](http://www.orangepi.org/html/hardWare/computerAndMicrocontrollers/details/Orange-Pi-5.html)
* ~100USD retail
* RK3588S SOC (ARM)
* 8GB RAM
* 250GB SSD

Software
* Ubuntu 22.04.5 LTS
* Python 3.10.12

# Install ollama

This step installs `ollama` using a script command from
[link](https://ollama.com/download/linux).  This was my first time using ollama
to run an ML model.  Open Ubuntu Terminal and run this command.
```bash
cd
curl -fsSL https://ollama.com/install.sh | sh
```

Result.
```bash
orangepi@orangepi-plus:~$ curl -fsSL https://ollama.com/install.sh | sh
>>> Installing ollama to /usr/local
[sudo] password for orangepi:
>>> Downloading Linux arm64 bundle
#############################################################             85.2%
######################################################################## 100.0%
>>> Creating ollama user...
>>> Adding ollama user to render group...
>>> Adding ollama user to video group...
>>> Adding current user to ollama group...
>>> Creating ollama systemd service...
>>> Enabling and starting ollama service...
Created symlink /etc/systemd/system/default.target.wants/ollama.service → /etc/systemd/system/ollama.service.
>>> The Ollama API is now available at 127.0.0.1:11434.
>>> Install complete. Run "ollama" from the command line.
WARNING: No NVIDIA/AMD GPU detected. Ollama will run in CPU-only mode.
orangepi@orangepi-plus:~$
```
The install has determined there is no supported GPU so the model will be run on CPU only.

# Run the model.

The smallest distilled version of [DeepSeek](https://github.com/deepseek-ai) R1 model can
now be run on this single board computer.  This step downloads the model (1.1GiB) first.
```bash
ollama run deepseek-r1:1.5b
```

Result is a command prompt.
```bash
orangepi@orangepi-plus:~$ ollama run deepseek-r1:1.5b
pulling manifest
pulling aabd4debf0c8... 100% ▕███████████████████████████████████████████████████████████████████████████████▏ 1.1 GB
pulling 369ca498f347... 100% ▕███████████████████████████████████████████████████████████████████████████████▏  387 B
pulling 6e4c38e1172f... 100% ▕███████████████████████████████████████████████████████████████████████████████▏ 1.1 KB
pulling f4d24e9138dd... 100% ▕███████████████████████████████████████████████████████████████████████████████▏  148 B
pulling a85fe2a2e58e... 100% ▕███████████████████████████████████████████████████████████████████████████████▏  487 B
verifying sha256 digest
writing manifest
success
>>> Send a message (/? for help)
```

We can see model information and licence by typing `/show info` and
`/show license`.  
* It is shared using the permissive open-source software MIT license.
* This distilled model is based on Alibaba Cloud's Qwen team's model architecture and trained weights.
* It uses 4-bit quantization same as the LLM that we used on a project called [AI in Box](https://github.com/usefulsensors/ai_in_a_box#quick-start) at Useful Sensors.  At Google I worked on quantizing ML models with 4-bits of weight precision with great results.
```bash
>>> /show info
  Model
    architecture        qwen2
    parameters          1.8B
    context length      131072
    embedding length    1536
    quantization        Q4_K_M

  Parameters
    stop    "<｜begin▁of▁sentence｜>"
    stop    "<｜end▁of▁sentence｜>"
    stop    "<｜User｜>"
    stop    "<｜Assistant｜>"

  License
    MIT License
    Copyright (c) 2023 DeepSeek

>>> /show license
MIT License

Copyright (c) 2023 DeepSeek

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

>>> Send a message (/? for help)
```

## A simple problem

You can now write a natural language prompt and watch the model reason and
generate an answer.  For example here is a simple mathematics problem to sum
3 and 2.
```bash
>>> What is the sum of 3 + 2 ?
<think>
Okay, let's tackle this problem step by step. I'm trying to find the sum of 3 plus 2.

First, I need to understand what addition means. Addition is like combining two numbers to get a total. So, when I see "3 + 2,"
it means I have three items and I add two more items to them.

Let me visualize this: imagine I have 3 apples. If I take another 2 apples, how many apples do I have in total?

Adding 1 apple to my 3 apples gives me 4 apples.
Adding another apple brings the total to 5 apples.

So, by adding 2 to 3, I end up with **5** apples.

I can also think of it on a number line. Starting at 3 and moving 2 steps forward lands me on 5.

To make sure I'm correct, I'll do the math again:
\[
3 + 2 = 5
\]
Yes, that's right.

Therefore, the sum of 3 and 2 is **5**.
</think>

To solve the addition problem \(3 + 2\), follow these steps:

1. **Identify the numbers being added:**
   - The first number is **3**.
   - The second number is **2**.

2. **Add the two numbers together:**
   \[
   3 + 2 = 5
   \]

3. **Conclusion:**
   - The sum of \(3\) and \(2\) is **5**.

\(\boxed{5}\)

>>> Send a message (/? for help)
```

The text between `<think>` and `</think>` shows the "reasoning" of the model as
it examines the problem.  It has produced the expected numerical result `5`.  

The model generated answer has several types of text formatting (Markdown, LaTeX) 
which are not rendered in my block above.  The answer is duplicated here with an 
indent to demonstrate the Markdown formatting.

> To solve the addition problem \(3 + 2\), follow these steps:
> 
> 1. **Identify the numbers being added:**
>   - The first number is **3**.
>   - The second number is **2**.
>
> 2. **Add the two numbers together:**
>    \[
>    3 + 2 = 5
>    \]
> 
> 3. **Conclusion:**
>    - The sum of \(3\) and \(2\) is **5**.

The session retains information from earlier questions for context.  So if 
you ask a follow-up question, such as 
`repeat the sum but first add +1 to both numbers`,
the model will recall the original numbers from the previous question during
reasoning before providing the correct answer `7`.

Type `ctrl + d` to quit.  In my testing the memory of previous questions is not
retained after quitting.

# Examples

This section describes DeepSeek R1 model examples using Ollama's Python API.

## Installation

In this section python requirements are installed for running the examples.

First check ollama is installed as described above.
```bash
cd
curl -fsSL https://ollama.com/install.sh | sh
```

Make DeepSeek model version "1.5b" available.
```bash
ollama pull deepseek-r1:1.5b
```

Clone this repo from GitHub.
```bash
cd
git clone git@github.com:guynich/deepseek_opi5plus
```

Next create a Python virtual environment called `venv_ollama` and install
packages.
```bash
sudo apt update
sudo apt install python3.10-venv

cd
python3 -m venv venv_ollama
source ./venv_ollama/bin/activate

python3 -m pip install -r deepseek_opi5plus/requirements.txt
```

## Benchmarking

The speed of this model version on a computer can be quantified with counting 
[the number of tokens generated per second](/benchmark/README.md).
```bash
cd
cd deepseek_opi5plus/benchmark
python3 main.py
```
The complete script results are shown in the 
[benchmark folder README](/benchmark/README.md).

The "1.5B" model running on OrangePi 5 Plus generates 7.8 tokens per second.  I also
ran the same test on lower cost OrangePi 5 board (different CPU, less RAM) which
ran about 10% slower.

| Board           | CPU     | Tokens per second | Other    |
| --------------- | ------- | ----------------- | -------- |
| OrangePi 5 Plus | RK3588  | 7.8               | 16GB RAM |
| OrangePi 5      | RK3588S | 7.0               | 8GB RAM  |

## Chat

In this example several stored prompts with context are passed to the model.
```bash
cd
cd deepseek_opi5plus/chat
python3 main.py
```
The model generates reasoning and answers with context. The complete script 
results are shown in the
[chat folder README](/chat/README.md#result).

# References

* Training the R1 1.5B model: [DeepSeek R1 Coldstart](https://youtu.be/Pabqg33sUrg?si=EYr9Nqs1zdFuEpul)

# Next steps

* [x] Check if all CPU cores are being used.
* [x] Quantify tokens per second.
* [x] Try OrangePi 5 single board computer with lower cost RK3588S chip and less memory (~100USD retail).
* [ ] Try OrangePi 3B single board computer (~50 USD retail with 4GB RAM)
* [x] Try more reasoning examples.
* [ ] Try larger size DeepSeek R1 "7B" model (4.7GiB download) on the OrangePi 5 Plus.

