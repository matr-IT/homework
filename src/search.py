import re


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