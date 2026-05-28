"""
Document sampling step for the workflow.

This module provides functionality to extract metadata and a text sample
from a PDF document to be used in subsequent analysis steps.
"""

from pypdf import PdfReader

from agno.workflow import StepInput, StepOutput


def sample_file(step_input: StepInput) -> StepOutput:
    """
    Extracts metadata and a text sample from the first few pages of a PDF.

    Reads the PDF file specified in the step input, retrieves basic metadata
    (title, author, subject), and extracts text from up to the first 7 pages
    to create a content sample.

    Args:
        step_input (StepInput): The workflow step input containing the 'file_path'.

    Returns:
        StepOutput: The result containing the extracted 'metadata' and 'sample' on success,
        or a failure status if an error occurs.
    """

    file_path = step_input.input['file_path']
    
    max_pages = 7

    try:
        with open(file_path, 'rb') as file:
            pdf = PdfReader(file)

            # metadata
            metadata = pdf.metadata
            if metadata is None:
                metadata = {'title': '', 'author': '', 'subject': ''}
            else:       
                metadata = {
                    'title': metadata.title if metadata.title is not None else '',
                    'author': metadata.author if metadata.author is not None else '',
                    'subject': metadata.subject if metadata.subject is not None else ''
                }

            # metadata_xmp = pdf.xmp_metadata
            # metadata_xmp = {
            #     'title': metadata_xmp.dc_title if metadata_xmp.dc_title is not None else '',
            #     'author': metadata_xmp.dc_creator if metadata_xmp.dc_creator is not None else '',
            #     'subject': metadata_xmp.dc_description if metadata_xmp.dc_description is not None else ''
            # }
            
            total_pages = len(pdf.pages)

            max_pages = min(max_pages, total_pages)
            
            # sample
            sample = ''
            for i in range(max_pages):
                page = pdf.pages[i]
                sample += page.extract_text()
    except Exception:
        return StepOutput(content='', success=False)
    else:
        return StepOutput(content={'metadata': metadata, 'sample': sample}, success=True)