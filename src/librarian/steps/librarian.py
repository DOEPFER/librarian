"""
Data preparation step for the Librarian agent.

This module extracts the summary, tags, and available shelves to prepare
the payload for the librarian agent's decision-making process.
"""
from pathlib import Path
import json
import numpy as np

from agno.workflow import StepInput, StepOutput

from librarian.utils.shelves_library import get_shelves
from librarian.utils.embedding import generate_vector
from librarian.utils.cosine_similarity import similarity

from librarian.core.settings import shelves_index_file


def select_shelves(tags: list[str]):

    threshold = 0.5

    tags_str_embedding = str(Path(*tags))
    tags_embedding = generate_vector(prompt=tags_str_embedding)

    with open(shelves_index_file, 'r', encoding='utf-8') as file:
        _shelves = json.load(file)
    
    shelves = []
    for key, value in _shelves.items():

        similarity_value = similarity(np.array(value), np.array(tags_embedding))
        if similarity_value >= threshold:
            shelves.append(key)

    # print('#' * 100)
    # print(shelves)
    # print('#' * 100)
    
    return shelves

def prepare_data(step_input: StepInput) -> StepOutput:
    """
    Prepares the data required by the librarian agent.

    Extracts the tags and summary from the output of the 'Summarize-document'
    step and retrieves the current list of shelves.

    Args:
        step_input (StepInput): The input object containing data from previous steps.

    Returns:
        StepOutput: An object containing the extracted tags, summary, and shelves on success.
    """
    
    tags = step_input.get_step_content("Summarize-document").tags
    summary = step_input.get_step_content("Summarize-document").summary
    # shelves = get_shelves()
    shelves = select_shelves(tags)
    
    return StepOutput(content={'tags': tags, 'summary': summary, 'shelves': shelves}, success=True)