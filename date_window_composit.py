import tkinter as tk
from tkinter import ttk, filedialog
from tkcalendar import DateEntry
from result_window import save_and_close, show_result_window
from calculate_profile import calculate_profile
from calculate_composit_profile import calculate_composite_positions
from image import draw_triangle_on_image, save_composite_image

def open_partner_data_entry_2(root):
    partner_window = tk.Toplevel(root)
    partner_window.title("Данные расчёта композитного портрета")
    partner_window.geometry("400x300")
    partner_window.resizable(False, False)

    # Создание и размещение элементов в форме
    frame = ttk.Frame(partner_window)
    frame.pack(padx=10, pady=10)

    name_label_1 = ttk.Label(frame, text="Имя первого партнера:")
    name_label_1.grid(row=0, column=0, padx=5, pady=5, sticky="W")

    name_entry_1 = ttk.Entry(frame)
    name_entry_1.grid(row=0, column=1, padx=5, pady=5)

    date_label_1 = ttk.Label(frame, text="Дата рождения первого партнера (ДД.ММ.ГГГГ):")
    date_label_1.grid(row=1, column=0, padx=5, pady=5, sticky="W")

    date_entry_1 = DateEntry(frame, date_pattern="dd.MM.yyyy", year=2000, month=1, day=1, width=15)
    date_entry_1.grid(row=1, column=1, padx=5, pady=5)

    name_label_2 = ttk.Label(frame, text="Имя второго партнера:")
    name_label_2.grid(row=2, column=0, padx=5, pady=5, sticky="W")

    name_entry_2 = ttk.Entry(frame)
    name_entry_2.grid(row=2, column=1, padx=5, pady=5)

    date_label_2 = ttk.Label(frame, text="Дата рождения второго партнера (ДД.ММ.ГГГГ):")
    date_label_2.grid(row=3, column=0, padx=5, pady=5, sticky="W")

    date_entry_2 = DateEntry(frame, date_pattern="dd.MM.yyyy", year=2000, month=1, day=1, width=15)
    date_entry_2.grid(row=3, column=1, padx=5, pady=5)

    # Создание кнопки "Рассчитать композитный портрет"
    calculate_button = ttk.Button(frame, text="Рассчитать композитный портрет", command=lambda: get_partner_composite_data(name_entry_1, date_entry_1, name_entry_2, date_entry_2), width=35)
    calculate_button.grid(row=4, columnspan=2, pady=(5, 0))

    # Создание кнопки "Вывести на экран композит"
    print_button = ttk.Button(partner_window, text="Вывести на экран композит", command=lambda: draw_triangle_on_image(date_entry_1.get(), name_entry_1.get(), date_entry_2.get(), name_entry_2.get()), width=35)
    print_button.pack(pady=(10, 0))

    # Создание кнопки "Сохранить композит"
    save_button = ttk.Button(partner_window, text="Сохранить композит", command=lambda: save_composite_image(date_entry_1.get(), name_entry_1.get(), date_entry_2.get(), name_entry_2.get()), width=35)
    save_button.pack(pady=(10, 0))

    # Центрирование кнопок внутри формы
    partner_window.update_idletasks()
    width = partner_window.winfo_width()
    height = partner_window.winfo_height()

    x_offset = (partner_window.winfo_screenwidth() - width) // 2
    y_offset = (partner_window.winfo_screenheight() - height) // 2

    partner_window.geometry(f"{width}x{height}+{x_offset}+{y_offset}")

    result_text = tk.StringVar()  # Создаем объект StringVar
    result_label = tk.Label(partner_window, textvariable=result_text)
    result_label.pack()

def get_partner_composite_data(name_entry_1, date_entry_1, name_entry_2, date_entry_2):
    partner_name_1 = name_entry_1.get()
    partner_date_of_birth_1 = date_entry_1.get()

    partner_name_2 = name_entry_2.get()
    partner_date_of_birth_2 = date_entry_2.get()

    result_1 = calculate_profile(partner_name_1, partner_date_of_birth_1, name_entry_1, date_entry_1)
    result_2 = calculate_profile(partner_name_2, partner_date_of_birth_2, name_entry_2, date_entry_2)

    show_result_window(partner_date_of_birth_1, partner_name_1, result_1, name_entry_1, date_entry_1)
    show_result_window(partner_date_of_birth_2, partner_name_2, result_2, name_entry_2, date_entry_2)
