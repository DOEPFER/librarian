from typing import List

from pathlib import Path

from librarian.core.settings import library_path, sys_folder_name


def get_shelves() -> List[str]:
    shelves = [shelf.relative_to(library_path).as_posix() for shelf in library_path.rglob(pattern='*/')]
    shelves = [shelf for shelf in shelves if not shelf.startswith(str(sys_folder_name))]
    return shelves

def get_library() -> List[str]:
    library = [doc.relative_to(library_path).as_posix() for doc in library_path.rglob(pattern='*') if doc.is_file()]
    library = [doc for doc in library if not doc.startswith(str(sys_folder_name))]
    return library