import pytest

from src.widget import mask_account_card
from tests.conftest import account_card_1, account_card_count_1


def test_mask_account_card_check(account_card_1: str, account_card_count_1: str) -> str:
    assert mask_account_card(account_card_1) == "Visa Platinum 7000 79** **** 6361"
    assert mask_account_card(account_card_count_1) == "Счет **4305"


@pytest.mark.parametrize(
    "some_account, mask_result",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Счет 35383033474447895560", "Счет **5560"),
    ],
)
def test_mask_account_card_diff_types(some_account: str, mask_result: str) -> str:
    assert mask_account_card(some_account) == mask_result


def test_mask_account_incorrect_data(
    account_card_short: str, account_card_long: str, account_card_count_short: str, account_card_count_long: str
):
    assert mask_account_card(account_card_short) == "Неверное количество цифр в номере карты"
    assert mask_account_card(account_card_long) == "Неверное количество цифр в номере карты"
    assert mask_account_card(account_card_count_short) == "Неверное количество цифр в номере счета"
    assert mask_account_card(account_card_count_long) == "Неверное количество цифр в номере счета"
