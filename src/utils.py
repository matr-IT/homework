import json
from json import JSONDecodeError


def open_json(path: str) -> list:
    """function converts json-files to python list of dicts"""
    with open(path, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except FileNotFoundError:
            return []
        except JSONDecodeError:
            return []
        except Exception:
            return []

print(open_json("/Users/rybin/PycharmProjects/homework/data/operations.json"))