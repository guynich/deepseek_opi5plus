"""AI Agent for summarizing news from the internet."""

import ollama
import requests
from bs4 import BeautifulSoup
from duckduckgo_search import DDGS

MAX_RESULTS = 3
TIME_LIMIT = "w"  # d, w, m.


def search_web(query, max_results=MAX_RESULTS):
    """Search the web using DuckDuckGo news."""
    results = DDGS().news(query, timelimit=TIME_LIMIT, max_results=max_results)
    return results


def extract_text_from_url(url):
    """Extract text from a given URL."""
    try:
        res = requests.get(url, timeout=5)
        soup = BeautifulSoup(res.text, "html.parser")
        paragraphs = soup.find_all("p")
        return " ".join(p.get_text() for p in paragraphs[:10])
    except Exception as e:
        return f"Failed to retrieve content: {e}"


def summarize_text(text, query):
    """Summarize the text using DeepSeek-R1."""
    prompt = f"""You are a research assistant. Please summarize the following article in relation to the query: "{query}".

Article:
{text}

Summary:"""

    response = ollama.chat(
        model="deepseek-r1:1.5b", messages=[{"role": "user", "content": prompt}]
    )
    return response["message"]["content"]


def remove_think_block(text):
    """Remove <think> block from text.  DeepSeek-R1 returns these blocks."""
    if "<think>" in text and "</think>" in text:
        start = text.find("<think>")
        end = text.find("</think>") + len("</think>")
        text = text[:start] + text[end:]

    return text.strip()


def research_topic(topic):
    """Research a topic and summarize the findings."""
    print(f"Searching the web for news on: {topic}")
    search_results = search_web(topic)

    summaries = []
    for result in search_results:
        print(f"\nReading: {result['title']}\n{result['url']}")
        text = extract_text_from_url(result["url"])
        print("Summarizing, please wait...")
        summary = summarize_text(text, topic)
        summary = remove_think_block(summary)
        summaries.append(
            f"* {result['title']}:\n{result['url']}\n{result['date']}\n\n{summary}\n"
        )

    print("\nSummary Report:")
    for s in summaries:
        print(s)


if __name__ == "__main__":
    # Example usage.
    research_topic("future of artifical intelligence")
