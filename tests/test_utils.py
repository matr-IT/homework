import pytest
from unittest.mock import patch, mock_open
from json import JSONDecodeError

from utils import open_json


@patch("utils.open", new_callable=mock_open)
@patch("utils.json.load")
def test_successful_load(mock_json_load, mock_file):
    """success test"""
    test_data = [{"id": 1, "name": "Alice"}]
    mock_json_load.return_value = test_data

    result = open_json("valid.json")

    assert result == test_data
    mock_file.assert_called_once_with("valid.json", "r", encoding="utf-8")
    mock_json_load.assert_called_once()


@patch("utils.open")
def test_file_not_found(mock_file):
    """Non-exist file test"""
    mock_file.side_effect = FileNotFoundError

    result = open_json("missing.json")

    assert result == []
    mock_file.assert_called_once_with("missing.json", "r", encoding="utf-8")


@patch("utils.open", new_callable=mock_open)
@patch("utils.json.load")
def test_json_decode_error(mock_json_load, mock_file):
    """incorrect JSON test"""
    mock_json_load.side_effect = JSONDecodeError("Error", "doc", 0)

    result = open_json("invalid.json")

    assert result == []
    mock_file.assert_called_once_with("invalid.json", "r", encoding="utf-8")
    mock_json_load.assert_called_once()