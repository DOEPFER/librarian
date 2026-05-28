"""
Final step for moving and indexing documents.

This module provides functionalities to move the processed document
to its designated shelf in the library and update the library index
with its vector embedding.
"""

from pathlib import Path
import json

from agno.workflow import StepInput, StepOutput

from librarian.core.settings import library_path, library_index_file


def update_library_index(file_shelf: Path, embedding: str) -> None:
    """
    Updates the library index file with the document's vector embedding.

    Args:
        file_shelf (Path): The relative path of the file within the library.
        embedding (str): The vector embedding representing the document's content.
    """

    with open(library_index_file, 'r', encoding='utf-8') as file:
        library = json.load(file)

    library[str(file_shelf)] = embedding

    with open(library_index_file, 'w', encoding='utf-8') as file:
        json.dump(library, file, indent=4, ensure_ascii=False)

    return

def send_to_shelf(step_input: StepInput) -> StepOutput:
    """
    Moves the processed file to the target shelf and updates the library index.

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
        shelf_path = Path(step_input.get_step_content('Semantic-similarity')['shelf_path'])
    else:
        shelf_path = Path(step_input.get_step_content('Librarian-analysis').shelf_path)

    dst = library_path / shelf_path

    try:
        dst.mkdir(parents=True, exist_ok=True)
        
        # src.rename(dst / file_name)
        src.copy(dst / file_name)

        embedding = step_input.get_step_content('Semantic-similarity')['embedding']
        update_library_index(file_shelf=shelf_path / file_name, embedding=embedding)
    except Exception:
        return StepOutput(content='', success=False)
    else:
        return StepOutput(content='', success=True)