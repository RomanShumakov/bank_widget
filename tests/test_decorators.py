import pytest
import tempfile
import os

from src.decorators import log

@log()
def my_function():
    return "result"

def test_log_console_output(capsys):
    my_function()
    captured = capsys.readouterr()
    assert "Функция my_function успешно завершила выполнение за" in captured.out
    assert "result" in captured.out

@log()
def error_function():
    raise ValueError("something went wrong...")

def test_log_console_error(capsys):
    error_function()
    captured = capsys.readouterr()
    assert "error_function error: ValueError. Inputs: (), {}" in captured.out
    assert "Время выполнения:" in captured.out


@log(filename="tempfile.txt")
def test_function():
    return "test result 45"

def test_log_file_output():
    test_function()
    with open("tempfile.txt", "r", encoding='utf-8') as file:
        content = file.read().encode('utf-8')
        assert "test result 45" in str(content)


@log(filename="tempfile.txt")
def test_error_function():
    raise ValueError("something went wrong...")

def test_log_file_error():
    test_error_function()
    with open("tempfile.txt", "r", encoding='utf-8') as file:
        content = file.read().encode('utf-8')
        assert "test_error_function error:" in str(content)
