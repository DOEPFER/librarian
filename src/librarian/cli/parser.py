import argparse
from librarian.cli import commands

parser = argparse.ArgumentParser(
    prog='librarian'
)

# Subparser command
subparsers = parser.add_subparsers(dest='command')
subparsers.required = True

# Run command
run_subparser = subparsers.add_parser('run')
run_subparser.add_argument('collection_path', help='Collection path', type=str)
run_subparser.set_defaults(execute=commands.run)

# Config command
config_subparser = subparsers.add_parser('config')
config_subparser.add_argument('-l', '--library', help='Set library path', type=str)
config_subparser.add_argument('-e', '--embedding', help='Set embedding model ID', type=str)
config_subparser.set_defaults(execute=commands.config)

args = parser.parse_args()