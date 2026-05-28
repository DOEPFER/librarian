# import sys

from pathlib import Path

from librarian.workflow.execution import workflow_run


# select = fr'{sys.argv[1]}'
# select = Path(select)

# workflow_run(collection_path=select)
workflow_run(collection_path=Path('/home/rafael-doepfer/Documents/librarian_test/collection'))