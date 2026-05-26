import csv
import pandas as pd
import os

def csv_reader(path_to_file:str = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data/transactions.csv"))) -> list[dict]:
    """Функция для считывания финансовых операций из CSV"""
    with open(path_to_file) as file:
        reader = csv.DictReader(file)
    return list(reader)


