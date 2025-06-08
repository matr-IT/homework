from src.masks import get_mask_account, get_mask_card_number
from tests.conftest import card_number_1, card_number_2, card_number_long, card_number_short


def test_get_mask_card_number(
    card_number_1: int, card_number_2: int, card_number_short: int, card_number_long: int, card_number_empty: str
):
    assert get_mask_card_number(card_number_1) == "7000 79** **** 6361"
    assert get_mask_card_number(card_number_2) == "7000 72** **** 2921"
    assert get_mask_card_number(card_number_short) == "Неверный ввод номера карты"
    assert get_mask_card_number(card_number_long) == "Неверный ввод номера карты"
    assert get_mask_card_number(card_number_empty) == "Карта не введена"


def test_get_mask_account(
    account_number_1, account_number_2, account_number_short, account_number_long, account_number_empty
):
    assert get_mask_account(account_number_1) == "**4305"
    assert get_mask_account(account_number_2) == "**5517"
    assert get_mask_account(account_number_short) == "Неверный ввод номера счета"
    assert get_mask_account(account_number_long) == "Неверный ввод номера счета"
    assert get_mask_account(account_number_empty) == "Номер счета не введен"
