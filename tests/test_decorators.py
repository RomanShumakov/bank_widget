from pytest import CaptureFixture

from src.decorators import log


@log()
def my_function() -> str:
    """Объявление декорированной функции для тестирования декоратора log на вывод результатов работы в консоль"""
    return "result"


def test_log_console_output(capsys: CaptureFixture) -> None:
    """Тестирование декоратора log при выводе результатов успешной работы my_function в консоль"""
    my_function()
    captured = capsys.readouterr()
    assert "Функция my_function успешно завершила выполнение за" in captured.out
    assert "result" in captured.out


@log()
def error_function() -> None:
    """Объявление декорированной функции для тестирования декоратора log на вывод ошибки в консоль"""
    raise ValueError("something went wrong...")


def test_log_console_error(capsys: CaptureFixture) -> None:
    """Тестирование декоратора log при выводе ошибки в консоль"""
    error_function()
    captured = capsys.readouterr()
    assert "error_function error: ValueError. Inputs: (), {}" in captured.out
    assert "Время выполнения:" in captured.out


@log(filename="tempfile.txt")
def test_function() -> str:
    """Объявление декорированной функции для тестирования декоратора log
    на вывод результатов успешной работы в txt-файл"""
    return "test result 45"


def test_log_file_output() -> None:
    """Тестирование декоратора log на вывод результатов успешной работы test_function в txt-файл"""
    test_function()
    with open("tempfile.txt", "r", encoding="utf-8") as file:
        content = file.read().encode("utf-8")
        assert "test result 45" in str(content)


@log(filename="tempfile.txt")
def test_error_function() -> None:
    """Объявление декорированной функции для тестирования декоратора log на вывод ошибки в txt-файл"""
    raise ValueError("something went wrong...")


def test_log_file_error() -> None:
    """Тестирование декоратора log на вывод ошибки в txt-файл"""
    test_error_function()
    with open("tempfile.txt", "r", encoding="utf-8") as file:
        content = file.read().encode("utf-8")
        assert "test_error_function error:" in str(content)
