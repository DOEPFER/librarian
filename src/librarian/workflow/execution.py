# import os
# from dotenv import load_dotenv

from pathlib import Path

from librarian.utils.collection import select_collection
# from librarian.utils.shelves_library import get_shelves
from librarian.workflow.pipeline import dag


# load_dotenv(override=True)
# LIBRARY_PATH = Path(os.getenv('LIBRARY_PATH'))

def run(path, library_path):

    # collection = select_collection(collection=path, library=library_path)
    collection = select_collection(collection=Path('/home/rafael-doepfer/Documents/librarian_test/collection'), library=library_path)

    for file_path in collection:
        # library_shelves = get_shelves(path=library_path)

        dag.run(
            input={
                'library_path': library_path,
                # 'library_shelves': library_shelves,
                'file_path': file_path
            }
        )