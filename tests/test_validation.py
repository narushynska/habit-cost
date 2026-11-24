# test_validation.py — перевіряємо validate без браузера.
# Запуск з папки проєкту: python -m pytest -q

import pandas as pd

from app.validation import validate


def test_good_file():
    df = pd.DataFrame({"назва": ["кава з собою"], "ціна_грн": [80]})
    assert validate(df) == []


def test_semicolon_file():
    # файл із «;» pandas читає одним стовпцем
    df = pd.DataFrame({"назва;ціна_грн": ["кава;80"]})
    assert validate(df) == ["Немає колонок: назва, ціна_грн"]


def test_empty_file():
    df = pd.DataFrame(columns=["назва", "ціна_грн"])
    assert validate(df) == ["Файл не містить рядків"]
