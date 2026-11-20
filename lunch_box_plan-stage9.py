# === Stage 9: Фильтрация записей ===
# Project: LunchBoxPlan
from datetime import date


def filter_by_day(lunches, day):
    """Отбирает обеды, у которых поле 'день' равно указанному значению.

    lunches - список объектов, каждый из которых имеет атрибут 'day'.
    day - значение, по которому проводится фильтрация.
    Возвращает новый список с подходящими записями, исходный список не изменяется.
    """
    return [lunch for lunch in lunches if lunch.day == day]


def filter_by_date_range(lunches, start_date, end_date):
    """Отбирает обеды, чей день попадает в заданный диапазон дат (включительно).

    lunches - список объектов, каждый из которых имеет атрибут 'day'.
    start_date и end_date - объекты date, границы диапазона.
    Возвращает новый список с подходящими записями, исходный список не изменяется.
    """
    if start_date > end_date:
        start_date, end_date = end_date, start_date
    return [
        lunch
        for lunch in lunches
        if start_date <= lunch.day <= end_date
    ]


def group_by_day(lunches):
    """Группирует обеды по значению поля 'день'.

    lunches - список объектов с атрибутом 'day'.
    Возвращает словарь, где ключ - значение дня, а значение - список обедов этого дня.
    Порядок дней сохраняется в порядке первого появления в исходном списке.
    """
    grouped = {}
    order = []
    for lunch in lunches:
        if lunch.day not in grouped:
            grouped[lunch.day] = []
            order.append(lunch.day)
        grouped[lunch.day].append(lunch)
    return {day: grouped[day] for day in order}


def get_days_with_lunches(lunches):
    """Возвращает отсортированный список уникальных дней из списка обедов.

    lunches - список объектов с атрибутом 'day'.
    Дни сортируются по возрастанию.
    """
    return sorted({lunch.day for lunch in lunches})


def total_calories_by_day(lunches):
    """Суммирует калорийность обедов по каждому дню.

    lunches - список объектов с атрибутами 'day' и 'calories'.
    Возвращает словарь, где ключ - день, а значение - суммарная калорийность за день.
    """
    totals = {}
    for lunch in lunches:
        totals[lunch.day] = totals.get(lunch.day, 0) + lunch.calories
    return totals
