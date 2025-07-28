import asyncio

from aiogram_dialog import setup_dialogs

from create_bot import bot, dp
from dialog.windows import dialog
from handlers.start import start_router
from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_commands():
    commands = [BotCommand(command='start', description='Старт')]
    await bot.set_my_commands(commands, BotCommandScopeDefault())


async def start_bot():
    await set_commands()


async def main():
    dp.include_router(start_router)
    dp.include_router(dialog)
    setup_dialogs(dp)
    dp.startup.register(start_bot)

    try:
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())