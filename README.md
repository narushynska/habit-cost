# Скільки коштує моя звичка

Ви обираєте звичку (кава з собою, таксі, доставка їжі) і кажете, скільки разів на тиждень це робите.
Програма рахує, скільки грошей на це йде за тиждень, місяць і рік, і на які мрії вистачило б цих грошей.
Дані вигадані для навчання.

Дві «вітрини» для однієї логіки:

- **сторінка в браузері** — `streamlit_app.py` (заняття 6);
- **версія в терміналі** — `main.py` (приклад «Програма з нуля»).

**Онлайн-версія:** [https://habit-cost-demo.streamlit.app](https://habit-cost-demo.streamlit.app)

## Як запустити

```bash
git clone https://github.com/narushynska/habit-cost.git
cd habit-cost
python -m venv .venv
.venv\Scripts\activate          # macOS: source .venv/bin/activate
python -m pip install -r requirements.txt
streamlit run streamlit_app.py  # сторінка в браузері
python main.py                  # версія в терміналі
```

## Тести

```bash
python -m pytest -q
```

Очікувано: `8 passed`.

## Приклад результату

Кава з собою, 7 разів на тиждень: **560 грн** за тиждень, **2427 грн** за місяць, **29120 грн** за рік.
За рік на ці гроші можна було б: квитки на потяг до моря для двох, велосипед дитині,
курс англійської на рік, вихідні в Карпатах для сім'ї.

Щоб побачити повідомлення про помилку, завантажте на сторінці `data/bad.csv`.

## Як опублікувати свою копію

1. Репозиторій на GitHub — **Public**, у корені є `streamlit_app.py` і `requirements.txt`.
2. [share.streamlit.io](https://share.streamlit.io) → **Continue with GitHub** → **Create app** → **Deploy a public app from GitHub**.
3. Repository: `ваш-логін/habit-cost`, Branch: `main`, Main file path: `streamlit_app.py`.
4. **Deploy** → 1–3 хвилини → посилання `https://….streamlit.app`. Кожен `git push` оновлює застосунок.

## Структура

```
habit-cost/
├── streamlit_app.py   сторінка Streamlit
├── main.py            версія в терміналі
├── app/               пакет з логікою
│   ├── config.py      шляхи до файлів (від Path(__file__))
│   ├── data_loader.py читання CSV
│   ├── calculator.py  розрахунки
│   ├── validation.py  перевірка таблиці, яку дала людина
│   └── report.py      текст звіту для терміналу
├── data/              звички, мрії, bad.csv для перевірки помилки
├── tests/             тести pytest
├── requirements.txt   streamlit, pandas, pytest
└── .gitignore
```
