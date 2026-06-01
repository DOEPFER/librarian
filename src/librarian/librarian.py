"""
Main entry point for the Librarian application.

This script initializes the document processing workflow by calling
the execution module with a specified collection path.
"""

from librarian.cli.parser import args

args.execute(args)
