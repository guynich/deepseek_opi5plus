"""A web-based chat application using Flask and Ollama.
This application allows users to interact with a locally running DeepSeek model.
"""
import argparse
import logging
import re

import markdown
from flask import Flask, render_template, request
from ollama import chat as ollama_chat

DEFAULT_MODEL = "deepseek-r1:1.5b"
DEFAULT_PORT = 5000


class ChatServer:
    def __init__(self):
        self.parser = self._init_argument_parser()
        self.args = self.parser.parse_args()
        self.app = Flask(__name__)
        self.messages = []
        self._setup_logging()
        self._setup_routes()

    @staticmethod
    def _init_argument_parser():
        parser = argparse.ArgumentParser(
            description="Run web server for DeepSeek-R1 chat application.")
        parser.add_argument(
            "--model", 
            type=str, 
            default=DEFAULT_MODEL, 
            help=f"Specify Ollama supported LLM model to use (default: {DEFAULT_MODEL})"
        )
        parser.add_argument(
            "--network", 
            action="store_true", 
            help="Enable any device on the network to connect"
        )
        parser.add_argument(
            "--port", 
            type=int, 
            default=DEFAULT_PORT, 
            help=f"Specify port to run the server on (default: {DEFAULT_PORT})"
        )
        parser.add_argument(
            "--verbose", 
            action="store_true", 
            help="Enable verbose logging output"
        )
        return parser

    def _setup_logging(self):
        """Configure logging for the chat server."""
        logging.basicConfig(
            level=logging.DEBUG if self.args.verbose else logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger(__name__)

    def _setup_routes(self):
        self.app.route("/")(self._handle_home)
        self.app.route("/chat", methods=["POST"])(self._handle_chat_request)

    def _handle_chat_request(self):
        """Handle chat API requests."""
        submitted_input = request.form.get("user_input", "")
        chat_response = self.process_chat_response(submitted_input)
        return {"response": chat_response, "last_question": submitted_input}

    def _handle_home(self) -> str:
        """Handle main page requests."""
        if request.method != "POST":
            return render_template("index.html", 
                                 user_input="", 
                                 chat_response="",
                                 model=self.args.model)

        submitted_input = request.form.get("user_input", "")
        chat_response = self.process_chat_response(submitted_input)
        return render_template(
            "index.html",
            last_question=submitted_input,
            chat_response=chat_response,
            model=self.args.model
        )

    def _process_content(self, content: str) -> str:
        """Process the content to handle <think> blocks and markdown in HTML."""
        content_with_placeholders, think_blocks = self._protect_think_blocks(content)
        
        # Convert markdown to HTML
        processed_content = markdown.markdown(
            content_with_placeholders, extensions=["fenced_code"]
        )
        
        return self._restore_think_blocks(processed_content, think_blocks)

    def _protect_think_blocks(self, content: str) -> tuple[str, list]:
        """Temporarily replace <think> blocks with placeholders."""
        think_blocks = []

        def save_think_block(match):
            think_blocks.append(match.group(0))
            return f"THINK_BLOCK_{len(think_blocks) - 1}"

        content_with_placeholders = re.sub(
            r"<think>[\s\S]*?</think>", save_think_block, content
        )
        return content_with_placeholders, think_blocks

    def _restore_think_blocks(self, content: str, think_blocks: list) -> str:
        """Restore <think> blocks from placeholders."""
        for i, block in enumerate(think_blocks):
            content = content.replace(f"<p>THINK_BLOCK_{i}</p>", block)
        return content

    def process_chat_response(self, user_input: str) -> str:
        """Get response from locally running Ollama model."""
        try:
            self.messages.append({"role": "user", "content": user_input})
            content = ""
            for part in ollama_chat(
                model=self.args.model,
                messages=self.messages,
                options={
                    "seed": 42,
                    "temperature": 0.6,
                },
                stream=True,
            ):
                chunk = part["message"]["content"]
                content += chunk
                if self.args.verbose:
                    # This is a non-logging print to get streaming output.
                    print(chunk, end="", flush=True)
            self.messages.append({"role": "assistant", "content": content})

            duration = part.total_duration / 1e9
            self.logger.info(f"Response generated in {duration:.3f}s ({(part.eval_count / duration):.1f} tok/s)")

            # Process the response content
            processed_content = self._process_content(content)
            return processed_content
            
        except Exception as e:
            self.logger.error(f"Error getting response from Ollama: {e}")
            return f"Sorry, something went wrong.\n{str(e)}"

    def run_server(self):
        config = {
            "debug": True,
            "port": self.args.port,
            "host": "0.0.0.0" if self.args.network else "127.0.0.1"
        }
        self.app.run(**config)


if __name__ == "__main__":
    server = ChatServer()
    server.run_server()
