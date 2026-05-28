import csv
import os

import pandas as pd


def csv_reader(
    path_to_file: str = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data/transactions.csv"))
) -> list[dict]:
    """Функция для считывания финансовых операций из CSV"""
    with open(path_to_file, encoding='utf-8') as file:
        reader = csv.DictReader(file)
        return list(reader)


def excel_reader(
    path_to_file: str = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data/transactions_excel.xlsx"))
) -> list[dict]:
    """Функция для считывания финансовых операций из Excel"""
    excel_data = pd.read_excel(path_to_file)
    return excel_data.to_dict(orient="records")
