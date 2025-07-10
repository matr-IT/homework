import re
from collections import Counter



def process_bank_search(data: list[dict], search: str) -> list[dict]:
    """Filters operations by keyword from their descriptions"""
    if not search:
        return data

    pattern = re.compile(re.escape(search), re.IGNORECASE)

    result = []
    for operation in data:
        if "description" not in operation:
            continue

        description = operation["description"]
        if pattern.search(description):
            result.append(operation)

    return result


def process_bank_operations(data: list[dict], categories: list[str]) -> dict[str, int]:
    """Counts amount of operations in each category by their description"""

    counter = Counter()
    for operation in data:
        description = operation.get("description", "")
        for category in categories:
            pattern = re.compile(re.escape(category), re.IGNORECASE)
            if pattern.search(description):
                counter[category] += 1

    return dict(counter)

