"""
Semantic similarity step for the workflow.

This module evaluates the semantic similarity of a new document against
the existing library index to suggest an appropriate shelf path.
"""

from pathlib import Path
import json

import numpy as np

from agno.workflow import StepInput, StepOutput

from librarian.utils.embedding import generate_vector
from librarian.utils.similarity import similarity

from librarian.core.settings import library_index_file


def semantic_similarity(step_input: StepInput) -> StepOutput:
    """
    Computes semantic similarity to find an appropriate shelf for a document.

    Generates an embedding based on the document's tags and summary, compares it
    against the existing library index, and determines if there is a match above
    a predefined similarity threshold (0.75).

    Args:
        step_input (StepInput): The workflow step input containing the previous step's output (tags and summary).

    Returns:
        StepOutput: The result containing the generated embedding and, if a match is found, the suggested shelf path.
    """
    
    threshold = 0.75

    # name = step_input.previous_step_content.name
    tags = step_input.previous_step_content.tags
    summary = step_input.previous_step_content.summary

    content = f'<tags>{tags}</tags><summary>{summary}</summary>'
    embedding = generate_vector(prompt=content)

    with open(library_index_file, 'r', encoding='utf-8') as file:
        _library = json.load(file)
    
    similar = ('', 0)   
    for key, value in _library.items():

        similarity_value = similarity(np.array(value), np.array(embedding))
        if similarity_value >= threshold and similarity_value > similar[1]:
            similar = (key, similarity_value)
    
    embedding = embedding.tolist()

    if similar[1]:
        return StepOutput(content={'shelf_path': str(Path(similar[0]).parent), 'embedding': embedding}, success=True)
    else:
        return StepOutput(content={'embedding': embedding}, success=False)