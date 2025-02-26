"""A simple web-based chat application using Flask and Ollama.
This application allows users to interact with a locally running DeepSeek model
"""

import markdown
from flask import Flask, render_template, request
from ollama import chat as ollama_chat

VERBOSE = False

app = Flask(__name__)

messages = []


def get_chat_response(user_input: str) -> str:
    """Get response from locally running Ollama model."""
    try:
        messages.append({"role": "user", "content": user_input})
        content = ""
        for part in ollama_chat(
            model="deepseek-r1:1.5b",
            messages=messages,
            options={
                "seed": 42,
                "temperature": 0.6,
            },
            stream=True,
        ):
            chunk = part["message"]["content"]
            content += chunk
            if VERBOSE:
                print(chunk, end="", flush=True)
        print()
        messages.append({"role": "assistant", "content": content})

        # Process the content to handle <think> blocks and markdown in HTML.

        # First, protect <think> blocks by replacing them temporarily
        think_blocks = []
        import re

        def save_think_block(match):
            think_blocks.append(match.group(0))
            return f"THINK_BLOCK_{len(think_blocks) - 1}"

        # Save think blocks and replace with placeholders
        content_with_placeholders = re.sub(
            r"<think>[\s\S]*?</think>", save_think_block, content
        )

        # Convert markdown to HTML
        processed_content = markdown.markdown(
            content_with_placeholders, extensions=["fenced_code"]
        )

        # Restore think blocks
        for i, block in enumerate(think_blocks):
            processed_content = processed_content.replace(
                f"<p>THINK_BLOCK_{i}</p>", block
            )
        if VERBOSE:
            print("Processed content:")
            print(processed_content)
        return processed_content
    except Exception as e:
        print(f"Error getting response from Ollama: {e}")
        return "Sorry, please try again."


@app.route("/", methods=["GET", "POST"])
def index() -> str:
    """Handle main page requests."""
    if request.method != "POST":
        return render_template("index.html", user_input="", bot_response="")

    submitted_input = request.form.get("user_input", "")
    chat_response = get_chat_response(submitted_input)
    return render_template(
        "index.html",
        last_question=submitted_input,
        bot_response=chat_response,
    )


@app.route("/chat", methods=["POST"])
def chat():
    """Handle chat API requests."""
    submitted_input = request.form.get("user_input", "")
    chat_response = get_chat_response(submitted_input)
    return {"response": chat_response, "last_question": submitted_input}


if __name__ == "__main__":
    app.run(debug=True)
