from pathlib import Path

from tomlkit import dumps, parse

from librarian.core.settings import logger
from librarian.workflow.execution import workflow_run


# RUN
def run(args):
    logger.info(msg="Starting workflow...")
    workflow_run(collection_path=Path(args.collection_path), move=args.move)
    return


# CONFIG
def set_config(key: str, value: str) -> bool:
    try:
        with open("librarian/config/config.toml", "r", encoding="utf-8") as file:
            config = parse(file.read())
    except Exception:
        logger.error(msg="Error reading config file.")
        return False
    else:
        try:
            config["settings"][key] = value
            with open("librarian/config/config.toml", "w", encoding="utf-8") as file:
                file.write(dumps(config))
                logger.info(msg="Config file updated.")
        except Exception:
            logger.error(msg="Error writing config file.")
            return False
    return True


def config(args):
    if args.library:
        set_config(key="library_path", value=args.library)
    if args.embedding:
        set_config(key="embedding_model_id", value=args.embedding)
    if args.threshold:
        set_config(key="similarity_threshold", value=args.threshold)
    if args.shelf_threshold:
        set_config(key="shelf_similarity_threshold", value=args.shelf_threshold)
    if args.prefix:
        set_config(key="logprefix", value=args.prefix)

    return
