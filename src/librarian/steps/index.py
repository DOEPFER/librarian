from agno.workflow import StepInput, StepOutput

from librarian.core.sys import shelf_embeddings, library_embeddings


def update_index(step_input: StepInput) -> StepOutput:
    library_path = step_input.input['library_path']

    shelf_embeddings(path=library_path, model='embeddinggemma')
    library_embeddings(path=library_path, model='embeddinggemma')
    
    return StepOutput(content='', success=True)