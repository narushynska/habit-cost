# validation.py — перевіряємо таблицю, яку дала людина.
# Тут немає st.: функцію можна перевірити тестом без браузера.

REQUIRED_COLUMNS = ["назва", "ціна_грн"]


def validate(df):
    """Повертає список проблем; [] — файл у порядку."""
    problems = []
    missing = [c for c in REQUIRED_COLUMNS if c not in df.columns]
    if missing:
        problems.append("Немає колонок: " + ", ".join(missing))
        return problems
    if df.empty:
        problems.append("Файл не містить рядків")
    return problems
