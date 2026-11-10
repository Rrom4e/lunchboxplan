# === Stage 4: Редактирование записей ===
# Project: LunchBoxPlan
def can_update_lunch(lunch, allowed_fields):
    """Проверяет, что переданный набор полей подмножество допустимых."""
    if not isinstance(allowed_fields, dict):
        return False
    return all(key in lunch for key in allowed_fields)


def validate_editable_lunch(lunch, allowed_fields):
    """Возвращает True, если обед существует и все поля для изменения допустимы."""
    if not can_update_lunch(lunch, allowed_fields):
        return False
    return True


def update_lunch(lunches, lunch_id, allowed_fields):
    """Редактирует обед по id, меняя только допустимые поля.

    lunches - словарь идентификаторов обедов в значения.
    lunch_id - идентификатор обeda для изменения.
    allowed_fields - словарь с новыми значениями полей обeda.
    """
    if not validate_editable_lunch(lunches, lunch_id, allowed_fields):
        raise KeyError(f"Обед {lunch_id} не найден или поля для изменения недопустимы")

    for key, value in allowed_fields.items():
        if key in ("название", "день", "калории", "время готовки"):
            lunches[lunch_id][key] = value
        else:
            raise ValueError(f"Поле '{key}' не является допустимым полем обeda")

    return lunches[lunch_id]


def edit_lunch_by_id(lunches, lunch_id, allowed_fields):
    """Удобная обёртка для редактирования обeda по id с проверкой допустимых полей."""
    if not validate_editable_lunch(lunches, lunch_id, allowed_fields):
        raise KeyError(f"Обед {lunch_id} не найден")

    for key, value in allowed_fields.items():
        if key not in ("название", "день", "калории", "время готовки"):
            raise ValueError(f"Поле '{key}' нельзя изменить")

    for key, value in allowed_fields.items():
        lunches[lunch_id][key] = value

    return lunches[lunch_id]


def get_editable_fields(lunch):
    """Возвращает список допустимых полей обeda для редактирования."""
    return ["название", "день", "калории", "время готовки"]


def is_valid_lunch_update(lunch, allowed_fields):
    """Проверяет валидность обновления обeda: наличие обeda и допустимость полей."""
    valid_fields = get_editable_fields(lunch)
    if not isinstance(allowed_fields, dict):
        return False
    return all(field in valid_fields for field in allowed_fields)
