import tkinter as tk
from tkinter import ttk, filedialog
from calculate_profile import get_tarot_card

def show_result_window(date_of_birth, full_name, portrait_data, name_entry, date_entry):
    result_window = tk.Toplevel()
    result_window.title("Психологический Портрет от Натальи Товцевой")
    result_window.geometry("250x450")
    result_window.minsize(250, 450)
    result_window.maxsize(250, 450)
    result_window.update_idletasks()
    width = result_window.winfo_width()
    height = result_window.winfo_height()
    x_offset = (result_window.winfo_screenwidth() - width) // 2
    y_offset = (result_window.winfo_screenheight() - height) // 2
    result_window.geometry(f"{width}x{height}+{x_offset}+{y_offset}")

    result_text = tk.StringVar()
    result_text.set(portrait_data)

    info_label = tk.Label(result_window, text=f"Дата рождения: {date_of_birth}\nИмя: {full_name}")
    info_label.pack(pady=(5, 0))

    result_label = tk.Label(result_window, textvariable=result_text, justify="center")
    result_label.pack(expand=True, pady=(0, 5))

    save_button = tk.Button(result_window, text="Сохранить", command=lambda: save_and_close(result_window, date_of_birth, full_name, portrait_data, name_entry, date_entry))
    save_button.pack(pady=(0, 15))  # отступ внизу кнопки

def save_and_close(result_window, date_of_birth, full_name, portrait_data, name_entry, date_entry):
    try:
        file_name = generate_file_name(name_entry, date_entry)
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")], initialfile=file_name)
        if file_path:
            with open(file_path, 'w') as file:
                file.write(f"Дата рождения: {date_of_birth}\nИмя: {full_name}\n\n{portrait_data}")
            result_window.destroy()
    except ValueError as e:
        # обработка ошибок, если необходимо
        pass

def generate_file_name(name_entry, date_entry):
    partner_name = name_entry.get() if name_entry.get() else "Партнёр"
    date_of_birth = date_entry.get().replace('.', '')
    return f"{partner_name}_{date_of_birth}"