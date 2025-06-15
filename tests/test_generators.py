import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_card_number_generator() -> None:
    _generator = card_number_generator(1, 5)
    assert next(_generator) == "0000 0000 0000 0001"
    assert next(_generator) == "0000 0000 0000 0002"
    assert next(_generator) == "0000 0000 0000 0003"
    assert next(_generator) == "0000 0000 0000 0004"
    assert next(_generator) == "0000 0000 0000 0005"
    with pytest.raises(StopIteration):
        next(_generator)


def test_filter_by_currency(different_operations: list[dict]) -> None:
    _generator = filter_by_currency(different_operations, "USD")
    assert next(_generator) == {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }
    assert next(_generator) == {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    }
    assert next(_generator) == "Нет операций по данной валюте"
    with pytest.raises(StopIteration):
        next(_generator)


def test_filter_by_currency_no_currency(different_operations: list[dict]) -> None:
    _generator = filter_by_currency(different_operations, "EUR")
    assert next(_generator) == "Нет операций по данной валюте"


def test_filter_by_currency_empty_str(empty_str_operations: str) -> None:
    _generator = filter_by_currency(empty_str_operations, "USD")
    assert next(_generator) == "Операции не обнаружены"
    with pytest.raises(StopIteration):
        next(_generator)


def test_filter_by_currency_empty_list(empty_list_operations: list) -> None:
    _generator = filter_by_currency(empty_list_operations, "USD")
    assert next(_generator) == "Операции не обнаружены"
    with pytest.raises(StopIteration):
        next(_generator)


def test_transaction_descriptions(different_operations: list[dict]) -> None:
    _generator = transaction_descriptions(different_operations)
    assert next(_generator) == "Перевод организации"
    assert next(_generator) == "Перевод со счета на счет"
    assert next(_generator) == "Перевод с карты на карту"
    with pytest.raises(StopIteration):
        next(_generator)


def test_transaction_descriptions_empty_str(empty_str_operations: str) -> None:
    _generator = transaction_descriptions(empty_str_operations)
    assert next(_generator) == "Операции не обнаружены"
    with pytest.raises(StopIteration):
        next(_generator)


def test_transaction_descriptions_empty_list(empty_list_operations: list) -> None:
    _generator = transaction_descriptions(empty_list_operations)
    assert next(_generator) == "Операции не обнаружены"
    with pytest.raises(StopIteration):
        next(_generator)
