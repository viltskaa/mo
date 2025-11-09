from pathlib import Path
import json


def load_requirements(path: Path) -> dict:
    if not path.is_file():
        raise FileExistsError("Path does not have a json file.")
    try:
        with open(path, 'r') as file:
            requirements = json.load(file)
    except json.JSONDecodeError:
        raise FileExistsError("Path does not have a json file.")

    return requirements
