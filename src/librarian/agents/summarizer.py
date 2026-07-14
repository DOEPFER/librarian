"""
Summarizer Agent configuration module.

This module initializes the Summarizer agent responsible for generating
a file name, a summary, and a list of tags for a given document using an LLM.
"""

from pathlib import Path

from agno.agent import Agent
from agno.models.ollama import Ollama

# from agno.models.openai import OpenAIChat
from librarian.agents.summarizer_io import SummarizerInput, SummarizerOutput

# from librarian.core.settings import openai_api_key

# Ollama
model = Ollama(
    id="gemma4:e2b",
    options={"temperature": 0.75, "num_thread": 12, "num_batch": 2048},
    format="json",
    keep_alive="0s",
)

# OpenAI
# model = OpenAIChat(id="gpt-5.4-mini", api_key=openai_api_key, temperature=0.75)

description_file = Path(__file__).parent / "summarizer_description.md"
DESCRIPTION = description_file.read_text(encoding="utf-8")

instructions_file = Path(__file__).parent / "summarizer_instructions.md"
INSTRUCTIONS = instructions_file.read_text(encoding="utf-8")

summarizer = Agent(
    name="Summarizer",
    role="Summarizer",
    model=model,
    description=DESCRIPTION,
    instructions=INSTRUCTIONS,
    input_schema=SummarizerInput,
    output_schema=SummarizerOutput,
    debug_mode=True,
    # debug_level=1,
)
