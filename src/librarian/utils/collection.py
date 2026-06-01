"""
Utility module for file collection and validation.

This module provides functions to calculate file checksums and filter
incoming collections of documents, avoiding duplicates and invalid formats.
"""

import hashlib
from pathlib import Path
from typing import List

from librarian.core.settings import library_path


def checksum(file: Path) -> str:
    """
    Computes the MD5 checksum of a file.

    Args:
        file (Path): The path to the file.

    Returns:
        str: The MD5 checksum as a hexadecimal string.
    """
    md5_hash = hashlib.md5()
    with open(file, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            md5_hash.update(chunk)
    return md5_hash.hexdigest()


def select_collection(collection_path: Path) -> List[Path]:
    """
    Selects a collection of valid, non-duplicate PDF files for processing.

    This function compares the checksums of the provided files against the existing
    library to prevent duplicates. It also filters out files that are not valid PDFs
    by checking their file signature (magic bytes).

    Args:
        collection_path (Path): The path to a single file or a directory
        containing files.

    Returns:
        List[Path]: A list of file paths that are valid PDFs and not currently
        in the library.
    """

    content_library = library_path.glob(pattern="**/*")
    content_library = [
        checksum(content) for content in content_library if content.is_file()
    ]

    if collection_path.is_file():
        new_files_to_add = (
            [collection_path]
            if checksum(collection_path) not in content_library
            else []
        )
    else:
        content_collection = collection_path.glob(pattern="**/*")
        files_by_checksum = {
            checksum(content): content
            for content in content_collection
            if content.is_file()
        }
        new_files_to_add = [
            path
            for checksum, path in files_by_checksum.items()
            if checksum not in content_library
        ]

    for content in new_files_to_add:
        with open(content, "rb") as file:
            first_bytes = file.read(4)
            if not first_bytes.startswith(b"\x25\x50\x44\x46"):  # pdf signature
                new_files_to_add.remove(content)

    return new_files_to_add
