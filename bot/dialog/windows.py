from aiogram_dialog import Window, Dialog
from aiogram_dialog.widgets.kbd import Button, Row
from aiogram_dialog.widgets.text import Const, Format
from aiogram_dialog.widgets.input import TextInput
from aiogram_dialog.widgets.kbd import Back, Cancel
from aiogram_dialog import DialogManager
from aiogram.fsm.context import FSMContext

from dialog.states import CalcStates
from dialog.utils import calculate_dose

# ASA выбор
asa_window = Window(
    Const("Выберите ASA-класс пациента:"),
    Row(
        Button(Const("I-II"), id="asa_1", on_click=lambda c, b, d: set_asa(c, d, "I-II")),
        Button(Const("III"), id="asa_3", on_click=lambda c, b, d: set_asa(c, d, "III")),
        Button(Const("IV-V"), id="asa_4", on_click=lambda c, b, d: set_asa(c, d, "IV-V")),
    ),
    state=CalcStates.select_asa
)

# Возраст
age_window = Window(
    Const("Пациент старше 65 лет?"),
    Row(
        Button(Const("Да"), id="age_yes", on_click=lambda c, b, d: set_age(c, d, True)),
        Button(Const("Нет"), id="age_no", on_click=lambda c, b, d: set_age(c, d, False)),
    ),
    state=CalcStates.select_age
)

# Ожирение
bmi_window = Window(
    Const("ИМТ пациента > 30 (ожирение)?"),
    Row(
        Button(Const("Да"), id="bmi_yes", on_click=lambda c, b, d: set_bmi(c, d, True)),
        Button(Const("Нет"), id="bmi_no", on_click=lambda c, b, d: set_bmi(c, d, False)),
    ),
    state=CalcStates.select_bmi
)

# Масса тела
weight_window = Window(
    Const("Введите массу тела пациента в кг:"),
    TextInput(id="weight_input", on_success=lambda c, b, d, w: set_weight(c, d, w)),
    state=CalcStates.enter_weight
)

async def result_getter(dialog_manager: DialogManager, **kwargs):
    return {
        "result": dialog_manager.dialog_data.get("result", "Нет результата")
    }

result_window = Window(
    Format("💉 Результат:\n{result}"),
    Cancel(Const("Завершить")),
    state=CalcStates.show_result,
    getter=result_getter
)

dialog = Dialog(
    asa_window,
    age_window,
    bmi_window,
    weight_window,
    result_window
)

# Колбэки

async def set_asa(c, d: DialogManager, value):
    d.dialog_data["asa"] = value
    d.dialog_data["mode"] = d.start_data["mode"]
    await d.next()

async def set_age(c, d: DialogManager, value):
    d.dialog_data["elderly"] = value
    await d.next()

async def set_bmi(c, d: DialogManager, value):
    d.dialog_data["obese"] = value
    await d.next()

async def set_weight(c, d: DialogManager, value):
    d.dialog_data["weight"] = float(value)
    result = calculate_dose(d.dialog_data)
    d.dialog_data["result"] = result
    await d.next()