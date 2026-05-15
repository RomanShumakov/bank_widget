from time import time
from functools import wraps


def log(filename=None):
    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            time_begin = time()
            error_message = None
            try:
                result = func(*args, **kwargs)
            except Exception as e:
                error_message = f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}"
                result = None

            time_end = time()
            if not filename and not error_message:
                print(f"Функция {func.__name__} успешно завершила выполнение за {time_end - time_begin} сек.: {result}")
            elif not filename and error_message:
                print(f"{error_message}. Время выполнения: {time_end - time_begin}")
            elif filename and not error_message:
                with open(filename, "a") as file:
                    file.write(f"Функция {func.__name__} успешно завершила выполнение за {time_end - time_begin} сек.: {result}" + "\n")
            else:
                with open(filename, "a") as file:
                    file.write(f"{error_message}. Время выполнения: {time_end - time_begin}" + "\n")

            return result
        return inner
    return wrapper
