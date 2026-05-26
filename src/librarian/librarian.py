import os
from dotenv import load_dotenv

from pathlib import Path

import sys
import time

from librarian.workflow.execution import run


load_dotenv(override=True)
LIBRARY_PATH = Path(os.getenv('LIBRARY_PATH'))

# select = fr'{sys.argv[1]}'
# select = Path(select)

# run(path=select, library_path=LIBRARY_PATH)
run(path='', library_path=LIBRARY_PATH)

# print(select)
# time.sleep(5)


# backup_folder = os.getenv(key='BACKUP_FOLDER', default=False)
# collection_folder = os.getenv(key='COLLECTION_FOLDER')