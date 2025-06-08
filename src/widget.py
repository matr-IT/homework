from datetime import datetime
from typing import Any

import masks
from masks import get_mask_account, get_mask_card_number


def mask_account_card(type_and_number: str) -> Any:
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
        if len(digits_of_number) == 20:
            masked_number = get_mask_account(digits_of_number)
            full_masked = type_of_number + masked_number
        else:
            return "Неверное количество цифр в номере счета"
    else:
        if len(digits_of_number) == 20:
            masked_number = get_mask_card_number(digits_of_number)
            full_masked = type_of_number + masked_number
        else:
            return "Неверное количество цифр в номере карты"
    return full_masked


def get_date(date_str: str) -> str:
    """function changes the date format from ISO 8601 format to DD.MM.YYYY"""
    if date_str == "":
        return "Дата не введена, введите дату"
    else:
        dt = datetime.fromisoformat(date_str.replace("Z", ""))
        return dt.strftime("%d.%m.%Y")
