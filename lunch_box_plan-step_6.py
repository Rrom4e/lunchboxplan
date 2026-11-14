# === Stage 6: Связанная сущность ===
# Project: LunchBoxPlan
class Dish:
    def __init__(self, name, calories, prep_time):
        self.name = name
        self.calories = calories
        self.prep_time = prep_time

    def __str__(self):
        return f"{self.name} ({self.calories} ккал, {self.prep_time} мин)"


class Meal:
    def __init__(self, name, day, calories, prep_time):
        self.name = name
        self.day = day
        self.calories = calories
        self.prep_time = prep_time
        self.dishes = []

    def add_dish(self, dish):
        self.dishes.append(dish)

    def total_calories(self):
        return sum(dish.calories for dish in self.dishes)

    def total_prep_time(self):
        return sum(dish.prep_time for dish in self.dishes)

    def __str__(self):
        return f"{self.name} ({self.day}): {self.total_calories()} ккал, {self.total_prep_time()} мин"


def create_dish(name, calories, prep_time):
    return Dish(name, calories, prep_time)


def add_dish_to_meal(meal, name, calories, prep_time):
    dish = create_dish(name, calories, prep_time)
    meal.add_dish(dish)
    return dish


if __name__ == "__main__":
    lunch = Meal("Куриный салат", "Понедельник", 450, 20)
    add_dish_to_meal(lunch, "Курица", 250, 25)
    add_dish_to_meal(lunch, "Салат", 200, 10)
    print(lunch)
    print(f"Всего калорий: {lunch.total_calories()}")
    print(f"Всего времени готовки: {lunch.total_prep_time()} мин")
