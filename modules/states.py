
from aiogram.dispatcher.filters.state import State, StatesGroup


# Welcome form
class AllStates(StatesGroup):
        
    question_2 = State()
    question_3 = State()
    question_4 = State()