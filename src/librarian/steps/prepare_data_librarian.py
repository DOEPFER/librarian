"""
Data preparation step for the Librarian agent.

This module extracts the summary, tags, and available shelves to prepare
the payload for the librarian agent's decision-making process.
"""

from agno.workflow import StepInput, StepOutput

from librarian.utils.shelves_library import get_shelves


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
    shelves = get_shelves()

    return StepOutput(content={'tags': tags, 'summary': summary, 'shelves': shelves}, success=True)