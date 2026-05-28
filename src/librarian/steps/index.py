from agno.workflow import StepInput, StepOutput

from librarian.core.sys import shelf_embeddings, library_embeddings
from librarian.core.settings import library_index_file, shelves_index_file


def update_index(step_input: StepInput) -> StepOutput:
    shelf_embeddings(shelves_index_file=shelves_index_file)
    library_embeddings(library_index_file=library_index_file)

    return StepOutput(content='', success=True)