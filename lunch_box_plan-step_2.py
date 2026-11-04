# === Stage 2: Проверка полей ===
# Project: LunchBoxPlan
import datetime


def normalize_day(day: str) -> str:
    day = day.strip().lower()
    aliases = {
        'пн': 'понедельник',
        'пн.': 'понедельник',
        'вт': 'вторник',
        'вт.': 'вторник',
        'ср': 'среда',
        'ср.': 'среда',
        'чт': 'четверг',
        'чт.': 'четверг',
        'пт': 'пятница',
        'пт.': 'пятница',
        'сб': 'суббота',
        'сб.': 'суббота',
        'вс': 'воскресенье',
        'вс.': 'воскресенье',
        'понедельник': 'понедельник',
        'вторник': 'вторник',
        'среда': 'среда',
        'четверг': 'четверг',
        'пятница': 'пятница',
        'суббота': 'суббота',
        'воскресенье': 'воскресенье',
    }
    return aliases.get(day, day)


def normalize_time(cook_time: str) -> datetime.time:
    cook_time = cook_time.strip()
    for fmt in ('%H:%M', '%H:%M:%S', '%H.%M'):
        try:
            return datetime.time.strptime(cook_time, fmt)
        except ValueError:
            continue
    raise ValueError('Время готовки должно быть в формате ЧЧ:ММ, например 13:30')


def normalize_name(name: str) -> str:
    name = name.strip()
    return name


def normalize_calories(calories: str) -> int:
    try:
        value = int(str(calories).strip())
        if value <= 0:
            raise ValueError('Калорийность должна быть положительным числом')
        return value
    except ValueError:
        raise ValueError('Калорийность должна быть целым числом больше нуля')


def validate_lunch(lunch: dict) -> None:
    name = lunch.get('название')
    day = lunch.get('день')
    calories = lunch.get('калории')
    cook_time = lunch.get('время готовки')

    if not name or not name.strip():
        raise ValueError('Название обеду обязательно')

    if not day or not day.strip():
        raise ValueError('Укажите день обёма')
    normalized_day = normalize_day(day)
    if normalized_day not in (
        'понедельник', 'вторник', 'среда', 'четверг', 'пятница',
        'суббота', 'воскресенье',
    ):
        raise ValueError('День должен быть одним из: пн, вт, ср, чт, пт, сб, вс')

    if calories is None:
        raise ValueError('Укажите калорийность обёма')
    normalized_calories = normalize_calories(calories)

    if cook_time is None:
        raise ValueError('Укажите время готовки обёма')
    normalized_time = normalize_time(cook_time)

    lunch['название'] = name.strip()
    lunch['день'] = normalized_day
    lunch['калории'] = normalized_calories
    lunch['время готовки'] = normalized_time
