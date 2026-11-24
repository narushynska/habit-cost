# test_calculator.py — перевіряємо розрахунки.
# Запуск з папки проєкту: python -m pytest -q

from app.calculator import cost_per_month, cost_per_year, dreams_i_can_afford
from app.config import HABITS_FILE
from app.data_loader import load_prices


def test_coffee_every_day():
    # кава за 80 грн 7 разів на тиждень: 80 * 7 * 52 = 29120 грн за рік
    assert cost_per_year(80, 7) == 29120


def test_month_is_rounded():
    # 29120 / 12 = 2426,67 -> округлюємо до 2427
    assert cost_per_month(80, 7) == 2427


def test_no_habit_costs_nothing():
    # 0 разів на тиждень = 0 грн
    assert cost_per_year(80, 0) == 0


def test_dreams_i_can_afford():
    dreams = {"квитки": 3000, "ноутбук": 35000}
    # на 5000 грн вистачає лише на квитки
    assert dreams_i_can_afford(dreams, 5000) == ["квитки"]


def test_prices_from_file():
    habits = load_prices(HABITS_FILE)
    assert habits["кава з собою"] == 80
