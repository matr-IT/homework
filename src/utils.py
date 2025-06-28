import json
from json import JSONDecodeError


def open_json(path: str) -> list:
    with open(path, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except JSONDecodeError:
            return []
        except Exception:
            return []
