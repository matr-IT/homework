import pytest

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