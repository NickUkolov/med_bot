from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, KeyboardButtonPollType


def main_kb():
    kb_list = [
        [KeyboardButton(text="О нас"), KeyboardButton(text="Калькуляторы")]
    ]

    keyboard = ReplyKeyboardMarkup(
        keyboard=kb_list,
        is_persistent=True,
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_placeholder="Воспользуйтесь меню:"
    )
    return keyboard

def calculators_kb():
    kb_list = [
        [KeyboardButton(text="Пропофол"), KeyboardButton(text="Главное меню")]
    ]

    keyboard = ReplyKeyboardMarkup(
        keyboard=kb_list,
        is_persistent=True,
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_placeholder="Воспользуйтесь меню:"
    )
    return keyboard

def propofol_type_kb():
    kb_list = [
        [KeyboardButton(text="Индукция анестезии"), KeyboardButton(text="Поддержание анестезии"), KeyboardButton(text="Седация")],
        [KeyboardButton(text="Меню выбора калькуляторов")]
    ]

    keyboard = ReplyKeyboardMarkup(
        keyboard=kb_list,
        is_persistent=True,
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_placeholder="Воспользуйтесь меню:"
    )
    return keyboard
