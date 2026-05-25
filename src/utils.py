import json
import logging
import os
from json import JSONDecodeError

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    filename=os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "logs/utils.log")),
    filemode="w",
    encoding="utf-8",
)

utils_logger = logging.getLogger(__name__)


def json_reader(
    path_to_file: str = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data/operations.json"))
) -> list:
    """Функция чтения json-файлов"""
    utils_logger.info("Начало работы функции чтения json-файла")

    try:
        with open(path_to_file, encoding="utf-8") as f:
            response = json.load(f)
        if not isinstance(response, list):
            utils_logger.warning("json-файл пуст. Продолжение работы с пустым файлом.")
            return []
        utils_logger.info("json-файл успешно прочитан")
        return response

    except FileNotFoundError:
        utils_logger.error(
            f"json-файл не найден по указанному пути: {path_to_file}. Продолжение работы с пустым файлом."
        )
        return []
    except JSONDecodeError:
        utils_logger.error("json-файл поврежден или неправильно прочитан. Продолжение работы с пустым файлом.")
        return []
