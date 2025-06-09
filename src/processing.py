from typing import List

# qwer = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'EXECUTED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'EXECUTED', 'date': '2018-10-14T08:21:33.419441'}]

def filter_by_state(list_of_dicts: list[dict], key: str = "EXECUTED") -> str | list[dict]:
    """sorting list by state"""
    new_list = []
    for i in list_of_dicts:
        if i["state"] == key:
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
        list_of_dicts.sort(key=lambda x: x["date"])
    return list_of_dicts
