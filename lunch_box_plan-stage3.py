# === Stage 3: Хранилище в памяти ===
# Project: LunchBoxPlan
import uuid


class LunchBox:
    def __init__(self, name):
        self.id = uuid.uuid4().hex
        self.name = name
        self._meals = {}

    def add_meal(self, meal):
        self._meals[meal.id] = meal

    def get_meal(self, meal_id):
        return self._meals.get(meal_id)

    def list_meals(self):
        return list(self._meals.values())


class Meal:
    def __init__(self, name, dish, calories, cook_time):
        self.id = uuid.uuid4().hex
        self.name = name
        self.dish = dish
        self.calories = calories
        self.cook_time = cook_time


if __name__ == "__main__":
    lunch = LunchBox("Обеды")
    lunch.add_meal(Meal("Салат", "Салат Цезарь", 350, 15))
    lunch.add_meal(Meal("Суп", "Суп с овощами", 280, 20))
    for meal in lunch.list_meals():
        print(f"{meal.name} - {meal.calories} ккал")
        print(f"  Блюдо: {meal.dish}, Время: {meal.cook_time} мин")
        print(f"  ID: {meal.id}")
        print()
