from pathlib import Path

from librarian.workflow.execution import workflow_run

def run(args):
    workflow_run(collection_path=Path(args.collection_path))
    return

def config(args):
    pass