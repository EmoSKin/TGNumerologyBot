from tkinter import filedialog
from tkinter import StringVar
from PIL import Image, ImageDraw, ImageFont
from calculate_profile import calculate_positions
from calculate_composit_profile import calculate_composite_positions
from result_window import show_result_window
from roman_conversion import to_roman

template_image_path = "background/background.png"
template_image_path_2 = "background/background_composit.png"

x_offset = 0  # Добавил отсутствующую переменную x_offset
positions = []  # Добавил отсутствующий список positions
composite_image = Image.new("RGBA", (1, 1), (255, 255, 255, 0))  # Инициализация переменной composite_image
# Размер картинок карт
def resize_image(image_path, width, height):
    # Откройте изображение
    image = Image.open(image_path)

    # Масштабирование изображения
    resized_image = image.resize((width, height))

    return resized_image

# Римские цифры назначенные картам
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
# Создание словаря с уменьшенными изображениями римских цифр
roman_num_images = {}
for i in range(1, 23):
    roman_numeral = to_roman(i)
    image_path = f'card/{roman_numeral}.jpg'
    roman_num_images[roman_numeral] = resize_image(image_path, 230, 400)
# Создание треугольника арканов в "горшочке" вывод их на позиции с отрисовкой карт
def draw_triangle(date, name, x_offset=0):
    positions = calculate_positions(date)

    # Открываем шаблон изображения
    template_image = Image.open(template_image_path)
    draw = ImageDraw.Draw(template_image)

    # Координаты для позиций изображений и текста
    image_positions = [
        (1740, 1250), (2460, 1250), (3200, 1250), (2090, 1650), (2830, 1650),
        (2460, 2050), (3200, 2050), (2460, 2700), (2090, 700), (2830, 700),
        (2460, 280), (1740, 2050), (1360, 920), (3550, 920), (3200, 280),
        (1360, 920), (2090, 2500), (3550, 920), (3200, 280), (1360, 2500)
    ]

    text_positions = [
        (1700, 1450), (2420, 1450), (3180, 1450), (2050, 1850), (2780, 1850),
        (2420, 2250), (3150, 2250), (2420, 2900), (2050, 920), (2780, 920),
        (2420, 480), (1700, 2250), (1300, 1120), (3520, 1120), (3150, 480),
        (1300, 1120), (2050, 2700), (3520, 1120), (3150, 480), (1300, 2700)
    ]

    image_width, image_height = template_image.size
    y_offset = (image_width - (max(image_positions, key=lambda x: x[0])[0] - min(image_positions, key=lambda x: x[0])[0])) // 16
    custom_font = ImageFont.truetype("font/pt-serif-expert.ttf", 64)

    for i, (x, y) in enumerate(image_positions):
        y += y_offset
        roman_numeral = positions[i]
        roman_img = roman_num_images[roman_numeral]
        template_image.paste(roman_img, (x - roman_img.width // 2, y - roman_img.height // 2), roman_img.convert("RGBA"))

    for i, (x, y) in enumerate(text_positions):
        y += y_offset + 40
        x += 40
        draw.text((x, y), positions[i], font=custom_font, fill="black", anchor="mm")

    draw.text((125, 10), f"\nДата рождения: {date}", font=custom_font, fill="black")
    draw.text((125, 80), f"\nИмя: {name}", font=custom_font, fill="black")

    # Покажем изображение
    template_image.show()
    return template_image
# Создание комбинированного изображения
def create_combined_image(date, name):
    background_path = "background.png"
    background_image = Image.open(background_path)
    triangle_image = draw_triangle(date, name)
    
    background_width, background_height = background_image.size
    triangle_image = triangle_image.resize((background_width, background_height))

    combined_image = Image.alpha_composite(background_image.convert("RGBA"), triangle_image.convert("RGBA"))
    combined_image.show()
    return combined_image
# Расчёт позиций для выведения
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
    if month >= 13:
        raise ValueError("Месяц рождения не может быть больше 12")

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
# Функция сохранения изображения
def save_image(date, name):
    global result_text  # Объявляем переменную как глобальную
    try:
        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg")], initialfile=generate_image_file_name(date, name))
        if file_path:
            image = draw_triangle(date, name)
            image.save(file_path, format="PNG", quality=95)
            result_text.set("Изображение успешно сохранено!")  # Установка текста результата
    except ValueError as e:
        result_text.set("Ошибка при сохранении изображения: " + str(e))


# Композит
# Создание три треугольника арканов в "горшочке" вывод их на позиции с отрисовкой карт
def draw_triangle_on_image(draw, date, name, positions, x_offset=0, composite_image=None):
    # Координаты для позиций изображений и текста
    image_positions = [
        (1740, 1250), (2460, 1250), (3200, 1250), (2090, 1650), (2830, 1650),
        (2460, 2050), (3200, 2050), (2460, 2700), (2090, 700), (2830, 700),
        (2460, 280), (1740, 2050), (1360, 920), (3550, 920), (3200, 280),
        (1360, 920), (2090, 2500), (3550, 920), (3200, 280), (1360, 2500)
    ]

    text_positions = [
        (1700, 1450), (2420, 1450), (3180, 1450), (2050, 1850), (2780, 1850),
        (2420, 2250), (3150, 2250), (2420, 2900), (2050, 920), (2780, 920),
        (2420, 480), (1700, 2250), (1300, 1120), (3520, 1120), (3150, 480),
        (1300, 1120), (2050, 2700), (3520, 1120), (3150, 480), (1300, 2700)
    ]

    image_width, image_height = composite_image.size
    y_offset = (image_width - (max(image_positions, key=lambda x: x[0])[0] - min(image_positions, key=lambda x: x[0])[0])) // 16
    custom_font = ImageFont.truetype("font/pt-serif-expert.ttf", 64)

    for i, (x, y) in enumerate(image_positions):
        y += y_offset
        roman_numeral = positions[i]
        roman_img = roman_num_images[roman_numeral]
        composite_image.paste(roman_img, (x + x_offset - roman_img.width // 2, y - roman_img.height // 2), roman_img.convert("RGBA"))

    for i, (x, y) in enumerate(text_positions):
        y += y_offset + 40
        x += 40 + x_offset
        draw.text((x, y), positions[i], font=custom_font, fill="black", anchor="mm")
# Отрисовывем три треугольника арканов в "горшочке"
def draw_three_columns():
    try:
        date1 = date_entry_1.get()
        name1 = name_entry_1.get()
        date2 = date_entry_2.get()
        name2 = name_entry_2.get()

        # Создадим изображение с тремя столбцами информации
        composite_image = Image.new("RGB", (9000, 3500), color="white")
        background_composit = Image.open(template_image_path_2)
        draw = ImageDraw.Draw(composite_image)
        
        # Получим позиции для обоих партнеров
        positions_1 = calculate_positions(date1)
        positions_2 = calculate_positions(date2)

        # Вычислим композитные позиции для обоих партнеров
        composite_positions = calculate_composite_positions(positions_1, positions_2)

        # Определите проценты для левого, среднего и правого столбцов
        left_percentage = -0.10  # Процентная позиция левого столбца относительно ширины изображения
        center_percentage = 0.225  # Процентная позиция центрального столбца относительно ширины изображения
        right_percentage = 0.55  # Процентная позиция правого столбца относительно ширины изображения

        # Рассчитайте смещения для левого, среднего и правого столбцов
        left_x_offset = int(left_percentage * composite_image.width)  # Смещение по X для левого столбца
        center_x_offset = int(center_percentage * composite_image.width)  # Смещение по X для центрального столбца
        right_x_offset = int(right_percentage * composite_image.width)  # Смещение по X для правого столбца

        # Отрисуем первый столбец (левый)
        draw_triangle_on_image(draw, date1, name1, positions_1, x_offset=left_x_offset, composite_image=composite_image)
        # Вывод данных над левым столбцом
        font = ImageFont.truetype("arial.ttf", 64)  # Установка шрифта и его размера
        draw.text((left_x_offset + 2300, 225), f"{date1}\n{name1}", fill="black", font=font)

        # Отрисуем второй столбец (средний)
        draw_triangle_on_image(draw, date2, name2, positions_2, x_offset=center_x_offset, composite_image=composite_image)
        # Вывод данных над центральным столбцом
        draw.text((center_x_offset + 2300, 225), f"{date2}\n{name2}", fill="black", font=font)

        # Отрисуем третий столбец (правый)
        draw_triangle_on_image(draw, '.'.join(composite_positions), 'Композит пары', composite_positions, x_offset=right_x_offset, composite_image=composite_image)
        # Вывод данных над правым столбцом
        draw.text((right_x_offset + 2000, 225), f"Композит пары\n{name1} + {name2}", fill="black", font=font)

        # Сохраняем изображение
        composite_image.show()
        return composite_image
    except Exception as e:
        print(f"Ошибка при создании изображения: {e}")
# Сохраняем ихображение на устройстве
def save_composite_image():
    try:
        partner1_name = name_entry_1.get() if name_entry_1.get() else "Partner1"
        partner2_name = name_entry_2.get() if name_entry_2.get() else "Partner2"

        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg")], initialfile=generate_composite_image_file_name())
        if file_path:
            composite_image = draw_three_columns()
            composite_image.save(file_path)
    except Exception as e:
        print(f"Ошибка при сохранении: {e}")
# Генерируем имя для текстового файла на основе введённых данных
def generate_composite_file_name():
    partner1_name = name_entry_1.get() if name_entry_1.get() else "Partner1"
    partner2_name = name_entry_2.get() if name_entry_2.get() else "Partner2"
    date1 = date_entry_1.get().replace('.', '')
    date2 = date_entry_2.get().replace('.', '')
    return f"{partner1_name}_{date1}_{partner2_name}_{date2}"
# Генерируем имя для изображения на основе введённых данных
def generate_composite_image_file_name():
    # Ваша логика именования файла изображения композита, аналогично предыдущему примеру
    partner1_name = name_entry_1.get() if name_entry_1.get() else "Partner1"
    partner2_name = name_entry_2.get() if name_entry_2.get() else "Partner2"
    date1 = date_entry_1.get().replace('.', '')
    date2 = date_entry_2.get().replace('.', '')
    return f"{partner1_name}_{date1}_{partner2_name}_{date2}"


# Генерируем имя для изображения на основе введённых данных
def generate_image_file_name(date, name):
    # Ваша логика именования файла изображения, аналогичная функции generate_file_name()
    partner_name = name if name else "Partner"
    date = date.replace('.', '')
    return f"{partner_name}_{date}"