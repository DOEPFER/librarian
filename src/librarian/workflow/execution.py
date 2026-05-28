from pathlib import Path

from librarian.utils.collection import select_collection
from librarian.workflow.pipeline import dag


def workflow_run(collection_path:Path) -> None:

    collection = select_collection(collection_path=collection_path)

    for file_path in collection:
        dag.run(
            input={
                'file_path': file_path
            }
        )