# === Stage 8: Генерация идентификаторов ===
# Project: LunchBoxPlan
PREFIX = "LBP"


def generate_id(name: str) -> str:
    """Формирует уникальный идентификатор с префиксом проекта.

    Идентификатор строится из префикса и хэша входного названия,
    затем проверяется на коллизии и при необходимости догружается
    суффиксом индекса.
    """
    base = f"{PREFIX}-{name}".lower().replace(" ", "_")
    candidate = f"{base}-{abs(hash(name)) % 100000:05d}"
    counter = 1
    while candidate in generate_id._ids:
        candidate = f"{base}-{abs(hash(name)) % 100000:05d}-{counter:03d}"
        counter += 1
    generate_id._ids.add(candidate)
    return candidate


generate_id._ids = set()
