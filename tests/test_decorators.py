import pytest

from src.decorators import log

@log()
def my_function():
    return "result"

@log()
def error_function():
    raise ValueError("something went wrong...")


def test_log_console_output(capsys):
    my_function()
    captured = capsys.readouterr()
    assert "Функция my_function успешно завершила выполнение за" in captured.out
    assert "result" in captured.out

def test_log_console_error(capsys):
    error_function()
    captured = capsys.readouterr()
    assert "error_function error: ValueError. Inputs: (), {}" in captured.out
    assert "Время выполнения:" in captured.out