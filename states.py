# states.py
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State

class NumerologyState(StatesGroup):
    WaitForBirthdate = State()