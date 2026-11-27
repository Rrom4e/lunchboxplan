# === Stage 12: Поиск по нескольким словам ===
# Project: LunchBoxPlan
def parse_query(query: str) -> list:
    """Разбирает строку поиска на список слов с поддержкой исключений.

    Слова, начинающиеся с «-», обрабатываются как исключения и
    возвращаются отдельным списком. Остальные слова собираются в список
    искомых ключевых слов.
    """
    negations: list = []
    keywords: list = []
    for token in query.split():
        if token.startswith("-"):
            negations.append(token[1:])
        else:
            keywords.append(token)
    return keywords, negations


def match_obed(obed: dict, keywords: list, negations: list) -> bool:
    """Проверяет, соответствует ли обед запросу.

    Обед считается подходящим, если он содержит все ключевые слова
    (в любом из своих полей) и не содержит ни одно из слов-исключений.
    """
    fields = [str(obed.get(key, "")).lower() for key in obed]
    for keyword in keywords:
        keyword = keyword.lower()
        if not any(keyword in field for field in fields):
            return False
    for negation in negations:
        negation = negation.lower()
        if any(negation in field for field in fields):
            return False
    return True


def search_obeds(obeds: list, query: str) -> list:
    """Ищет обеды по нескольким словам с поддержкой исключений через «-»."""
    keywords, negations = parse_query(query)
    results = [
        obed for obed in obeds
        if match_obed(obed, keywords, negations)
    ]
    return results
