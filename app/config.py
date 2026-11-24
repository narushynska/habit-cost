# config.py — налаштування: де лежать файли і сталі числа.

from pathlib import Path

# config.py лежить у папці app, тому корінь проєкту — на одну папку вище.
# Так програма знайде файли, звідки б її не запустили.
BASE_DIR = Path(__file__).resolve().parent.parent

HABITS_FILE = BASE_DIR / "data" / "habits.csv"
DREAMS_FILE = BASE_DIR / "data" / "dreams.csv"

# У році 52 тижні
WEEKS_IN_YEAR = 52
