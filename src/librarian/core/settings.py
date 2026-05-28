from pathlib import Path

import os
from dotenv import load_dotenv

dotenv_path = Path('librarian') / 'config' / '.env'
load_dotenv(dotenv_path=dotenv_path, override=True)

# Environment
library_path = Path(os.getenv('LIBRARY_PATH'))
sys_folder_name = os.getenv('SYS_FOLDER_NAME')
library_index_file_name = os.getenv('LIBRARY_INDEX_FILE_NAME')
shelves_index_file_name = os.getenv('SHELVES_INDEX_FILE_NAME')

openai_api_key = os.getenv('OPENAI_API_KEY')
embedding_model_id = os.getenv('EMBEDDING_MODEL_ID')
# similarity_threshold = os.getenv('SIMILARITY_THRESHOLD')

# Variables
sys_path = library_path / sys_folder_name
library_index_file = sys_path / library_index_file_name
shelves_index_file = sys_path / shelves_index_file_name