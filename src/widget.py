from masks import get_mask_card_number
from masks import get_mask_account


def mask_account_card(type_and_number: str) -> str:
    """gets type and number and masks number"""
    digits_of_number = ""
    type_of_number = ""

    for x in type_and_number:
        if x.isdigit():
            digits_of_number += x
    for x in type_and_number:
        if x.isalpha() or x.isspace():
            type_of_number += x

    if type_of_number == "Счет ":
        masked_number = get_mask_account(digits_of_number)
        full_masked = type_of_number + masked_number
    else:
        masked_number = get_mask_card_number(digits_of_number)
        full_masked = type_of_number + masked_number
    return full_masked


print(mask_account_card("Maestro 1596837868705199"))
print(mask_account_card("Счет 64686473678894779589"))
print(mask_account_card("MasterCard 7158300734726758"))
print(mask_account_card("Счет 35383033474447895560"))
print(mask_account_card("Visa Classic 6831982476737658"))
print(mask_account_card("Visa Platinum 8990922113665229"))
print(mask_account_card("Visa Gold 5999414228426353"))
print(mask_account_card("Счет 73654108430135874305"))

def get_date()