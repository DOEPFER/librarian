"""
Final step for moving and indexing documents.

This module provides functionalities to move the processed document
to its designated shelf in the library and update the library index
with its vector embedding.
"""

from pathlib import Path
import json

from agno.workflow import StepInput, StepOutput

from librarian.core.settings import library_path, library_index_file, shelves_index_file
from librarian.utils.embedding import generate_vector


def update_index(index_file: Path, index: str, embedding: str) -> None:
    """
    Updates a JSON index file with a new embedding for a given index key.

    Reads the existing index from the file, updates or adds the entry
    for the specified index, and writes the updated dictionary back to the file.

    Args:
        index_file (Path): The path to the JSON index file.
        index (str): The key representing the shelf or file path to be indexed.
        embedding (str): The vector embedding to be stored for the index.
    """
    with open(index_file, 'r', encoding='utf-8') as file:
        _index = json.load(file)

    _index[index] = embedding

    with open(index_file, 'w', encoding='utf-8') as file:
        json.dump(_index, file, indent=4, ensure_ascii=False)

    return
    
def send_to_shelf(step_input: StepInput) -> StepOutput:
    """
    Copies the processed file to the target shelf and updates the library index.

    Retrieves the designated shelf path from either the semantic similarity step
    or the librarian analysis step. It then copies the file to the new location
    with the generated file name and updates the index with the document's embedding.

    Args:
        step_input (StepInput): The workflow step input containing outputs from previous steps.

    Returns:
        StepOutput: The result of the step execution, indicating success or failure.
    """
    
    src = step_input.input['file_path']
    
    name = step_input.get_step_content('Summarize-document').name
    extension = src.suffix.lower()
    file_name = f'{name}{extension}'

    if (step_input.get_step_output(step_name='Semantic-similarity').success == True):
        shelf_path = step_input.get_step_content('Semantic-similarity')['shelf_path']
    else:
        shelf_path = step_input.get_step_content('Librarian-analysis').shelf_path
                                  
    shelf_path = Path(shelf_path)
    dst = library_path / shelf_path

    try:
        dst.mkdir(parents=True, exist_ok=True)
        
        # src.rename(dst / file_name)
        src.copy(dst / file_name)

        # Update index document embedding
        doc_embedding = step_input.get_step_content('Semantic-similarity')['embedding']
        update_index(index_file=library_index_file, index=str(shelf_path / file_name), embedding=doc_embedding)
        
        # Update index shelf embedding
        shelf_embedding = generate_vector(prompt=str(shelf_path)).tolist()
        update_index(index_file=shelves_index_file, index=str(shelf_path), embedding=shelf_embedding)
    except Exception:
        return StepOutput(content='', success=False)
    else:
        return StepOutput(content='', success=True)