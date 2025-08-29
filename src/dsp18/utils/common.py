import os
import yaml
from src.dsp18 import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
from box.exceptions import BoxValueError

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Reads a YAML file and returns its content as a ConfigBox.

    Args:
        path_to_yaml (Path): The path to the YAML file.

    Raises:
        ValueError: If the YAML file is empty
        e: empty file

    Returns:
        ConfigBox: ConfigBox type.
    """

    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"YAML file {path_to_yaml} loaded successfully.")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError(f"YAML file {path_to_yaml} is empty.") 
    except Exception as e:
        raise e

@ensure_annotations
# def create_directories(path_to_directories: list, verbose=True):
#     """Creates directories if they do not exist.

#     Args:
#         path_to_directories (list): List of directory paths to create.
#         ignore_log (bool, optional): Ignore if multiple directories are to be created. Defaults to False.
#     """
#     for dir_path in path_to_directories:
#         os.mkdir(dir_path, exist_ok=True)
#         if verbose:
#             logger.info(f"Created directory: {dir_path}")

def create_directories(path_to_directories: list, verbose=True):
    for dir_path in path_to_directories:
        Path(dir_path).mkdir(parents=True, exist_ok=True)
        if verbose:
            logger.info(f"Created directory: {dir_path}")

@ensure_annotations
def save_json(path_to_json: Path, data: dict):
    """Saves a dictionary as a JSON file.

    Args:
        path_to_json (Path): The path to the JSON file.
        data (dict): The data to save.
    """
    with open(path_to_json, 'w') as json_file:
        json.dump(data, json_file, indent=4)

    logger.info(f"JSON file saved at {path_to_json}.")

@ensure_annotations
def load_json(path_to_json: Path) -> ConfigBox:
    """Loads a JSON file data.

    Args:
        path_to_json (Path): The path to the JSON file.

    Returns:
        ConfigBox: Data as class attributes instead of dict.
    """
    with open(path_to_json, 'r') as json_file:
        content = json.load(json_file)
    logger.info(f"JSON file loaded from {path_to_json}.")
    return ConfigBox(content)

@ensure_annotations
def save_bin(data: Any, path_to_bin: Path):
    """Saves binary file.

    Args:
        data (Any): The data to be saved as binary.
        path_to_bin (Path): The path to the binary file.
    """
    joblib.dump(value=data, filename=path_to_bin)
    logger.info(f"Binary file saved at {path_to_bin}.")


@ensure_annotations
def load_bin(path_to_bin: Path) -> Any:
    """Loads binary file.

    Args:
        path_to_bin (Path): The path to the binary file.

    Returns:
        Any: The loaded data.
    """
    data = joblib.load(path_to_bin)
    logger.info(f"Binary file loaded from {path_to_bin}.")
    return data 
