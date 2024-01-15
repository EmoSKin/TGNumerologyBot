import tkinter as tk
from PIL import Image, ImageTk
from position_logic import calculate_positions

# Импорты других необходимых модулей

# Расчёт композита
def calculate_composite_positions(positions1, positions2):
    composite_positions = []
    roman_dict = {'I': 1, 'II': 2, 'III': 3, 'IV': 4, 'V': 5, 'VI': 6, 'VII': 7, 'VIII': 8, 'IX': 9, 'X': 10,
                  'XI': 11, 'XII': 12, 'XIII': 13, 'XIV': 14, 'XV': 15, 'XVI': 16, 'XVII': 17, 'XVIII': 18,
                  'XIX': 19, 'XX': 20, 'XXI': 21, 'XXII': 22}

    def roman_to_int(roman):
        return roman_dict.get(roman)

    def to_roman(n):
        return {v: k for k, v in roman_dict.items()}[n]

    for pos1, pos2 in zip(positions1, positions2):
        val1 = roman_to_int(pos1)
        val2 = roman_to_int(pos2)

        if val1 is None or val2 is None:
            print(f"Ошибка: Неверный формат данных в позициях {pos1} и {pos2}")
            continue

        composite_val = (val1 + val2)
        if composite_val >= 23:
            composite_val -= 22
        if composite_val == 0:
            composite_positions.append(to_roman(22))
        if composite_val < 0:
            composite_val = (22-(val1 + val2))
        else:
            composite_positions.append(to_roman(composite_val))

    return composite_positions
# Функция расчета композита и вывода информации
def calculate_composite():
    try:
        global date_entry_1, name_entry_1, date_entry_2, name_entry_2  # Объявляем переменные как глобальные

        # Определение переменных date_entry_1, name_entry_1, date_entry_2, name_entry_2
        date1 = date_entry_1.get()
        name1 = name_entry_1.get()
        date2 = date_entry_2.get()
        name2 = name_entry_2.get()

        # Проверка заполнения полей
        if not date1 or not date2:
            raise ValueError("Пожалуйста, заполните поля для обоих партнеров.")

        # Вычисление позиций для каждого партнера
        positions_1 = calculate_positions(date1)
        positions_2 = calculate_positions(date2)

        # Проверка наличия позиций
        if not positions_1 or not positions_2:
            raise ValueError("Ошибка при расчете позиций для обоих партнеров.")

        # Вычисление композита
        composite_positions = calculate_composite_positions(positions_1, positions_2)

        # Формирование текстовых данных для вывода
        partner1_result = "\n".join([f"Позиция {i+1}: {get_tarot_card(pos)}" for i, pos in enumerate(positions_1)])
        partner2_result = "\n".join([f"Позиция {i+1}: {get_tarot_card(pos)}" for i, pos in enumerate(positions_2)])
        composite_result = "\n".join([f"Позиция {i+1}: {get_tarot_card(pos)}" for i, pos in enumerate(composite_positions)])

        # Отображение окна с информацией
        show_composite_window(partner1_result, partner2_result, composite_result, date1, name1, date2, name2)

        return composite_result, composite_result  # Возвращаем значения для сохранения
    except ValueError as e:
        print(f"Ошибка: {e}")
        return None, None

# Окно для вывода информации о композите
def show_composite_window(partner1_data, partner2_data, composite_data, date1, name1, date2, name2):
    # Определение окна и его параметров
    composite_window = tk.Toplevel()
    composite_window.title("Композит Психологических Портретов")
    composite_window.geometry("960x420")
    composite_window.minsize(960, 420)

    composite_frame = tk.Frame(composite_window)
    composite_frame.pack(fill='both', expand=True)

    # Создание текстовых полей для отображения данных
    partner1_text = tk.Text(composite_frame, height=15, width=25)
    partner1_text.pack(side='left', fill='both', expand=True)
    partner1_text.insert(tk.END, f"1 партнёр: {name1} \nдатой рождения {date1}:\n\n{partner1_data}")

    # Остальные текстовые поля аналогично для второго партнёра и композита

    def save_and_close():
        file_name = generate_composite_file_name()
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")], initialfile=file_name)
        if file_path:
            with open(file_path, 'w') as file:
                file.write(f"1 партнёр: {name1} \nдатой рождения {date1}:\n{partner1_data}\n\n"
                           f"2 партнёр: {name2} \nдатой рождения {date2}:\n{partner2_data}\n\n"
                           f"Композит:  {name1 if name1 else '1 Партнёр'} + {name2 if name2 else '2 партнёр'}\n{composite_data}")
        composite_window.destroy()

    save_button = tk.Button(composite_window, text="Сохранить", command=save_and_close)
    save_button.pack(side='bottom', pady=10)

    # Установка центра окна
    composite_window.update_idletasks()
    width = composite_window.winfo_width()
    height = composite_window.winfo_height()
    x_offset = (composite_window.winfo_screenwidth() - width) // 2
    y_offset = (composite_window.winfo_screenheight() - height) // 2
    composite_window.geometry(f"{width}x{height}+{x_offset}+{y_offset}")

if __name__ == "__main__":
    composite_window()  # Функция, запускающая окно для расчета композита
