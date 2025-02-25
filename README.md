Running [DeepSeek-R1](https://github.com/deepseek-ai) reasoning model using 
[Ollama](https://ollama.com) on an Ubuntu single board computer.

> [!TIP]
> Note: Mac users can install the Ollama download [described here](/README_MAC.md).

No user login nor registration is needed for the following steps.  The distilled 
DeepSeek-R1 model runs locally on Ubuntu OS without internet connection after 
installation.

- [SBC hardware and setup](#sbc-hardware-and-setup)
- [Install Ollama](#install-ollama)
- [Run the model.](#run-the-model)
  - [A simple problem](#a-simple-problem)
  - [Prompt history](#prompt-history)
- [Examples](#examples)
  - [Temperature (experimental)](#temperature-experimental)
  - [Benchmarking](#benchmarking)
    - [1.5B model](#15b-model)
    - [7B model](#7b-model)
  - [Chat script](#chat-script)
    - [Installation](#installation)
    - [Run](#run)
- [References](#references)
- [Next steps](#next-steps)

# SBC hardware and setup

I tested several single board computers rather like Raspberry Pi.

Hardware
  
| Board           | Retail  | CPU     | RAM  | Disk  | Website |
| --------------- | ------- | ------- | ---: | ----- | ------- |
| OrangePi 5 Plus | ~150USD | RK3588  | 16GB | 1TB   | [link](http://www.orangepi.org/html/hardWare/computerAndMicrocontrollers/details/Orange-Pi-5-plus.html) |
| OrangePi 5      | ~100USD | RK3588S |  8GB | 250GB | [link](http://www.orangepi.org/html/hardWare/computerAndMicrocontrollers/details/Orange-Pi-5.html) |
| OrangePi 3B     | ~50USD  | RK3566  |  4GB | microSD | [link](http://www.orangepi.org/html/hardWare/computerAndMicrocontrollers/details/Orange-Pi-3B.html) |

Retail estimates do not include cost of disk or microSD, sales tax and shipping.

Software
* Ubuntu 22.04.5 LTS [download](https://joshua-riek.github.io/ubuntu-rockchip-download)
* Python 3.10.12

# Install Ollama

This step installs `Ollama` using a script command from
[link](https://ollama.com/download/linux).  This was my first time using Ollama
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

The text between `<think>` and `</think>` shows the "chain-of-thought" or
reasoning of the model as it examines the problem.  It is not deterministic and
the reasoning text will vary from run to run with the same prompt.

The final text after `</think>` is the model's answer to the prompt and 
produces the expected numerical result `5`.  The text in the answer will 
vary from run to run.  In my testing the numerical result of 5 is consistent.

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

Type `ctrl + d` to quit.  

## Prompt history
Ollama stores a text file containing prompt history in the folder `.ollama`.  
This prompt history is available using the cursor keys to scroll back through your 
earlier prompts when running a model.

On a new run of the command `ollama run deepseek-r1:1.5b` I did not observe the model 
has any context from any earlier runs.

Should you wish to delete this history then delete the file.
```console
cd
rm -f .ollama/history
```

# Examples

## Temperature (experimental)

DeepSeek documentation recommends changing 
[parameter `temperature`](https://api-docs.deepseek.com/quick_start/parameter_settings) 
based on the use case.  This documentation does not state if this guidance is
specific to the V3 model or the R1 model.  

DeepSeek R1 model documentation also mentions setting the `temperature` in these
[usage recommendations](https://github.com/deepseek-ai/DeepSeek-R1#usage-recommendations).

To experiment with this parameter Ollama offers customization of a model using 
[Modelfile documentation](https://github.com/ollama/ollama/blob/main/docs/modelfile.md#ollama-model-file).  
An example [Modelfile_r1_1.5b](/Modelfile_r1_1.5b) is provided in this repo
with a temperature parameter.

To run the customized model first create `r1`.  The DeepSeek R-1 1.5B model
needs to be pulled first if not already done as before.
```console
ollama pull deepseek-r1:1.5b

ollama create r1 -f ./Modelfile_r1_1.5b
```

Then run the customized model `r1`.
```console
ollama run r1
```

I'm not sure I see a difference in the answers compared with running the 
model `ollama run deepseek-r1:1.5b`.  This Modelfile is provided for 
experimentation and comments are welcome!

## Benchmarking

The speed of this model version on a computer can be quantified with counting 
the number of tokens generated per second.  The `ollama` application provides 
flag `--verbose` to return timing values.

### 1.5B model

Command.
```bash
ollama run deepseek-r1:1.5b --verbose
```
Result for the question "What is the sum of 3 + 2?" run on OrangePi 5 Plus.
```console
total duration:       24.601935746s
load duration:        92.272721ms
prompt eval count:    14 token(s)
prompt eval duration: 138ms
prompt eval rate:     101.45 tokens/s
eval count:           193 token(s)
eval duration:        24.369s
eval rate:            7.92 tokens/s
```
The returned `eval rate` value for this run was 7.9 tokens per second.  For five
runs I saw variation in range [7.77, 8.03] tokens per second and the number of 
`eval count` tokens varied in range [131, 193].

I used an earlier deprecated script in this repo to generate the following table 
data for a single prompt.  The DeepSeek-R1 1.5B distilled model running on 
OrangePi 5 Plus generated 7.8 tokens per second.   I also ran the same test on 
lower cost OrangePi 5 board (different CPU, less RAM) which ran about 10% 
slower.  

| Model | Board           | CPU     | Tokens per second | Other    |
| ----- | --------------- | ------- | ----------------- | -------- |
| 1.5B  | OrangePi 5 Plus | RK3588  | 7.8               | 16GB RAM |
| 1.5B  | OrangePi 5      | RK3588S | 7.0               | 8GB RAM  |
| 1.5B  | OrangePi 3B     | RK3566  | 2.4               | 4GB RAM  |

The rates for the first two rows are equivalent to approximately 4-6 words per 
second which is faster than human speech (roughly 2 words per second).  The 
lowest cost board (OrangePi 3B) rate is slower than human speech.

### 7B model

Command.
```bash
ollama run deepseek-r1:7b --verbose
```
The `eval rate` value for this run on OrangePi 5 Plus was 2.6 tokens per second.
The text update at this rate is too slow to my attention.  I think a 
distilled R1 model size in between 1.5B and 7B (say 3B or 4B) could be a good 
trade-off for this CPU.

## Chat script

This section describes a chat example with several stored prompts using Ollama's 
Python API.  It is more convenient for testing than using the `ollama run` 
command.

### Installation

In this section python requirements are installed for running the example.

First check Ollama is installed as described above.
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

### Run

In this example a sequence of stored prompts are passed to the model.  This 
method creates context history for the later answers.
```bash
cd
cd deepseek_opi5plus/chat
python3 main.py
```
The model generates reasoning and answers with context.  The rate of the model
is printed in tokens per second including the session average rate.  See 
[chat folder README](/chat/README.md#result) for more information.

# References

* Ollama.
    * [ollama.com](http://www.ollama.com).  A platform and framework for running and managing LLMs.  Useful for running models without internet connectivity.
    * DeepSeek-R1 model documentation [ollama.com/library/deepseek](https://ollama.com/library/deepseek-r1:1.5b).  Includes model quantization.
    * Ollama's Python API: [github.com/ollama](https://github.com/ollama/ollama-python).  I found example scripts `chat-with-history.py` and `chat-steam.py` helpful.
* Training the R1 1.5B model.
    * DeepSeek-R1 Coldstart [youtube.com](https://youtu.be/Pabqg33sUrg?si=EYr9Nqs1zdFuEpul).  Running a DeepSeek-R1 distilled model on Ollama is demonstrated in this video.
* Ubuntu OS.
    * RockChip single board computers: [github.com/Joshua-Riek](https://github.com/Joshua-Riek/ubuntu-rockchip/releases).  I used Ubuntu Desktop OS 22.04 from this repo dated [2024-10-22](https://joshua-riek.github.io/ubuntu-rockchip-download/boards/orangepi-5-plus.html).

# Next steps

* [x] Check if all CPU cores are being used.
* [x] Quantify tokens per second.
* [x] Try OrangePi 5 single board computer with lower cost RK3588S chip and less memory (~100USD retail with 8GB RAM).
* [x] Try more reasoning examples.
* [x] Print chat script session in a stream
* [x] Try larger size DeepSeek-R1 "7B" model (4.7GiB download) on the OrangePi 5 Plus.
* [x] Try [OrangePi 3B](http://www.orangepi.org/html/hardWare/computerAndMicrocontrollers/details/Orange-Pi-3B.html) single board computer (~50 USD retail with 4GB RAM) with microSD card.
* [x] Add Ollama Modefile with temperature.
* [ ] Update chat/README for OrangePi 5 run with `"seed": 42` in chat script.
