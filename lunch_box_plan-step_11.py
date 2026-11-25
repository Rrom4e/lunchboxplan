# === Stage 11: Текстовый поиск ===
# Project: LunchBoxPlan
def highlight_matches(text, needle):
    text = str(text)
    needle = str(needle)
    if not needle:
        return text
    lowered = text.lower()
    needle_lower = needle.lower()
    start = 0
    parts = []
    index = 0
    while True:
        pos = lowered.find(needle_lower, index)
        if pos == -1:
            parts.append(text[start:])
            break
        parts.append(text[start:pos])
        parts.append('\033[7m' + text[pos:pos + len(needle)] + '\033[0m')
        start = pos + len(needle)
        index = start
    return ''.join(parts)


def find_lunch_by_text(lunches, needle):
    needle = str(needle).strip()
    if not needle:
        return []
    results = []
    for lunch in lunches:
        fields = [
            str(getattr(lunch, 'name', '')),
            str(getattr(lunch, 'day', '')),
            str(getattr(lunch, 'cooking_time', '')),
        ]
        if any(highlight_matches(field, needle) for field in fields):
            results.append(lunch)
    return results


if __name__ == '__main__':
    sample = [
        {'name': 'Гречка с курицей', 'day': 'Понедельник', 'cooking_time': '20 мин'},
        {'name': 'Салат Цезарь', 'day': 'Среда', 'cooking_time': '15 мин'},
        {'name': 'Овощной суп', 'day': 'Пятница', 'cooking_time': '30 мин'},
    ]
    query = 'сред'
    print('Результаты поиска по:', query)
    for match in find_lunch_by_text(sample, query):
        print('Название:', highlight_matches(match['name'], query))
        print('День:', highlight_matches(match['day'], query))
        print('Готовка:', highlight_matches(match['cooking_time'], query))
        print('---')
