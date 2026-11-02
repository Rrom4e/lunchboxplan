# === Stage 1: Каркас модуля ===
# Project: LunchBoxPlan
from dataclasses import dataclass, field
from datetime import date


@dataclass
class Obed:
    """Обед с собой за день."""
    название: str
    день: date
    калории: int
    время_готовки: str


def make_demo_obedy() -> list[Obed]:
    """Создание демонстрационных записей обёдов."""
    return [
        Obed("Куриный салат", date(2024, 1, 1), 420, "20 минут"),
        Obed("Гречка с рыбой", date(2024, 1, 2), 510, "35 минут"),
        Obed("Овощной суп", date(2024, 1, 3), 330, "25 минут"),
    ]


def main() -> None:
    obedy = make_demo_obedy()
    for обед in obedy:
        print(f"{обед.день} — {обед.название}, "
              f"готовка {обед.время_готовки}, {обед.калории} ккал")


if __name__ == "__main__":
    main()
