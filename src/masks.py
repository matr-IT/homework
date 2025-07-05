import logging
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent  # Перейти на 2 уровня вверх из src/utils.py
LOG_DIR = BASE_DIR / "logs"  # Директория логов в корне проекта
LOG_FILE = LOG_DIR / "masks.log"

LOG_DIR.mkdir(exist_ok=True, parents=True)

logging.basicConfig(filemode="w")
logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(LOG_FILE, encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: int) -> str:
    """function gets a card number returns a card number
    with divided in groups by four digits and with masked digits from 7 to 12"""
    str_card_number = str(card_number)
    logger.info(f"Проверяем, введен ли номер карты")
    if str_card_number != "":
        logger.info(f"Проверяем длину номера карты")
        if len(str_card_number) == 16:
            logger.info(f"Маскируем карту {card_number}")
            mask_card_number = (
                str_card_number[0:4] + " " + str_card_number[4:6] + "**" + " **** " + str_card_number[-4:]
            )
            logger.info(f"Полученный результат маскировки карты: {mask_card_number}")
            return mask_card_number
        logger.error("Номер карты введен неверно")
        return "Неверный ввод номера карты"
    logger.error("Карта не введена")
    return "Карта не введена"


def get_mask_account(account_number: int) -> str:
    """function gets acc number and returns it's four last digits with prefix **"""
    str_account_number = str(account_number)
    logger.info("Проверяем, введен ли номер счета")
    if str_account_number != "":
        logger.info(f"Проверяем длину номера счета")
        if len(str_account_number) == 20:
            mask_account_number = "**" + str_account_number[-4:]
            logger.info(f"Полученный результат маскировки карты: {mask_account_number}")
            return mask_account_number
        logger.error("Номер счета введен неверно")
        return "Неверный ввод номера счета"
    logger.error("Номер счета не введен")
    return "Номер счета не введен"
