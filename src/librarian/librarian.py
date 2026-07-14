"""
Main entry point for the Librarian application.

This script initializes the document processing workflow by calling
the execution module with a specified collection path.
"""

from librarian.cli.parser import parse_arguments
from librarian.core import settings
from librarian.log import setup_logging

args = parse_arguments()

if args.verbose:
    settings.logger = setup_logging(logprefix=settings.logprefix, verbose=True)

args.execute(args)
