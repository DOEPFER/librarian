"""
Workflow pipeline definition for the Librarian project.

This module defines the Directed Acyclic Graph (DAG) for the document processing
workflow. It outlines the sequence of steps, from indexing and sampling to
summarization, similarity checking, librarian analysis, and finally moving
the document to its designated shelf.
"""

from agno.workflow import Condition, Step, Workflow

from librarian.agents.librarian import librarian
from librarian.agents.summarizer import summarizer
from librarian.steps.index import update_index
from librarian.steps.librarian import prepare_data
from librarian.steps.sample import sample_file
from librarian.steps.send import to_shelf
from librarian.steps.similarity import semantic_similarity

# STEPS
step_0 = Step(
    name="Index", description="Update the library's index files", executor=update_index
)

step_1 = Step(
    name="Sample-file",
    description="""
    Extract a sample of the document content
    to help the agent understand the document.
    """,
    executor=sample_file,
)

step_2 = Step(
    name="Summarize-document",
    description="Analyze the document and generate, file name, summary and tags.",
    agent=summarizer,
)

step_3 = Step(
    name="Semantic-similarity",
    description="""
    Check the semantic similarity with other files and, if a match is found,
    move it to the same folder (shelf).
    """,
    executor=semantic_similarity,
)

step_4 = Step(
    name="Prepare-data",
    description="Prepare the data for the Librarian agent.",
    executor=prepare_data,
)

step_5 = Step(
    name="Librarian-analysis",
    description="Analyze the document and generate a path (shelf).",
    agent=librarian,
)

step_6 = Step(
    name="Send-to-shelf",
    description="Send the analyzed file to the appropriate folder (shelf).",
    executor=to_shelf,
)

# WORKFLOW
dag = Workflow(
    name="Librarian execution pipeline",
    steps=[
        step_0,
        step_1,
        step_2,
        step_3,
        Condition(
            name="Semantic-similarity-found",
            evaluator=lambda step_input: (
                step_input.get_step_output(step_name="Semantic-similarity").success
                == (not True)
            ),
            steps=[step_4, step_5],
        ),
        step_6,
    ],
    debug_mode=True,
)
