# streamlit_app.py — сторінка в браузері для програми «Скільки коштує моя звичка».
# Запуск з папки проєкту: streamlit run streamlit_app.py
# Логіку не переписуємо: беремо її з пакета app/, як і main.py.

import pandas as pd
import streamlit as st

from app.calculator import cost_per_month, cost_per_week, cost_per_year, dreams_i_can_afford
from app.config import DREAMS_FILE, HABITS_FILE
from app.data_loader import load_prices
from app.validation import validate

st.set_page_config(page_title="Моя звичка", layout="wide")
st.title("Скільки коштує моя звичка")
st.caption("Оберіть звичку і як часто ви це робите: побачите, скільки це коштує "
           "за тиждень, місяць і рік і на яку мрію вистачило б цих грошей.")

uploaded = st.sidebar.file_uploader("Свій CSV зі звичками", type="csv")
if uploaded is not None:
    df = pd.read_csv(uploaded)
else:
    df = pd.read_csv(HABITS_FILE)
    st.info("Файл не завантажено, показано приклад data/habits.csv")

problems = validate(df)
if problems:
    for p in problems:
        st.error(p)
    st.stop()

st.sidebar.header("Моя звичка")
habit = st.sidebar.selectbox("Звичка", df["назва"])
times = st.sidebar.slider("Разів на тиждень", 0, 14, 7)

row = df[df["назва"] == habit]
price = int(row["ціна_грн"].iloc[0])
year = cost_per_year(price, times)
c1, c2, c3 = st.columns(3)
c1.metric("За тиждень, грн", cost_per_week(price, times))
c2.metric("За місяць, грн", cost_per_month(price, times))
c3.metric("За рік, грн", year)

st.subheader("За рік на ці гроші можна було б")
affordable = dreams_i_can_afford(load_prices(DREAMS_FILE), year)
if not affordable:
    st.warning("Поки грошей не вистачає на жодну мрію зі списку.")
for dream in affordable:
    st.success(dream)

st.dataframe(df)
st.bar_chart(df, x="назва", y="ціна_грн")
