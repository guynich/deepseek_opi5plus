Simple AI Agent example.

- [Introduction](#introduction)
- [Example run](#example-run)
- [Next steps](#next-steps)

# Introduction

This script uses the DuckDuckGo search engine to find recent news articles
related to a given topic, extracts text from the articles, and summarizes them
using a locally running DeepSeek-R1 reasoning model.  It is designed to help
gather and summarize news information on a specific topic.

This example was adapted from OpenAI ChatGPT suggested code.  It is a
(very) simple example of an agent that can
* perceive (by fetching content)
* reason (by summarizing with an LLM)
* act (by doing multiple steps without more input)

Install requirements in virtual environment.
```console
cd
source venv_ollama/bin/activate
python3 -m pip install -r ./deepseek_opi5plus/requirements.txt
```

Run the AI agent.
```console
python3 ./deepseek_opi5plus/ai_agent/main.py
```

# Example run

```console
(venv_ollama) orangepi@orangepi5-plus:~$ python3 ./deepseek_opi5plus/ai_agent/main.py
Searching the web for: future of artifical intelligence

Reading: 2 No-Brainer Artificial Intelligence Stocks to Buy Right Now
https://www.msn.com/en-us/money/savingandinvesting/2-no-brainer-artificial-intelligence-stocks-to-buy-right-now/ar-AA1CnGvg
Summarizing, please wait...

Reading: Bloom Energy Is Getting a $2.5 Billion Boost From Artificial Intelligence (AI). Is the Stock a Buy?
https://www.msn.com/en-us/money/topstocks/bloom-energy-is-getting-a-25-billion-boost-from-artificial-intelligence-ai-is-the-stock-a-buy/ar-AA1Clhiu
Summarizing, please wait...

Reading: The Future Of Code: How AI Is Transforming Software Development
https://www.forbes.com/councils/forbestechcouncil/2025/04/04/the-future-of-code-how-ai-is-transforming-software-development/
Summarizing, please wait...
```

Summary report in plain text.  The DeepSeek-R1 model sometimes returns markdown
formatting.
```console
Summary Report:
* 2 No-Brainer Artificial Intelligence Stocks to Buy Right Now:
https://www.msn.com/en-us/money/savingandinvesting/2-no-brainer-artificial-intelligence-stocks-to-buy-right-now/ar-AA1CnGvg
2025-04-06T09:35:00+00:00

The future of artificial intelligence (AI) presents both exciting possibilities and significant challenges. AI's transformative potential lies in its ability to process vast amounts of data across industries, enhancing efficiency and creativity. However, ethical considerations remain critical:

1. **Ethical Concerns**: Issues such as bias and fairness highlight the need for ethical guidelines. For instance, facial recognition systems may exhibit racial biases, necessitating equal treatment.

2. **Collaboration Needs**: AI lacks human traits like empathy and intuition, requiring interdisciplinary efforts to ensure effective collaboration among experts and algorithms.

3. **Human Interaction Challenges**: AI's natural communication is crucial; it must be trained to facilitate clear understanding and prevent confusion or mistrust.

4. **Impact on Society**: In healthcare, AI can improve diagnoses, potentially leading to better outcomes. However, limited accessibility may restrict access for many, leaving some without essential services.

5. **The "AI Race" debate**: While companies argue against AI replacing humans entirely, others emphasize ethical and practical reasons, suggesting a balanced approach is necessary.

6. **Education and Training**: Developers must undergo continuous learning in AI domains to ensure accuracy in predictions and recommendations, fostering partnerships with experts.

7. **Regulations and Ethics**: Increasing strict regulations on AI development and use are essential to address issues like privacy and safety, with many countries now setting ambitious frameworks.

In conclusion, the future of AI holds promise but requires addressing ethical, collaborative, and responsible practices. Continued education, training, and regulation are vital to navigating this evolving landscape.

* Bloom Energy Is Getting a $2.5 Billion Boost From Artificial Intelligence (AI). Is the Stock a Buy?:
https://www.msn.com/en-us/money/topstocks/bloom-energy-is-getting-a-25-billion-boost-from-artificial-intelligence-ai-is-the-stock-a-buy/ar-AA1Clhiu
2025-04-05T08:53:00+00:00

The future of artificial intelligence (AI) is poised to revolutionize human life by augmenting various aspects of our daily lives. Here's a structured overview based on the analysis:

1. **Shift in Human Dependency**: AI is expected to replace human roles in tasks like reasoning, creativity, and problem-solving, which are now more dependent on machines.

2. **Lack of Inherent Intelligence**: Current AI systems operate on preprogrammed algorithms, lacking the same level of intelligence, creativity, and autonomy as humans.

3. **Progression in Capabilities**: Future AI will enhance learning through experience, adaptability to new contexts, and improved problem-solving abilities, moving beyond mere execution.

4. **Ethical Considerations**: The integration of AI raises ethical issues such as job displacement, loss of cultural heritage, and privacy concerns related to data security.

5. **Practical Applications**: AI is already being utilized across industries like manufacturing, healthcare, education, transportation, finance, entertainment, logistics, and energy, with examples in automation tasks.

6. **Risks and Risks**: Potential risks include job displacement if roles shift to routine tasks and the erosion of cultural heritage from those born with AI.

7. **Need for Responsible Use**: Balancing ethical frameworks, regulation, collaboration, and ongoing research is crucial to harnessing AI responsibly.

This summary highlights both opportunities and challenges in the future of AI, emphasizing the need for responsible development and ethical practices.

* The Future Of Code: How AI Is Transforming Software Development:
https://www.forbes.com/councils/forbestechcouncil/2025/04/04/the-future-of-code-how-ai-is-transforming-software-development/
2025-04-04T14:17:00+00:00

**Summary:**

The article discusses the transformative impact of artificial intelligence (AI) on software engineering, highlighting how AI is integrating into the domain through tools like GitHub Copilot and Cursor, which enhance efficiency by focusing on business logic. While this shift presents challenges, it also offers opportunities for engineers to adopt AI-assisted programming roles, requiring them to upskill in AI-related areas. The integration of AI creates new opportunities where machines assist humans while reskilling remains essential. Ultimately, the future of software engineering is likely marked by collaboration between machines and humans, enabling innovative solutions for real-world problems.
```

# Next steps

* [ ] Command line arguments for topic, max number of results, time limits, model.
* [ ] Save the summary report to file.
* [ ] Set up to run automatically (crontab?).
* [ ] Summary formatting.
