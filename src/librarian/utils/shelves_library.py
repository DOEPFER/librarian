"""
Utility functions for library file and shelf management.

This module provides helpers to retrieve the current directories (shelves)
and files (documents) within the library, excluding system folders.
"""

from typing import List

from librarian.core.settings import library_path, sys_folder_name


def get_shelves() -> List[str]:
    """
    Retrieves the list of shelves (directories) present in the library.

    Ignores the system folder defined in the settings.

    Returns:
        List[str]: A list of strings containing the relative paths of the shelves.
    """

    return [
        shelf.relative_to(library_path).as_posix()
        for shelf in library_path.rglob(pattern="*/")
        if shelf.relative_to(library_path).parts[0] != sys_folder_name
    ]


def get_library() -> List[str]:
    """
    Retrieves the list of all documents (files) present in the library.

    Ignores the files contained within the system folder defined in the settings.

    Returns:
        List[str]: A list of strings containing the relative paths of the documents.
    """

    return [
        doc.relative_to(library_path).as_posix()
        for doc in library_path.rglob(pattern="*")
        if doc.is_file() and doc.relative_to(library_path).parts[0] != sys_folder_name
    ]
