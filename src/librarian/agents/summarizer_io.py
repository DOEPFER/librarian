"""
Input and output schemas for the Summarizer Agent.

This module defines the Pydantic data models used to structure the
data going into and coming out of the summarizer LLM.
"""

from typing import Dict, List

from pydantic import BaseModel, Field


class SummarizerInput(BaseModel):
    """
    Represents the input payload provided to the Summarizer Agent.
    """

    metadata: Dict[str, str] = Field(
        description="Document metadata such as title, author, and subject."
    )
    sample: str = Field(
        description="A sample of the document content to help the agent understand the document."
    )


class SummarizerOutput(BaseModel):
    """
    Represents the structured output expected from the Summarizer Agent.
    """

    name: str = Field(description="The name generated for the analyzed file.")
    tags: List[str] = Field(description="Tags to help classify the document.")
    summary: str = Field(description="A summary of the document content.")
