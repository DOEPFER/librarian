import hashlib
from pathlib import Path


def generate_hash(file: Path) -> str:
    """
    Computes the MD5 checksum of a file.

    Args:
        file (Path): The path to the file.

    Returns:
        str: The MD5 checksum as a hexadecimal string.
    """
    with open(file, "rb") as f:
        digest = hashlib.file_digest(f, "md5")
    return digest.hexdigest()
