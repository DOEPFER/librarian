from pathlib import Path
import json

from librarian.core.settings import sys_path
from librarian.utils.embedding import generate_vector
from librarian.utils.shelves_library import get_shelves, get_library


def create_sys_path(sys_path: Path) -> None:

    try:
        sys_path.mkdir(parents=True, exist_ok=True)
    except Exception:
        pass

    return

def shelf_embeddings(shelves_index_file: Path) -> None:

    create_sys_path(sys_path=sys_path)

    # if not shelves_index_file.exists():
    #     shelves_index_file.write_text('{}', encoding='utf-8')

    # Retorna as prateleiras atuais
    shelves = get_shelves()

    try:
        with open(shelves_index_file, 'r', encoding='utf-8') as file:
            _shelves = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        _shelves = {}

    # Reconstroi o arquivo de indices
    new_shelves = {}
    for shelf in shelves:
        if shelf in _shelves:
            new_shelves[shelf] = _shelves[shelf]
        else:
            new_shelves[shelf] = generate_vector(prompt=shelf).tolist()

    with open(shelves_index_file, 'w', encoding='utf-8') as file:
        json.dump(new_shelves, file, indent=0, ensure_ascii=False)

def library_embeddings(library_index_file: Path) -> None:

    create_sys_path(sys_path=sys_path)

    # if not library_index_file.exists():
    #     library_index_file.write_text('{}', encoding='utf-8')

    # Retorna a biblioteca atual
    library = get_library()

    try:
        with open(library_index_file, 'r', encoding='utf-8') as file:
            _library = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        _library = {}

    # Reconstroi o arquivo de indices
    new_library = {}
    for doc in library:
        if doc in _library:
            new_library[doc] = _library[doc]
        else:
            new_library[doc] = []
            # TODO:
            # new_library[doc] = generate_vector(prompt=doc).tolist()
            # um agente deve ser chamado para resumir e gerar um embedding
            # sugerir caminho novo?

    with open(library_index_file, 'w', encoding='utf-8') as file:
        json.dump(new_library, file, indent=4, ensure_ascii=False)