def filter_by_state(list_of_dicts: list[dict], key: str = "EXECUTED") -> list[dict]:
    """sorting list by state"""
    new_list = []
    for i in list_of_dicts:
        if i["state"] == key:
            new_list.append(i)
    return new_list


def sort_by_date(list_of_dicts: list[dict], ascending: bool = True) -> list[dict]:
    """sorting by date"""
    if ascending:
        list_of_dicts.sort(key=lambda x: x["date"])
    if not ascending:
        list_of_dicts.sort(key=lambda x: x["date"], reverse=True)
    return list_of_dicts
