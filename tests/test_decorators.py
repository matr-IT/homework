from typing import Generator

import pytest

from src.decorators import log


def test_successful_console_logging(capsys):
    @log()
    def add(a, b):
        return a + b

    result = add(5, 3)
    captured = capsys.readouterr()

    assert result == 8
    assert captured.out.strip() == "add ok"


def test_error_console_logging(capsys):
    @log()
    def divide(a, b):
        return a / b

    with pytest.raises(ZeroDivisionError):
        divide(10, 0)

    captured = capsys.readouterr()
    assert captured.out.strip() == "divide error: ZeroDivisionError. Inputs: (10, 0), {}"