from unittest.mock import MagicMock, patch

import pandas as pd
import pytest

from src.read_csv_excel import read_csv, read_excel


@patch("src.read_csv_excel.pd.read_csv")
def test_read_csv_success(mock_read_csv, test_data_read):
    """successful test"""
    mock_df = MagicMock()
    mock_df.to_dict.return_value = test_data_read
    mock_read_csv.return_value = mock_df

    result = read_csv("data/transactions.csv")

    assert result == test_data_read
    mock_read_csv.assert_called_once_with("data/transactions.csv")
    mock_df.to_dict.assert_called_once_with(orient="records")


@patch("src.read_csv_excel.pd.read_csv")
def test_read_csv_empty(mock_read_csv):
    """empty-csv test"""
    mock_df = MagicMock()
    mock_df.to_dict.return_value = []
    mock_read_csv.return_value = mock_df

    result = read_csv("data/empty.csv")

    assert result == []
    mock_read_csv.assert_called_once_with("data/empty.csv")
    mock_df.to_dict.assert_called_once_with(orient="records")


@patch("src.read_csv_excel.pd.read_csv")
def test_read_csv_error(mock_read_csv):
    """FileNotFound test"""
    mock_read_csv.side_effect = FileNotFoundError("File not found")

    with pytest.raises(FileNotFoundError) as exc_info:
        read_csv("data/missing.csv")

    assert "File not found" in str(exc_info.value)
    mock_read_csv.assert_called_once_with("data/missing.csv")


@patch("src.read_csv_excel.pd.read_excel")
def test_read_excel_success(mock_read_excel, test_data_read):
    """successful test"""
    mock_df = MagicMock()
    mock_df.to_dict.return_value = test_data_read
    mock_read_excel.return_value = mock_df

    result = read_excel("data/transactions_excel.xlsx")

    assert result == test_data_read
    mock_read_excel.assert_called_once_with("data/transactions_excel.xlsx")
    mock_df.to_dict.assert_called_once_with(orient="records")


@patch("src.read_csv_excel.pd.read_excel")
def test_read_excel_error(mock_read_excel):
    """ValueError test"""
    mock_read_excel.side_effect = ValueError("Invalid Excel file")

    with pytest.raises(ValueError) as exc_info:
        read_excel("data/corrupted.xlsx")

    assert "Invalid Excel file" in str(exc_info.value)
    mock_read_excel.assert_called_once_with("data/corrupted.xlsx")
