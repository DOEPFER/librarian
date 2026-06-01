"""
Input and output schemas for the Librarian Agent.

This module defines the Pydantic data models used to structure the
data going into and coming out of the Librarian LLM.
"""

from typing import List

from pydantic import BaseModel, Field


class LibrarianInput(BaseModel):
    """
    Represents the input payload provided to the Librarian Agent.
    """

    tags: List[str] = Field(description="Tags to help classify the document.")
    summary: str = Field(description="A summary of the document content.")
    shelves: List[str] = Field(
        description="The folders (shelves) currently existing in the library."
    )


class LibrarianOutput(BaseModel):
    """
    Represents the structured output expected from the Librarian Agent.
    """

    shelf_path: str = Field(
        description="The folder path (shelf) chosen for the analyzed file."
    )
