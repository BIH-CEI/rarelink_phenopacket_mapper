import json
from pathlib import Path
from typing import Union, Dict


def read_json(path: Union[str, Path]) -> Dict:
    if isinstance(path, str):
        path = Path(path)

    with open(path) as f:
        return json.load(f)