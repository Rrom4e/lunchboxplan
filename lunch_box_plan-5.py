# === Stage 5: Удаление и восстановление ===
# Project: LunchBoxPlan
import copy


class LunchBoxPlan:
    def __init__(self):
        self._lunches = {}

    def add_lunch(self, name, day, calories, cooking_time):
        self._lunches[(day, name)] = {
            'name': name,
            'day': day,
            'calories': calories,
            'cooking_time': cooking_time,
            'soft_deleted': False,
        }

    def get_lunch(self, day, name):
        return self._lunches.get((day, name))

    def delete_lunch(self, day, name):
        key = (day, name)
        if key not in self._lunches:
            raise KeyError(f'Lunch {name} on {day} not found')

        existing = self._lunches[key]
        if existing['soft_deleted']:
            existing['soft_deleted'] = False
            return

        self._soft_deleted[key] = copy.deepcopy(existing)
        del self._lunches[key]

    def restore_lunch(self, day, name):
        key = (day, name)
        if key in self._soft_deleted:
            self._lunches[key] = copy.deepcopy(self._soft_deleted.pop(key))
        else:
            raise KeyError(f'Lunch {name} on {day} is not soft-deleted')

    def list_lunches(self):
        return [
            lunch for lunch in self._lunches.values()
            if not lunch['soft_deleted']
        ]

    def list_soft_deleted(self):
        return copy.deepcopy(self._soft_deleted)


soft_deleted_store = {}


def make_planner():
    return LunchBoxPlan()


def demo():
    planner = make_planner()
    planner.add_lunch('Салат', 'Понедельник', 350, 15)
    planner.add_lunch('Курица', 'Вторник', 480, 25)
    planner.delete_lunch('Понедельник', 'Салат')
    print('Остались:', planner.list_lunches())
    print('В корзине:', planner.list_soft_deleted())
    planner.restore_lunch('Понедельник', 'Салат')
    print('После восстановления:', planner.list_lunches())


if __name__ == '__main__':
    demo()
