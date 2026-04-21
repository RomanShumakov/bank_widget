from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card: int | str) -> str:
    """Функция обработки информации как о картах, так и о счетах"""
    card = str(card)
    splited_card = card.rsplit(" ", maxsplit=1)
    words_list = []
    for word in splited_card:
        if word.isdigit() and len(word) == 16:
            word = get_mask_card_number(word)
        elif word.isdigit() and len(word) == 20:
            word = get_mask_account(word)

        words_list.append(word)
    masked_card = " ".join(words_list)
    return masked_card


def get_date(date: str) -> str:
    """Функция изменения формата даты"""

    inverted_date = date[:10].split("-")
    if any(not part.isdigit() for part in inverted_date[:3]):
        raise ValueError("Недопустимый формат ввода")

    if not (1 <= int(inverted_date[2]) <= 31) or not (1 <= int(inverted_date[1]) <= 12) or len(inverted_date[0]) != 4:
        raise ValueError("Недопустимае данные для даты")
    formated_date = f"{inverted_date[2]}.{inverted_date[1]}.{inverted_date[0]}"
    return formated_date
