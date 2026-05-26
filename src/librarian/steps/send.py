from pathlib import Path
import json

from agno.workflow import StepInput, StepOutput

from librarian.core.sys import LIBRARY_INDEX

import numpy as np
import numpy.typing as npt


def update_library_index(path: Path, file_shelf: Path, embedding: npt.NDArray[np.float64]) -> None:
    
    library_file = path / LIBRARY_INDEX

    with open(library_file, 'r', encoding='utf-8') as file:
        files = json.load(file)

    files[str(file_shelf)] = embedding.tolist()

    with open(library_file, 'w', encoding='utf-8') as file:
        json.dump(files, file, indent=4, ensure_ascii=False)

    return

def send_to_shelf(step_input: StepInput) -> StepOutput:
    
    src = step_input.input['file_path']
    library_path = step_input.input['library_path']
    
    name = step_input.get_step_content('Summarize-document').name
    extension = src.suffix.lower()
    file_name = f'{name}{extension}'

    if (step_input.get_step_output(step_name='Semantic-similarity').success == True):
        shelf_path = step_input.get_step_content('Semantic-similarity')['shelf_path']
    else:
        shelf_path = step_input.get_step_content('Librarian-analysis').shelf_path

    dst = Path(library_path / shelf_path)
    
    try:
        dst.mkdir(parents=True, exist_ok=True)
        # src.rename(dst / file_name)
        src.copy(dst / file_name)
    except Exception as e:
        print(e)
        return StepOutput(content='', success=False)
    else:
        embedding = step_input.get_step_content('Semantic-similarity')['embedding']
        update_library_index(path=library_path, file_shelf=Path(shelf_path) / Path(file_name), embedding=embedding)
        return StepOutput(content='', success=True)