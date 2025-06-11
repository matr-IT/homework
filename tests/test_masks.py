from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number(
    card_number_1: int, card_number_2: int, card_number_short: int, card_number_long: int, card_number_empty: int
) -> None:
    assert get_mask_card_number(card_number_1) == "7000 79** **** 6361"
    assert get_mask_card_number(card_number_2) == "7000 72** **** 2921"
    assert get_mask_card_number(card_number_short) == "Неверный ввод номера карты"
    assert get_mask_card_number(card_number_long) == "Неверный ввод номера карты"
    assert get_mask_card_number(card_number_empty) == "Карта не введена"


def test_get_mask_account(
    account_number_1: int,
    account_number_2: int,
    account_number_short: int,
    account_number_long: int,
    account_number_empty: int,
) -> None:
    assert get_mask_account(account_number_1) == "**4305"
    assert get_mask_account(account_number_2) == "**5517"
    assert get_mask_account(account_number_short) == "Неверный ввод номера счета"
    assert get_mask_account(account_number_long) == "Неверный ввод номера счета"
    assert get_mask_account(account_number_empty) == "Номер счета не введен"
