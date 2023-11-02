"""Generic utilities for use in the FastAPI project."""

import json
import os
from typing import Any
import logging

logger = logging.getLogger(__name__)


def dump_to_file(data: Any, file_path: str = "data_dump") -> bool:
    dir_name = "data/"
    dump_success = False
    try:
        if not os.path.exists(os.path.dirname(dir_name)):
            os.makedirs(os.path.dirname(dir_name))
        with open(file_path, "w") as file:
            json.dump(data, file)
            dump_success = True
    except Exception as exc:
        raise exc

    return dump_success


def read_from_dump_file(file_path: str = "data_dump") -> bool:
    data = None
    try:
        with open(file_path, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        logger.exception(f"file not found at {file_path}")
    except Exception as exc:
        raise exc

    return bool(data)
