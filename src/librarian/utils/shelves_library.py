"""
Utility functions for library file and shelf management.

This module provides helpers to retrieve the current directories (shelves)
and files (documents) within the library, excluding system folders.
"""

from typing import List

from pathlib import Path

from librarian.core.settings import library_path, sys_folder_name


def get_shelves() -> List[str]:
    """
    Retrieves the list of shelves (directories) present in the library.

    Ignores the system folder defined in the settings.

    Returns:
        List[str]: A list of strings containing the relative paths of the shelves.
    """
    shelves = [shelf.relative_to(library_path).as_posix() for shelf in library_path.rglob(pattern='*/')]
    shelves = [shelf for shelf in shelves if not shelf.startswith(str(sys_folder_name))]
    return shelves

def get_library() -> List[str]:
    """
    Retrieves the list of all documents (files) present in the library.

    Ignores the files contained within the system folder defined in the settings.

    Returns:
        List[str]: A list of strings containing the relative paths of the documents.
    """
    library = [doc.relative_to(library_path).as_posix() for doc in library_path.rglob(pattern='*') if doc.is_file()]
    library = [doc for doc in library if not doc.startswith(str(sys_folder_name))]
    return library