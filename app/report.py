# report.py — як результат побачить людина: збираємо текст звіту.


def make_report(habit, times_per_week, week, month, year, affordable):
    """Повертає готовий текст звіту."""
    lines = []
    lines.append(f"Звичка: {habit}, {times_per_week} раз(и) на тиждень")
    lines.append("-" * 40)
    lines.append(f"За тиждень: {week} грн")
    lines.append(f"За місяць:  {month} грн")
    lines.append(f"За рік:     {year} грн")
    lines.append("")

    if len(affordable) == 0:
        lines.append("Поки що грошей не вистачає на жодну мрію зі списку.")
    else:
        lines.append("За рік на ці гроші можна було б:")
        for dream in affordable:
            lines.append(f"  + {dream}")

    # "\n".join склеює всі рядки в один текст, кожен з нового рядка
    return "\n".join(lines)
