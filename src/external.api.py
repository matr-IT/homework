import os

import requests
from dotenv import load_dotenv

load_dotenv()


def transaction_amount(transaction):
    """functions gets value of transaction converted into RUB"""
    tran_amount = transaction["operationAmount"]["amount"]
    tran_amount_code = transaction["operationAmount"]["currency"]["code"]
    if tran_amount_code == "RUB":
        return tran_amount
    else:
        if tran_amount_code == "EUR" or tran_amount_code == "USD":
            url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={tran_amount_code}&amount={tran_amount}"
            headers = {"apikey": os.getenv("API_KEY_EXCHANGE")}

            response = requests.get(url, headers=headers)
            return response.json()["result"]
