from src.masks import get_mask_account, get_mask_card_number
from src.masks import get_mask_account
from tests.conftest import card_number_1, card_number_2, card_number_short, card_number_long


def test_get_mask_card_number_1(card_number_1):
    assert get_mask_card_number(card_number_1) == "7000 79** **** 6361"

def test_get_mask_card_number_2(card_number_2):
    assert get_mask_card_number(card_number_2) == "7000 72** **** 2921"

def test_get_mask_card_number_short(card_number_short):
    assert get_mask_card_number(card_number_short) == "Неверный ввод номера карты"

def test_get_mask_card_number_long(card_number_long):
    assert get_mask_card_number(card_number_long) == "Неверный ввод номера карты"

def test_get_mask_card_number_empty(card_number_empty):
    assert get_mask_card_number(card_number_empty) == "Карта не введена"

def test_get_mask_account_1(account_number_1):
    assert get_mask_account(account_number_1) == "**4305"

def test_get_mask_account_2(account_number_2):
    assert get_mask_account(account_number_2) == "**5517"

def test_get_mask_account_short(account_number_short):
    assert get_mask_account(account_number_short) == "Неверный ввод номера счета"

def test_get_mask_account_long(account_number_long):
    assert get_mask_account(account_number_long) == "Неверный ввод номера счета"

def test_get_mask_account_empty(account_number_empty):
    assert get_mask_account(account_number_empty) == "Номер счета не введен"