from agno.workflow import StepInput, StepOutput

from librarian.utils.shelves_library import get_shelves


def prepare_data(step_input: StepInput) -> StepOutput:
    tags = step_input.get_step_content("Summarize-document").tags
    summary = step_input.get_step_content("Summarize-document").summary
    library_shelves = get_shelves(path=step_input.input['library_path'])

    return StepOutput(content={'tags': tags, 'summary': summary, 'library_shelves': library_shelves}, success=True)