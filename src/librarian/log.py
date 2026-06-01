import logging
import sys
import time
from datetime import datetime, timezone
from logging import Logger
from pathlib import Path


def setup_logging(logprefix: str = "librarian", verbose: bool = False) -> Logger:
    log_path = Path("log")
    log_path.mkdir(parents=True, exist_ok=True)

    date = datetime.now(timezone.utc)
    log_file_name = f"{logprefix}_{date:%Y_%m_%d}.log"
    log_file = log_path / log_file_name

    handlers = (
        [
            logging.FileHandler(log_file, encoding="utf-8"),
            logging.StreamHandler(sys.stdout),
        ]
        if verbose
        else [logging.FileHandler(log_file, encoding="utf-8")]
    )

    logging.Formatter.converter = time.gmtime  # UTC

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)sZ | %(levelname)s | [%(name)s] | %(message)s",
        handlers=handlers,  # type: ignore
        datefmt="%Y-%m-%dT%H:%M:%S",  # ISO 8601
    )

    return logging.getLogger("librarian")
