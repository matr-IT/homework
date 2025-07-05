import json
import logging
from json import JSONDecodeError
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent  # Перейти на 2 уровня вверх из src/utils.py
LOG_DIR = BASE_DIR / "logs"  # Директория логов в корне проекта
LOG_FILE = LOG_DIR / "utils.log"

LOG_DIR.mkdir(exist_ok=True, parents=True)

logging.basicConfig(filemode='w')
logger = logging.getLogger('utils')
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(LOG_FILE, encoding='utf-8')
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)



def open_json(path: str) -> list:
    """function converts json-files to python list of dicts"""
    with open(path, "r", encoding="utf-8") as f:
        try:
            logger.info(f'Открываем JSON-файл по ссылке {path}')
            return json.load(f)
        except FileNotFoundError as ex:
            logger.error(f'Произошла ошибка: {ex}. Файл {path} не найден')
            return []
        except JSONDecodeError as ex:
            logger.error(f'Произошла ошибка: {ex}. Ошибка декодирования файла {path}')
            return []
        except Exception as ex:
            logger.error(f'Произошла ошибка: {ex}')
            return []

