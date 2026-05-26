from typing import Dict, List
from pydantic import BaseModel, Field

class LibrarianInput(BaseModel):
    tags: List[str] = Field(description='Tags to help classify the document.')
    summary: str = Field(description='A summary of the document content.')
    library_shelves: List[str] = Field(description='The folders (shelves) currently existing in the library.')

class LibrarianOutput(BaseModel):
    shelf_path: str = Field(description='The folder path (shelf) chosen for the analyzed file.')