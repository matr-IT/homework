from typing import Generator


def filter_by_currency(operations: list[dict], currency: str) -> Generator:
    """function filters operations by its currency"""
    for operation in operations:
        if operation["operationAmount"]["currency"]["name"] == currency:
            yield operation
        else:
            yield "Транзакции по данной валюте не обнаружены"


def transaction_descriptions(operations: list[dict]) -> Generator:
    """function returns a description of each operation one-by-one"""
    for operation in operations:
        if operation["description"]:
            yield operation["description"]
        else:
            yield "Транзакции не обнаружены"

def generate_card_number(start: int, end: int) -> Generator:
    """generates 16-digits card number"""
    for i in range(start, end+1):
        card_number = []
        num = str(i).zfill(16)
        for j in range(0, 16, 4):
            card_number.append(num[j:j+4])
        yield " ".join(card_number)