import asyncio
import logging
from aiogram import types
from aiogram import Bot, Dispatcher, F
from aiogram.filters.command import Command
from config import Token
from buttons import inline_btn
from pay import order1, pre_checkout_query, successful_payment

dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(f"Assalomu Aleykum.\nXurmatli {message.from_user.full_name}!\nBotimizga xush kelibsiz 👋",
                         reply_markup=inline_btn)


dp.callback_query.register(order1, F.data == "Tolov")
dp.pre_checkout_query.register(pre_checkout_query)
dp.message.register(successful_payment, F.successful_payment)


async def main() -> None:
    bot = Bot(token=Token)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
