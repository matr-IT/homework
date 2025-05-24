def get_mask_card_number(card_number: int) -> str:
    """function gets a card number returns a card number
    with divided in groups by four digits and with masked digits from 7 to 12"""
    str_card_number = str(card_number)
    mask_card_number = str_card_number[0:4] + " " + str_card_number[4:6] + "**" + " **** " + str_card_number[-4:]
    return mask_card_number


def get_mask_account(account_number: int) -> str:
    """function gets acc number and returns it's four last digits with prefix **"""
    str_account_number = str(account_number)
    mask_account_number = "**" + str_account_number[-4:]
    return mask_account_number
