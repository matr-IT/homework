import pytest

from src.search import process_bank_operations, process_bank_search


def test_search_existing_keyword(sample_operations):
    """success test"""
    result = process_bank_search(sample_operations, "Sberbank")
    assert len(result) == 2
    assert result[0]["id"] == 1
    assert result[1]["id"] == 6


def test_search_nonexistent_keyword(sample_operations):
    """non-existing keyword"""
    result = process_bank_search(sample_operations, "Gazprom")
    assert result == []


def test_empty_search(sample_operations):
    """empty keyword"""
    result = process_bank_search(sample_operations, "")
    assert result == sample_operations


def test_process_bank_operations_success(sample_operations):
    """success test"""
    categories = ["Sberbank", "VTB", "Alfa-Bank", "Tinkoff"]
    result = process_bank_operations(sample_operations, categories)

    assert result == {"Sberbank": 2, "VTB": 1, "Alfa-Bank": 1, "Tinkoff": 1}


def test_process_bank_operations_case_insensitivity(sample_operations):
    """case test"""
    categories = ["sberbank", "vtb", "ALFA-BANK", "tInKoFf"]
    result = process_bank_operations(sample_operations, categories)

    assert result == {"sberbank": 2, "vtb": 1, "ALFA-BANK": 1, "tInKoFf": 1}


def test_process_bank_operations_empty_operations_list():
    """empty operations test"""
    result = process_bank_operations([], ["Sberbank"])
    assert result == {}
