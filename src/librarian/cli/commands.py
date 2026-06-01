from pathlib import Path

from librarian.core.settings import logger
from librarian.workflow.execution import workflow_run


def run(args):
    logger.info(msg="Starting workflow...")
    workflow_run(collection_path=Path(args.collection_path))
    return


def config(args):
    pass
