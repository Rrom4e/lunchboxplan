# === Stage 7: Связи между сущностями ===
# Project: LunchBoxPlan
from datetime import date, datetime
from dataclasses import dataclass, field
from typing import Dict, List, Optional


@dataclass
class Dish:
    name: str
    calories: int
    cook_time: int


@dataclass
class Meal:
    name: str
    day: date
    calories: int
    cook_time: int


@dataclass
class MealPlan:
    _meals: Dict[str, List[Dish]] = field(default_factory=dict)

    def add_dish(self, meal: Meal, dish: Dish) -> None:
        self._meals.setdefault(meal.name, []).append(dish)

    def get_dishes(self, meal: Meal) -> List[Dish]:
        return list(self._meals.get(meal.name, []))


def check_integrity(meal: Meal, plan: MealPlan) -> List[str]:
    missing = []
    if not isinstance(meal, Meal):
        missing.append("meal не является объектом Meal")
    if not isinstance(plan, MealPlan):
        missing.append("plan не является объектом MealPlan")
    if meal.day is None:
        missing.append("у обеда отсутствует день")
    if meal.calories <= 0:
        missing.append("калорийность обеда некорректна")
    if meal.cook_time < 0:
        missing.append("время готовки некорректно")
    if not plan.get_dishes(meal):
        missing.append("обеду не назначено ни одного блюда")
    return missing


def validate_dishes(meal: Meal, dishes: List[Dish]) -> List[str]:
    errors = []
    if not isinstance(dishes, list):
        errors.append("блюда должны быть списком")
        return errors
    for dish in dishes:
        if not isinstance(dish, Dish):
            errors.append(f"блюдо не является объектом Dish: {dish!r}")
            continue
        if not dish.name:
            errors.append(f"у блюда отсутствует название")
        if dish.calories <= 0:
            errors.append(f"калорийность блюда некорректна: {dish.name}")
        if dish.cook_time < 0:
            errors.append(f"время готовки блюда некорректно: {dish.name}")
        if meal.calories < sum(d.calories for d in dishes):
            errors.append(
                "суммарная калорийность блюд превышает калорийность обеда"
            )
    return errors
