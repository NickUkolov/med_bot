from aiogram.fsm.state import StatesGroup, State

class CalcStates(StatesGroup):
    select_asa = State()
    select_age = State()
    select_bmi = State()
    enter_weight = State()
    show_result = State()