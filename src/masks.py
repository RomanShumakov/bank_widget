import logging
import os

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    filename=os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "logs/masks.log")),
    filemode="w",
    encoding="utf-8",
)

app_logger = logging.getLogger(__name__)


def get_mask_card_number(card_num: str) -> str:
    """Функция маскировки номера банковской карты"""
    app_logger.info("Начало работы функции маскировки банковской карты")
    if len(card_num) != 16:
        app_logger.critical("Неправильно введен номер банковской карты. Остановка работы.")
        raise ValueError("Неправильно введен номер банковской карты")
    app_logger.info("Маскировка банковской карты успешно завершена")

    return card_num[:4] + " " + card_num[4:6] + "** **** " + card_num[-4:]


def get_mask_account(card_id: str) -> str:
    """Функция маскировки номера банковского счета"""

    app_logger.info("Начало работы функции маскировки банковского счета")
    if len(card_id) != 20:
        app_logger.critical("Неправильно введен номер банковского счета. Остановка работы.")
        raise ValueError("Неправильно введен номер банковского счета")
    app_logger.info("Маскировка банковского счета успешно завершена")
    return "**" + card_id[-4:]
