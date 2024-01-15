# date_window.py
import tkinter as tk
from tkinter import ttk, filedialog
from tkcalendar import DateEntry
from calculate_profile import calculate_profile
from result_window import show_result_window
from image import draw_triangle, save_image
from tkinter import ttk

def open_partner_data_entry(root):
    partner_window = tk.Toplevel(root)
    partner_window.title("Данные расчёта портрета")
    partner_window.geometry("400x200")
    partner_window.resizable(False, False)

    # Создание и размещение элементов в форме
    frame = ttk.Frame(partner_window)
    frame.pack(padx=10, pady=10)

    name_label = ttk.Label(frame, text="Имя партнера:")
    name_label.grid(row=0, column=0, padx=5, pady=5, sticky="W")

    name_entry = ttk.Entry(frame)
    name_entry.grid(row=0, column=1, padx=5, pady=5)

    date_label = ttk.Label(frame, text="Дата рождения (ДД.ММ.ГГГГ):")
    date_label.grid(row=1, column=0, padx=5, pady=5, sticky="W")

    date_entry = DateEntry(frame, date_pattern="dd.MM.yyyy", year=2000, month=1, day=1, width=15)
    date_entry.grid(row=1, column=1, padx=5, pady=5)

    # Создание кнопки "Рассчитать портрет"
    calculate_button = ttk.Button(frame, text="Рассчитать портрет", command=lambda: get_partner_data(name_entry, date_entry), width=35)
    calculate_button.grid(row=2, columnspan=2, pady=(5, 0))

    # Создание кнопки "Вывести на экран"
    print_button = ttk.Button(partner_window, text="Вывести на экран", command=lambda: draw_triangle(date_entry.get(), name_entry.get()), width=35)
    print_button.pack(pady=(10, 0))

    # Создание кнопки "Сохранить портрет"
    save_button = ttk.Button(partner_window, text="Сохранить портрет", command=lambda: save_image(date_entry.get(), name_entry.get()), width=35)
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


def get_partner_data(name_entry, date_entry):
    partner_name = name_entry.get()
    partner_date_of_birth = date_entry.get()

    result = calculate_profile(partner_name, partner_date_of_birth, name_entry, date_entry)

    show_result_window(partner_date_of_birth, partner_name, result, name_entry, date_entry)