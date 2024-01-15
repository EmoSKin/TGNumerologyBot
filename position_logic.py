# position_logic.py
from roman_conversion import to_roman, get_tarot_card

def calculate_profile(date_of_birth):
    try:
        positions = calculate_positions(date_of_birth)
        result = f"1 позиция: {get_tarot_card(positions[0])}\n2 позиция: {get_tarot_card(positions[1])}\n3 позиция: {get_tarot_card(positions[2])}\n4 позиция: {get_tarot_card(positions[3])}\n5 позиция: {get_tarot_card(positions[4])}\n6 позиция: {get_tarot_card(positions[5])}\n7 позиция: {get_tarot_card(positions[6])}\n8 позиция: {get_tarot_card(positions[7])}\n9 позиция: {get_tarot_card(positions[8])}\n10 позиция: {get_tarot_card(positions[9])}\n11 позиция: {get_tarot_card(positions[10])}\n12 позиция: {get_tarot_card(positions[11])}\nПР1: {get_tarot_card(positions[15])}\nПР2: {get_tarot_card(positions[16])}\nПР3: {get_tarot_card(positions[17])}\nКО7: {get_tarot_card(positions[18])}\nКО12: {get_tarot_card(positions[19])}"

        # Возвращаем результат расчета
        return result
    except ValueError as e:
        return str(e)

def adjust_position(position):
    if position == 0:
        return '22'
    elif position > 22:
        return str(position - 22)
    elif position < 0:
        return str(22 + position)
    else:
        return str(position)

def calculate_positions(date):
    day, month, year = map(int, date.split('.'))
    
    def adjust_over_limit(position):
        if position > 22:
            return position - 22
        elif position <= 0:
            return 22 + position
        else:
            return position

    position_1 = adjust_over_limit(day)
    if month > 12 or month < 1:
        raise ValueError("Месяц рождения должен быть в диапазоне от 1 до 12.")

    position_2 = month
    position_3 = sum(int(digit) for digit in str(year))
    position_3 = adjust_over_limit(position_3)
    position_4 = adjust_over_limit(position_1 + position_2)
    position_5 = adjust_over_limit(position_2 + position_3)
    position_6 = adjust_over_limit(position_4 + position_5)
    position_7 = adjust_over_limit(position_1 + position_5)
    position_8 = adjust_over_limit(position_2 + position_6)
    position_9 = abs(position_1 - position_2)
    position_9 = 22 if position_9 == 0 else position_9
    position_10 = abs(position_2 - position_3)
    position_10 = 22 if position_10 == 0 else position_10
    position_11 = abs(position_9 - position_10)
    position_12 = adjust_over_limit(position_7 + position_8)
    position_13 = adjust_over_limit(position_1 + position_4 + position_6)
    position_14 = adjust_over_limit(position_3 + position_5 + position_6)
    position_15 = adjust_over_limit((position_9 + position_10 + position_11) - position_7)
    position_PR1 = adjust_over_limit(position_13)
    position_PR2_1 = adjust_over_limit(position_2 + position_4 + position_5 + position_6)
    position_PR2_1 = adjust_over_limit(position_PR2_1)
    position_PR2_2 = adjust_over_limit(position_6 + position_8)
    position_PR2 = adjust_over_limit(position_PR2_1)
    position_PR2 = adjust_over_limit(position_PR2_2)
    position_PR2 = adjust_over_limit(position_PR2)
    position_PR3 = adjust_over_limit(position_14)
    position_KO7 = adjust_over_limit(position_15)
    position_KO12 = adjust_over_limit((position_9 + position_10 + position_11) - position_12)
    position_KO7 = adjust_over_limit(position_KO7)

    positions = [
        adjust_over_limit(position_1), adjust_over_limit(position_2),
        adjust_over_limit(position_3), adjust_over_limit(position_4),
        adjust_over_limit(position_5), adjust_over_limit(position_6),
        adjust_over_limit(position_7), adjust_over_limit(position_8),
        adjust_over_limit(position_9), adjust_over_limit(position_10),
        adjust_over_limit(position_11), adjust_over_limit(position_12),
        adjust_over_limit(position_13), adjust_over_limit(position_14),
        adjust_over_limit(position_15), adjust_over_limit(position_PR1),
        adjust_over_limit(position_PR2), adjust_over_limit(position_PR3),
        adjust_over_limit(position_KO7), adjust_over_limit(position_KO12)
    ]

    return [to_roman(pos) for pos in positions]
