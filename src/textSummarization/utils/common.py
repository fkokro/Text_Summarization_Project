import os
import yaml
from textSummarization.logging import logger
from pathlib import Path


def read_yaml(path_to_yaml: Path)->dict:
    """ Read a YAML file and return the contents as a dictionary.
    Args: 
        path_to_yaml (Path): Path to the YAML file.
    Raise:
        FileNotFoundError: If the YAML file does not exist.
    Returns:
        Dict: The contents of the YAML file as a dictionary.
    """
    try:
        with open(path_to_yaml, 'r') as f:
            logger.info(f"YAML file: {path_to_yaml} loaded successfully.")
            return dict(yaml.safe_load(f))

    except FileNotFoundError as e:
        logger.error(e)

    except Exception as e:
        raise e
    
    
def create_directories(path_to_directories: list, verbose=True)->None:
    """ Create a list of directories.
    Args:
        path_to_directories (list): List of directories to create.
    Raises:
        FileExistsError: If a directory already exists.
    """
    for directory in path_to_directories:
        os.makedirs(directory, exist_ok=True)
        if verbose:
            logger.info(f"Directory {directory} created successfully.")
            

def get_size(path_to_file: Path)-> str:
    """ Get the size of a file.
    Args:
        path (Path): Path to the file.
    Returns:
        str: The size of the file in bytes.
    """
    return str(round(os.path.getsize(path_to_file))) + "kb"       