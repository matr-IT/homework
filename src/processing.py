def filter_by_state(list_of_dicts: list[dict], key: str = "EXECUTED") -> list[dict]:
    """sorting list by state"""
    new_list = []
    for i in list_of_dicts:
        if i["state"] == key:
            new_list.append(i)
    return new_list


def sort_by_date(list_of_dicts: list[dict], descending: bool = True) -> list[dict]:
    """sorting by date"""
    if descending:
        list_of_dicts.sort(key=lambda x: x["date"], reverse=True)
    if not descending:
        list_of_dicts.sort(key=lambda x: x["date"])
    return list_of_dicts
