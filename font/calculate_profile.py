import tkinter as tk
from tkinter import ttk, filedialog
from tkcalendar import DateEntry
from PIL import Image, ImageDraw, ImageFont
from roman_conversion import get_tarot_card
from position_logic import calculate_positions

template_image_path = "background/background.png"
template_image_path_2 = "background/background_composit.png"

# выведение позиций строго по порядку
def calculate_profile(partner_name, date_of_birth, name_entry, date_entry):
    try:
        positions = calculate_positions(date_of_birth)
        result = f"1 позиция: {get_tarot_card(positions[0])}\n2 позиция: {get_tarot_card(positions[1])}\n3 позиция: {get_tarot_card(positions[2])}\n4 позиция: {get_tarot_card(positions[3])}\n5 позиция: {get_tarot_card(positions[4])}\n6 позиция: {get_tarot_card(positions[5])}\n7 позиция: {get_tarot_card(positions[6])}\n8 позиция: {get_tarot_card(positions[7])}\n9 позиция: {get_tarot_card(positions[8])}\n10 позиция: {get_tarot_card(positions[9])}\n11 позиция: {get_tarot_card(positions[10])}\n12 позиция: {get_tarot_card(positions[11])}\nПР1: {get_tarot_card(positions[15])}\nПР2: {get_tarot_card(positions[16])}\nПР3: {get_tarot_card(positions[17])}\nКО7: {get_tarot_card(positions[18])}\nКО12: {get_tarot_card(positions[19])}"

        # Возвращаем результат расчета
        return result
    except ValueError as e:
        return str(e)