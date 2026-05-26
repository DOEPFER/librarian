from typing import List

from pathlib import Path

def get_shelves(path: Path) -> List[str]:
    shelves = [shelf.relative_to(path).as_posix() for shelf in path.rglob(pattern='*/')]
    shelves = [shelf for shelf in shelves if not shelf.startswith('.sys')]
    return shelves

def get_library(path: Path) -> List[str]:
    library = [doc.relative_to(path).as_posix() for doc in path.rglob(pattern='*') if doc.is_file()]
    library = [doc for doc in library if not doc.startswith('.sys')]
    return library