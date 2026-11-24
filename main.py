# main.py — точка входу. Запуск з папки проєкту: python main.py
# main.py лише з'єднує частини: дані -> розрахунки -> звіт.

from app.calculator import cost_per_month, cost_per_week, cost_per_year, dreams_i_can_afford
from app.config import DREAMS_FILE, HABITS_FILE
from app.data_loader import load_prices
from app.report import make_report


def ask_number(question):
    """Питає число, доки людина не введе правильне."""
    while True:
        answer = input(question)
        try:
            return int(answer)
        except ValueError:
            print("Будь ласка, введіть ціле число, наприклад 5.")


def main():
    # 1. Читаємо дані. Якщо файлу немає — пояснюємо людською мовою.
    try:
        habits = load_prices(HABITS_FILE)
        dreams = load_prices(DREAMS_FILE)
    except FileNotFoundError:
        print("Не знайдено файлів у папці data. Перевірте, що вони на місці.")
        return

    # 2. Показуємо список звичок з номерами
    print("СКІЛЬКИ КОШТУЄ МОЯ ЗВИЧКА\n")
    names = list(habits)
    for number, name in enumerate(names, start=1):
        print(f"{number}. {name} — {habits[name]} грн")

    # 3. Питаємо, що обрала людина
    choice = ask_number("\nОберіть номер звички: ")
    if choice < 1 or choice > len(names):
        print("Такого номера немає в списку.")
        return
    habit = names[choice - 1]  # у списку рахуємо з 0, тому віднімаємо 1
    times = ask_number("Скільки разів на тиждень? ")

    # 4. Рахуємо
    price = habits[habit]
    week = cost_per_week(price, times)
    month = cost_per_month(price, times)
    year = cost_per_year(price, times)
    affordable = dreams_i_can_afford(dreams, year)

    # 5. Друкуємо звіт
    print()
    print(make_report(habit, times, week, month, year, affordable))


# Цей рядок запускає main(), лише коли ми запускаємо саме цей файл
if __name__ == "__main__":
    main()
