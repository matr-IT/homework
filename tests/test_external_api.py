import os
from unittest.mock import MagicMock, patch

import pytest

from src.external_api import transaction_amount


def test_rub_transaction():
    """Test for transaction in RUB"""
    transaction = {"operationAmount": {"amount": "1000.00", "currency": {"code": "RUB"}}}

    result = transaction_amount(transaction)

    assert result == "1000.00"


@patch("src.external_api.requests.get")
@patch("src.external_api.os.getenv")
def test_eur_transaction(mock_getenv, mock_requests_get):
    """Test for transaction in RUB"""
    mock_getenv.return_value = "test_api_key"
    mock_response = MagicMock()
    mock_response.json.return_value = {"result": 95.50}
    mock_requests_get.return_value = mock_response

    transaction = {"operationAmount": {"amount": "1.00", "currency": {"code": "EUR"}}}

    result = transaction_amount(transaction)

    assert result == 95.50
    mock_getenv.assert_called_once_with("API_KEY_EXCHANGE")
    mock_requests_get.assert_called_once_with(
        "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=EUR&amount=1.00",
        headers={"apikey": "test_api_key"},
    )
