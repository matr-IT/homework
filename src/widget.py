from masks import get_mask_card_number
from masks import get_mask_account


def mask_account_card(type_and_number: str) -> str:
    """gets type and number and masks number"""
    if "Счет" in type_and_number:
        masked = type_and_number[0:5] + get_mask_account(int(type_and_number[-20:]))

    elif "Maestro" in  type_and_number:
        masked = type_and_number[0:8] + get_mask_card_number(int(type_and_number[-16:]))

    elif "Visa Platinum" in type_and_number:
        masked = type_and_number[0:14] + get_mask_card_number(int(type_and_number[-16:]))
    return masked

print(mask_account_card('Visa Platinum 7000792289606361'))
print((mask_account_card("Maestro 1596837868705199")))