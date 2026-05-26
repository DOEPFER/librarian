# from typing import List

from pathlib import Path
import json

from librarian.utils.embedding import generate_vector
from librarian.utils.shelves_library import get_shelves, get_library

SYS_PATH = Path('.sys')
SHELVES_INDEX = SYS_PATH / 'shelves.json'
LIBRARY_INDEX = SYS_PATH / 'library.json'

def sys_path(path: Path) -> Path:

    sys = path / SYS_PATH
    
    try:
        sys.mkdir(parents=True, exist_ok=True)
    except Exception:
        pass

def shelf_embeddings(path: Path, model: str) -> None:

    sys_path(path=path)

    # Indice de embeddings
    shelves_file = path / SHELVES_INDEX

    # if not shelves_file.exists():
    #     shelves_file.write_text('{}', encoding='utf-8')

    # Retorna as prateleiras atuais
    library_shelves = get_shelves(path=path)

    try:
        with open(shelves_file, 'r', encoding='utf-8') as file:
            folders = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        folders = {}

    # Reconstroi o arquivo de indices
    new_folders = {}
    for shelf in library_shelves:
        if shelf in folders:
            new_folders[shelf] = folders[shelf]
        else:
            new_folders[shelf] = generate_vector(model=model, prompt=shelf).tolist()

    with open(shelves_file, 'w', encoding='utf-8') as file:
        json.dump(new_folders, file, indent=0, ensure_ascii=False)

def library_embeddings(path: Path, model: str) -> None:

    sys_path(path=path)

    # Indice de embeddings
    library_file = path / LIBRARY_INDEX

    # if not library_file.exists():
    #     library_file.write_text('{}', encoding='utf-8')

    # Retorna a biblioteca atual
    library = get_library(path=path)

    try:
        with open(library_file, 'r', encoding='utf-8') as file:
            files = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        files = {}

    # Reconstroi o arquivo de indices
    new_files = {}
    for doc in library:
        if doc in files:
            new_files[doc] = files[doc]
        else:
            new_files[doc] = []
            # new_files[doc] = generate_vector(model=model, prompt=doc).tolist()
            # um agente deve ser chamado para resumir e gerar um embedding
            # sugerir caminho novo?

    with open(library_file, 'w', encoding='utf-8') as file:
        json.dump(new_files, file, indent=4, ensure_ascii=False)