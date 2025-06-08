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
def start_format_date():
    return "2024-03-11T02:26:18.671407"

@pytest.fixture
def empty_date():
    return ""
# Фикстурты для модуля processing.py
