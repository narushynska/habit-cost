# calculator.py — усі розрахунки.
# Тут немає print і input: функції лише рахують і повертають результат.
# Тому їх легко перевірити тестами.

from app.config import WEEKS_IN_YEAR


def cost_per_week(price, times_per_week):
    """Скільки коштує звичка за тиждень."""
    return price * times_per_week


def cost_per_year(price, times_per_week):
    """Скільки коштує звичка за рік."""
    return price * times_per_week * WEEKS_IN_YEAR


def cost_per_month(price, times_per_week):
    """Скільки коштує звичка за місяць: рік ділимо на 12 і округлюємо."""
    return round(cost_per_year(price, times_per_week) / 12)


def dreams_i_can_afford(dreams, money):
    """Повертає список мрій, на які вистачає грошей."""
    affordable = []
    for name, price in dreams.items():
        if price <= money:
            affordable.append(name)
    return affordable
