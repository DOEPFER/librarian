from pathlib import Path
import json

import numpy as np

from agno.workflow import StepInput, StepOutput

from librarian.utils.embedding import generate_vector
from librarian.utils.similarity import similarity

from librarian.core.sys import LIBRARY_INDEX


def semantic_similarity(step_input: StepInput) -> StepOutput:
    
    threshold = 0.75

    # name = step_input.previous_step_content.name
    tags = step_input.previous_step_content.tags
    summary = step_input.previous_step_content.summary

    content = f'<tags>{tags}</tags><summary>{summary}</summary>'
    embedding = generate_vector(model='embeddinggemma', prompt=content)

    library_index_file = step_input.input['library_path'] / LIBRARY_INDEX
    # library_index_file.touch(exist_ok=True)
    with open(library_index_file, 'r', encoding='utf-8') as file:
        files = json.load(file)
    
    similar = ('', 0)   
    for key, value in files.items():

        similarity_value = similarity(np.array(value), np.array(embedding))
        if similarity_value >= threshold and similarity_value > similar[1]:
            similar = (key, similarity_value)
    
    if similar[1]:
        return StepOutput(content={'shelf_path': str(Path(similar[0]).parent), 'embedding': embedding}, success=True)
    else:
        return StepOutput(content={'embedding': embedding}, success=False)