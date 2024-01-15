# handlers.py
from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardRemove
from aiogram.dispatcher import Dispatcher
from position_logic import calculate_profile

async def start_keyboard(message: types.Message) -> None:
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = [
        types.KeyboardButton(text="Start"),
        types.KeyboardButton(text="Calculate"),
        types.KeyboardButton(text="Show"),
        types.KeyboardButton(text="Save"),
    ]
    keyboard.add(*buttons)

    await message.answer("Выберите действие:", reply_markup=keyboard)

# Функция для регистрации обработчиков в объекте Dispatcher
def setup(dp: Dispatcher):
    dp.register_callback_query_handler(command_handler, lambda c: c.data in ['start_button', 'calculate_button', 'show_button', 'save_button'])
    dp.register_message_handler(command_handler, commands=['calculate', 'show', 'save'])
        
# Обработчик команд /start
async def start_handler(callback_query: types.CallbackQuery) -> None:
    partner_name = callback_query.from_user.first_name
    date_of_birth = "2000-01-13"  # Здесь нужно использовать реальную дату
    result = calculate_profile(partner_name, date_of_birth)
    await callback_query.message.answer(result)

# Обработчик для кнопки Calculate и команды /calculate
# Аналогично, можно создать обработчики для show и save
async def calculate_handler(message: types.Message) -> None:
    username = message.from_user.first_name
    await message.answer(f"Ожидайте, {username}! расчёт займет какое - то время.")

# Функция-обработчик для команд calculate, show, save
async def command_handler(message: types.Message) -> None:
    username = message.from_user.first_name
    command = message.get_command()
    await message.answer(f"Привет, {username}! Это бот.")
    
    if command == '/calculate':
        await calculate_handler(message)
    elif command == '/show':
        await show_handler(message)
    elif command == '/save':
        await save_handler(message)
