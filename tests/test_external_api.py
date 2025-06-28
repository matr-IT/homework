from unittest.mock import patch
from src.external_api import transaction_amount

@patch('requests.get')
def test_transaction_amount(mock_get):
    mock_get.return_value.json.return_value = {"operationAmount": {
      "amount": "71771.90",
      "currency": {
        "name": "USD",
        "code": "USD"}}}
    assert transaction_amount("mock_get") == 5641954.034313
