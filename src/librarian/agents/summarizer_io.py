from typing import Dict, List
from pydantic import BaseModel, Field

class SummarizerInput(BaseModel):
    metadata: Dict[str, str] = Field(description='Document metadata such as title, author, and subject.')
    sample: str = Field(description='A sample of the document content to help the agent understand the document.')

class SummarizerOutput(BaseModel):
    name: str = Field(description='The name generated for the analyzed file.')
    tags: List[str] = Field(description='Tags to help classify the document.')
    summary: str = Field(description='A summary of the document content.')