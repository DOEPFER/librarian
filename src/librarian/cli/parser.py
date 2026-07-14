import argparse

from librarian.cli import commands

parser = argparse.ArgumentParser(prog="librarian")
parser.add_argument("-v", "--verbose", help="Verbose mode.", action="store_true")

# Subparser command
subparsers = parser.add_subparsers(dest="command")
subparsers.required = True

# Run command
run_subparser = subparsers.add_parser("run")
run_subparser.add_argument("collection_path", help="Collection path", type=str)
run_subparser.add_argument(
    "-m", "--move", help="Move files to shelf", action="store_true"
)

run_subparser.set_defaults(execute=commands.run)

# Config command
config_subparser = subparsers.add_parser("config")
config_subparser.set_defaults(execute=commands.config)

config_subparser.add_argument("-l", "--library", help="Set library path", type=str)
config_subparser.add_argument(
    "-e", "--embedding", help="Set embedding model ID", type=str
)
config_subparser.add_argument(
    "-t", "--threshold", help="Set similarity threshold", type=float
)
config_subparser.add_argument(
    "-s", "--shelf_threshold", help="Set shelf similarity threshold", type=float
)
config_subparser.add_argument(
    "-p", "--prefix", help="Set log file prefix.", type=str, default="librarian"
)


def parse_arguments():
    return parser.parse_args()
