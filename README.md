Running [DeepSeek](https://github.com/deepseek-ai) R1 reasoning model using [ollama](https://ollama.com) on an Ubuntu single board computer.

No user login nor registration is needed for the following steps.

- [SBC hardware and setup](#sbc-hardware-and-setup)
- [Install ollama](#install-ollama)
- [Run the model.](#run-the-model)
- [A simple problem](#a-simple-problem)
- [References](#references)
- [Next steps](#next-steps)

# SBC hardware and setup

I used a single board computer rather like a Raspberry Pi.

[OrangePi 5 Plus](http://www.orangepi.org/html/hardWare/computerAndMicrocontrollers/service-and-support/Orange-Pi-5-plus.html) 
* RK3588 SOC (ARM)
* 16GB RAM
* 1TB SSD

Software
* Ubuntu 22.04.5 LTS
* Python 3.10.12

# Install ollama

This step installs `ollama` using a script command from [link](https://ollama.com/download/linux).  This was my 
first time using ollama to run an ML model.  Open Ubuntu Terminal and run this command.
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

The smallest version of [DeepSeek](https://github.com/deepseek-ai) R1 model can now be run.  
This step downloads the model (1.1GiB) first.
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

We can see model information and MIT licence by typing `/show info` and `/show license`.
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

# A simple problem

You can now write a natural language prompt and watch the model reason and generate an answer.  For example here is a simple mathematics problem to sum 3 and 2.
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

The text between `<think>` and `</think>` shows the "reasoning" of the model as it examines the problem.  It has
produced the expected numerical result `5`.

Type `ctrl + d` to quit.

# References

* Training the R1 1.5B model: [DeepSeek R1 Coldstart](https://youtu.be/Pabqg33sUrg?si=EYr9Nqs1zdFuEpul)

# Next steps

* [ ] Check if all CPU cores are being used.
* [ ] Try more reasoning problems.
* [ ] Try larger size DeepSeek R1 "7B" model (4.7GiB download) on the OrangePi 5 Plus.
* [ ] Try single board computer with lower cost RK3588S chip (~100USD).
