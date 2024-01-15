def to_roman(n):
    syb = [
        "XXII", "XXI", "XX", "XIX", "XVIII", "XVII", "XVI", "XV", "XIV", "XIII", "XII", "XI", "X", "IX", "VIII", "VII", "VI", "V", "IV", "III", "II", "I", "N"
    ]
    if n == 0:
        return "XXII"
    val = list(range(len(syb) - 1, -1, -1))
    roman_num = ''
    i = 0
    while n > 0:
        for _ in range(n // val[i]):
            roman_num += syb[i]
            n -= val[i]
        i += 1
    return roman_num

def get_tarot_card(roman_numeral):
    tarot_cards = {
        "I": "I - Маг",
        "II": "II - Жрица",
        "III": "III - Императрица",
        "IV": "IV - Император",
        "V": "V - Жрец",
        "VI": "VI - Влюбленные",
        "VII": "VII - Колесница",
        "VIII": "VIII - Правосудие",
        "IX": "IX - Отшельник",
        "X": "X - Колесо Фортуны",
        "XI": "XI - Сила",
        "XII": "XII - Повешенный",
        "XIII": "XIII - Смерть",
        "XIV": "XIV -Умеренность",
        "XV": "XV - Дьявол",
        "XVI": "XVI - Башня",
        "XVII": "XVII - Звезда",
        "XVIII": "XVIII - Луна",
        "XIX": "XIX - Солнце",
        "XX": "XX - Суд",
        "XXI": "XXI - Мир",
        "XXII": "XXII - Шут"
    }

    return tarot_cards.get(roman_numeral, "Неизвестный аркан")
