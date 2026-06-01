"""
Workflow execution module.

This module provides the entry point for executing the document processing
pipeline (DAG) over a given collection of files or a single file.
"""

from pathlib import Path

from librarian.utils.collection import select_collection
from librarian.workflow.pipeline import dag


def workflow_run(collection_path: Path) -> None:
    """
    Executes the workflow pipeline for a collection of files.

    Validates and selects files from the provided path, then triggers the
    Directed Acyclic Graph (DAG) pipeline for each valid file.

    Args:
        collection_path (Path): The path to a file or a directory of files to process.
    """

    collection = select_collection(collection_path=collection_path)

    for file_path in collection:
        dag.run(input={"file_path": file_path})
