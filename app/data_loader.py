# data_loader.py — читаємо дані з CSV-файлів.
# Тільки цей файл знає, що дані лежать саме в CSV.

import csv


def load_prices(path):
    """Читає CSV зі стовпцями «назва» і «ціна_грн».

    Повертає словник, наприклад: {"кава з собою": 80, "таксі": 200}
    """
    prices = {}
    with open(path, encoding="utf-8") as file:
        # DictReader читає кожен рядок як словник: {"назва": ..., "ціна_грн": ...}
        for row in csv.DictReader(file):
            name = row["назва"]
            price = int(row["ціна_грн"])  # з тексту "80" робимо число 80
            prices[name] = price
    return prices
