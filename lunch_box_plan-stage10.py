# === Stage 10: Сортировка записей ===
# Project: LunchBoxPlan
from datetime import datetime


def sort_lunch_records(records, field_name="name", descending=False):
    """Сортирует список записей 'обед' по полю и дате создания.

    Args:
        records: список словарей, представляющих обеды.
        field_name: имя поля для первичной сортировки (по умолчанию 'name').
        descending: если True, сортировка по убыванию, иначе по возрастанию.

    Returns:
        новый список, отсортированный по заданным критериям.
    """
    key_func = lambda record: (
        record.get(field_name, ""),
        record.get("created_at", datetime.min),
    )
    return sorted(records, key=key_func, reverse=descending)


def sort_by_date_created(records, descending=False):
    """Сортирует обеды по дате создания.

    Args:
        records: список словарей, представляющих обеды.
        descending: если True, сортировка по убыванию, иначе по возрастанию.

    Returns:
        новый список, отсортированный по дате создания.
    """
    key_func = lambda record: (
        record.get("created_at", datetime.min),
        record.get("name", ""),
    )
    return sorted(records, key=key_func, reverse=descending)


if __name__ == "__main__":
    sample = [
        {"name": "Плов", "created_at": "2024-01-02T10:00:00"},
        {"name": "Гречка", "created_at": "2024-01-01T10:00:00"},
        {"name": "Овощной салат", "created_at": "2024-01-01T11:00:00"},
    ]
    print(sort_lunch_records(sample))
    print(sort_by_date_created(sample))
