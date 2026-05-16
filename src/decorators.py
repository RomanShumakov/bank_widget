from functools import wraps
from time import time
from typing import Any, Callable


def log(filename: str | None = None) -> Callable:
    """Декоратор для вывода логов с результатами работы функции в консоль или файл"""

    def wrapper(func: Callable) -> Callable:
        @wraps(func)
        def inner(*args: Any, **kwargs: Any) -> Any:
            time_begin = time()
            error_message = None
            try:
                result = func(*args, **kwargs)
            except Exception as e:
                error_message = f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}"
                result = None

            time_end = time()
            if not filename and not error_message:
                print(
                    f"Функция {func.__name__} успешно завершила выполнение за {time_end - time_begin} сек.: {result}"
                )
            elif not filename and error_message:
                print(f"{error_message}. Время выполнения: {time_end - time_begin}")
            elif filename and not error_message:
                with open(filename, "a", encoding="utf-8") as file:
                    file.write(
                        f"Функция {func.__name__} успешно завершила выполнение за "
                        f"{time_end - time_begin} сек.: {result}" + "\n"
                    )
            elif filename and error_message:
                with open(filename, "a", encoding="utf-8") as file:
                    file.write(f"{error_message}. Время выполнения: {time_end - time_begin}" + "\n")

            return result

        return inner

    return wrapper
