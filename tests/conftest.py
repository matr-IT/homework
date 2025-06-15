import pytest


# Фикстуры для модуля masks.py
@pytest.fixture
def card_number_1() -> int:
    return 7000792289606361


@pytest.fixture
def card_number_2() -> int:
    return 7000722896042921


@pytest.fixture
def card_number_short() -> int:
    return 70007228960429


@pytest.fixture
def card_number_long() -> int:
    return 700072289604292112


@pytest.fixture
def card_number_empty() -> str:
    return ""


@pytest.fixture
def account_number_1() -> int:
    return 73654108430135874305


@pytest.fixture
def account_number_2() -> int:
    return 73654108430135875517


@pytest.fixture
def account_number_short() -> int:
    return 736541084301358743


@pytest.fixture
def account_number_long() -> int:
    return 73654108430135874305123


@pytest.fixture
def account_number_empty() -> str:
    return ""


# Фикстурты для модуля widget.py
@pytest.fixture
def account_card_1() -> str:
    return "Visa Platinum 7000792289606361"


@pytest.fixture
def account_card_count_1() -> str:
    return "Счет 73654108430135874305"


@pytest.fixture
def account_card_short() -> str:
    return "Visa Platinum 70007922896063"


@pytest.fixture
def account_card_long() -> str:
    return "Visa Platinum 700079228960636112"


@pytest.fixture
def account_card_count_short() -> str:
    return "Счет 73654108430135305"


@pytest.fixture
def account_card_count_long() -> str:
    return "Счет 73654108430123135874305"


@pytest.fixture
def start_format_date_1() -> str:
    return "2024-03-11T02:26:18.671407"


@pytest.fixture
def start_format_date_2() -> str:
    return "2025-10-23T02:26:18.671407"


@pytest.fixture
def empty_date() -> str:
    return ""


@pytest.fixture
def non_standard_date_1() -> str:
    return "2023-10-05"


@pytest.fixture
def non_standard_date_2() -> str:
    return "2023-10-05T12:30:45+03:00"


# Фикстурты для модуля processing.py
@pytest.fixture
def list_of_dicts_1() -> list[dict]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def list_of_dicts_2() -> list[dict]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def list_of_dicts_3() -> list[dict]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-06-30T02:08:58.425572"},
    ]

# Фикстуры для generators.py

@pytest.fixture
def different_operations() -> list[dict]:
    return [{
          "id": 939719570,
          "state": "EXECUTED",
          "date": "2018-06-30T02:08:58.425572",
          "operationAmount": {
              "amount": "9824.07",
              "currency": {
                  "name": "USD",
                  "code": "USD"
              }
          },
          "description": "Перевод организации",
          "from": "Счет 75106830613657916952",
          "to": "Счет 11776614605963066702"
      },
      {
              "id": 142264268,
              "state": "EXECUTED",
              "date": "2019-04-04T23:20:05.206878",
              "operationAmount": {
                  "amount": "79114.93",
                  "currency": {
                      "name": "USD",
                      "code": "USD"
                  }
              },
              "description": "Перевод со счета на счет",
              "from": "Счет 19708645243227258542",
              "to": "Счет 75651667383060284188"
       },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "RUB",
                    "code": "RUB"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },

    ]

@pytest.fixture
def empty_operations() -> list[dict]:
    return [{}]
