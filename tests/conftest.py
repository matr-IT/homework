import pytest


# Фикстуры для модуля masks.py
@pytest.fixture
def card_number_1():
    return 7000792289606361

@pytest.fixture
def card_number_2():
    return 7000722896042921

@pytest.fixture
def card_number_short():
    return 70007228960429

@pytest.fixture
def card_number_long():
    return 700072289604292112

@pytest.fixture
def card_number_empty():
    return ""

@pytest.fixture
def account_number_1():
    return 73654108430135874305

@pytest.fixture
def account_number_2():
    return 73654108430135875517

@pytest.fixture
def account_number_short():
    return 736541084301358743

@pytest.fixture
def account_number_long():
    return 73654108430135874305123

@pytest.fixture
def account_number_empty():
    return ""

# Фикстурты для модуля widget.py
@pytest.fixture
def account_card_1():
    return "Visa Platinum 7000792289606361"

@pytest.fixture
def account_card_count_1():
    return "Счет 73654108430135874305"

@pytest.fixture
def account_card_short():
    return "Visa Platinum 70007922896063"

@pytest.fixture
def account_card_long():
    return "Visa Platinum 700079228960636112"

@pytest.fixture
def account_card_count_short():
    return "Счет 73654108430135305"

@pytest.fixture
def account_card_count_long():
    return "Счет 73654108430123135874305"

# Фикстурты для модуля processing.py
