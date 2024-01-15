import tkinter as tk
import subprocess
from date_window import open_partner_data_entry
from date_window_composit import open_partner_data_entry_2

#
def open_calculation_file():
    # Выполнение файла с логикой калькуляции
    subprocess.Popen(["python", "calculate_profile.py"])
# 
def calculate_composite():
    # Выполнение файла с логикой расчета композита
    subprocess.Popen(["python", "calculate_composite.py"])
# создание окна психологического портрета
def create_window():
    root = tk.Tk()
    root.title("Психологический профиль")
    root.geometry("400x150")
    root.resizable(False, False)

    btn_profile = tk.Button(root, text="Психологический портрет", command=lambda: open_partner_data_entry(root))
    btn_profile.pack(pady=10, padx=20, fill=tk.X)

    # btn_composite = tk.Button(root, text="Композит пары", command=lambda: open_partner_data_entry_2())
    # btn_composite.pack(pady=10, padx=20, fill=tk.X)

    # btn_shadow_profile = tk.Button(root, text="Теневой портрет", command=lambda: calculate_shadow_profile)
    # btn_shadow_profile.pack(pady=10, padx=20, fill=tk.X)

    root.update_idletasks()  # Обновление размеров окна
    width = root.winfo_width()
    height = root.winfo_height()

    # Получение размеров экрана
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Расчет координат для размещения окна по центру экрана
    x_coordinate = int((screen_width - width) / 2)
    y_coordinate = int((screen_height - height) / 2)

    root.geometry(f"{width}x{height}+{x_coordinate}+{y_coordinate}")

    root.mainloop()

if __name__ == '__main__':
    create_window()