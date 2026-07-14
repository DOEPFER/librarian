"""
Index update step for the workflow.

This module defines the step responsible for updating the system's vector
embeddings index for both shelves and documents.
"""

from agno.workflow import StepInput, StepOutput

from librarian.core.settings import library_index_file, shelves_index_file
from librarian.core.system import library_embeddings, shelf_embeddings


def update_index(step_input: StepInput) -> StepOutput:
    """
    Updates the embeddings index for both library shelves and documents.

    Args:
        step_input (StepInput): The input data for the current step in the workflow.

    Returns:
        StepOutput: The result of the step execution, indicating success.
    """
    try:
        shelf_embeddings(shelves_index_file=shelves_index_file)
        library_embeddings(library_index_file=library_index_file)
    except Exception:
        return StepOutput(content="", success=False, stop=True)
    else:
        return StepOutput(content="", success=True)
