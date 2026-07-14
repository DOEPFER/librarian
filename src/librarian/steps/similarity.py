"""
Semantic similarity step for the workflow.

This module evaluates the semantic similarity of a new document against
the existing library index to suggest an appropriate shelf path.
"""

import json
from pathlib import Path

import numpy as np
from agno.workflow import StepInput, StepOutput

from librarian.core.settings import library_index_file, logger, similarity_threshold
from librarian.utils.cosine import similarity
from librarian.utils.embedding import generate_vector


def semantic_similarity(step_input: StepInput) -> StepOutput:
    """
    Computes semantic similarity to find an appropriate shelf for a document.

    Generates an embedding based on the document's tags and summary, compares it
    against the existing library index, and determines if there is a match above
    a predefined similarity threshold.

    Args:
        step_input (StepInput): The workflow step input containing the previous step's
        output (tags and summary).

    Returns:
        StepOutput: The result containing the generated embedding and,
        if a match is found, the suggested shelf path.
    """

    tags = step_input.previous_step_content.tags
    summary = step_input.previous_step_content.summary

    doc_str_embedding = f"<tags>{tags}</tags><summary>{summary}</summary>"
    doc_embedding = generate_vector(prompt=doc_str_embedding)

    try:
        with open(library_index_file, "r", encoding="utf-8") as file:
            _library = json.load(file)
    except Exception:
        logger.error(msg="Error reading library index file.")
        return StepOutput(content="", success=False, stop=True)
    else:
        logger.info(msg="Checking semantic similarity...")
        similar = ("", 0)
        for key, value in _library.items():
            similarity_value = similarity(np.array(value), np.array(doc_embedding))
            if (
                similarity_value >= similarity_threshold
                and similarity_value > similar[1]
            ):
                similar = (key, similarity_value)

        doc_embedding = doc_embedding.tolist()

        # --------------------------------------------------------------------------
        # tags_str_embedding = str(Path(*tags))
        # tags_embedding = generate_vector(prompt=tags_str_embedding)

        # with open(shelves_index_file, "r", encoding="utf-8") as file:
        #     _shelves = json.load(file)

        # similar_shelf = ("", 0)
        # for key, value in _shelves.items():
        #     similarity_value = similarity(np.array(value), np.array(tags_embedding))
        #     if (
        #         similarity_value >= similarity_threshold
        #         and similarity_value > similar_shelf[1]
        #     ):
        #         similar_shelf = (key, similarity_value)
        # --------------------------------------------------------------------------

        if similar[1]:
            return StepOutput(
                content={
                    "shelf_path": str(Path(similar[0]).parent),
                    "embedding": doc_embedding,
                },
                success=True,
            )
        else:
            return StepOutput(content={"embedding": doc_embedding}, success=False)
