"""
Configuration settings for the Librarian project.

Loads environment variables and initializes core configuration variables,
such as paths to the library, system folders, index files, and API keys.
"""

import os
from pathlib import Path

from dotenv import load_dotenv
from tomlkit import parse

from librarian.log import setup_logging

# Load environment variables
dotenv_path = Path("librarian") / ".env"
load_dotenv(dotenv_path=dotenv_path, override=True)

# Load config
with open("librarian/config/config.toml", "r", encoding="utf-8") as file:
    content = file.read()
    config = parse(content)

# Environment
openai_api_key = os.getenv("OPENAI_API_KEY")

# Settings
library_path = Path(config["settings"]["library_path"])
sys_folder_name = config["settings"]["sys_folder_name"]
library_index_file_name = config["settings"]["library_index_file_name"]
shelves_index_file_name = config["settings"]["shelves_index_file_name"]
embedding_model_id = config["settings"]["embedding_model_id"]
similarity_threshold = config["settings"]["similarity_threshold"]
shelf_similarity_hreshold = 0.5

# Variables
sys_path = library_path / sys_folder_name
library_index_file = sys_path / library_index_file_name
shelves_index_file = sys_path / shelves_index_file_name

# Log
# logger = setup_logging(logprefix=args.logprefix, verbose=args.verbose)
logger = setup_logging(logprefix="librarian", verbose="store_true")
