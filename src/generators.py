from typing import Generator


def filter_by_currency(operations: list[dict], currency: str) -> Generator:
    """function filters operations by its currency"""
    if operations:
        for operation in operations:
            if operation["operationAmount"]["currency"]["name"] == currency:
                yield operation
            else:
                yield "Нет операций по данной валюте"
    else:
        yield "Операции не обнаружены"


def transaction_descriptions(operations: list[dict]) -> Generator:
    """function returns a description of each operation one-by-one"""
    if operations:
        for operation in operations:
            if operation["description"] != 0:
                yield operation["description"]
    else:
        yield "Операции не обнаружены"


def card_number_generator(start: int, stop: int) -> Generator:
    """generates 16-digits card number"""
    for i in range(start, stop + 1):
        card_number = []
        num = str(i).zfill(16)
        for j in range(0, 16, 4):
            card_number.append(num[j : j + 4])
        yield " ".join(card_number)
