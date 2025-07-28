from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from aiogram_dialog import DialogManager, StartMode

from dialog.states import CalcStates
from keyboards.all_keyboards import main_kb, calculators_kb, propofol_type_kb

start_router = Router()

@start_router.message(CommandStart())
async def start(message: Message):
    await message.answer('Дарова, любитель пропофола =)',
                         reply_markup=main_kb())

@start_router.message(F.text == "О нас")
async def about(message: Message):
    await message.answer('Что-то о создателях',
                         reply_markup=main_kb())

@start_router.message(F.text == "Калькуляторы")
async def calculators(message: Message):
    await message.answer('Выбери тип калькулятора',
                         reply_markup=calculators_kb())

@start_router.message(F.text == "Пропофол")
async def calculators(message: Message):
    await message.answer('Выбери тип калькулятора',
                         reply_markup=propofol_type_kb())

@start_router.message(F.text == "Главное меню")
async def calculators(message: Message):
    await message.answer('Главное меню',
                         reply_markup=main_kb())

@start_router.message(F.text.in_(["Индукция анестезии", "Поддержание анестезии", "Седация"]))
async def start_calc(message: Message, dialog_manager: DialogManager):
    mode_map = {
        "Индукция анестезии": "induction",
        "Поддержание анестезии": "maintenance",
        "Седация": "sedation"
    }
    m = mode_map[message.text]
    await dialog_manager.start(CalcStates.select_asa, mode=StartMode.RESET_STACK, data={"mode": m})


@start_router.message(F.text == "Меню выбора калькуляторов")
async def calculators(message: Message):
    await message.answer('Выбери тип калькулятора',
                         reply_markup=calculators_kb())