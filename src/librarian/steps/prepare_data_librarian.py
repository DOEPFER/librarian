from agno.workflow import StepInput, StepOutput

from librarian.utils.shelves_library import get_shelves


def prepare_data(step_input: StepInput) -> StepOutput:
    tags = step_input.get_step_content("Summarize-document").tags
    summary = step_input.get_step_content("Summarize-document").summary
    shelves = get_shelves()

    return StepOutput(content={'tags': tags, 'summary': summary, 'shelves': shelves}, success=True)