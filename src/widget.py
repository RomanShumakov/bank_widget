from masks import get_mask_account, get_mask_card_number


def mask_account_card(card: str) -> str:
    """Функция обработки информации как о картах, так и о счетах"""
    splited_card = card.split()
    words_list = []
    for word in splited_card:
        if word.isdigit() and len(word) == 16:
            word = get_mask_card_number(int(word))
        if word.isdigit() and len(word) == 20:
            word = get_mask_account(int(word))

        words_list.append(word)
    masked_card = " ".join(words_list)
    return masked_card


def get_date(date: str) -> str:
    """Функция изменения формата даты"""

    inverted_date = date[:10].split("-")
    formated_date = f"{inverted_date[2]}.{inverted_date[1]}.{inverted_date[0]}"
    return formated_date
