from mypy.state import state

from src.utils import open_json


def filter_by_state(list_of_dicts: list[dict], key: str = "EXECUTED") -> str | list[dict]:
    """sorting list by state"""
    new_list = []
    for i in list_of_dicts:
        if "state" in i and i["state"] == key:
            new_list.append(i)
    if len(new_list) != 0:
        return new_list
    else:
        return "Нет операций по данному ключу"


def sort_by_date(list_of_dicts: list[dict], descending: bool = True) -> list[dict]:
    """sorting by date"""
    if descending:
        list_of_dicts.sort(key=lambda x: x["date"], reverse=True)
    if not descending:
        list_of_dicts.sort(key=lambda x: x["date"], reverse=False)
    return list_of_dicts
