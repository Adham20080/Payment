import asyncio
import logging
from aiogram import types
from aiogram import Bot, Dispatcher, F
from aiogram.filters.command import Command
from config import Token, Admin_ID
from buttons import inline_btn, inline_btn1, inline_btn2, menu, IPhone, macBook, keyboard
from pay import order1, order2, order3, pre_checkout_query, successful_payment

dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    if message.from_user.id != Admin_ID:
        await message.answer(f"Assalomu Aleykum.\nXurmatli {message.from_user.full_name}!\nBotimizga xush kelibsiz 👋",
                             reply_markup=menu)
    else:
        await message.answer("Assalomu Aleykum hurmatli Admin janoblari", reply_markup=menu)


@dp.message(F.text == "Mahsulotlar")
async def cmd_start(message: types.Message):
    await message.answer(f"Xurmatli {message.from_user.full_name}!\nMahsulotni tanlang",
                         reply_markup=keyboard)


@dp.message(F.text == "Phone 📱")
async def cmd_start(message: types.Message):
    await message.answer(f"Xurmatli {message.from_user.full_name}!\nMahsulotni tanlang",
                         reply_markup=IPhone)

    @dp.message(F.text == "iPhone 15 PRO")
    async def cmd_start(message: types.Message):
        await message.answer_photo("https://images.uzum.uz/cn7hgprifoubkc6s4cs0/original.jpg",
                                   caption=f"Xurmatli {message.from_user.full_name}!",
                                   reply_markup=inline_btn)

    @dp.message(F.text == "iPhone 14 Plus")
    async def cmd_start(message: types.Message):
        await message.answer_photo("https://images.uzum.uz/cnk67og4idugcqegf1l0/original.jpg",
                                   caption=f"Xurmatli {message.from_user.full_name}!",
                                   reply_markup=inline_btn1)


@dp.message(F.text == "Laptop 💻")
async def cmd_start(message: types.Message):
    await message.answer(f"Xurmatli {message.from_user.full_name}!",
                         reply_markup=macBook)

    @dp.message(F.text == "MacBook Air 13")
    async def cmd_start(message: types.Message):
        await message.answer_photo("https://images.uzum.uz/cnat9s1s99ouqbfvegsg/original.jpg",
                                   caption=f"Xurmatli {message.from_user.full_name}!",
                                   reply_markup=inline_btn2)


@dp.message(F.text == "Orqaga")
async def cmd_start(message: types.Message):
    await message.answer(f"Xurmatli {message.from_user.full_name}!\nOrtga qaytildi",
                         reply_markup=menu)


dp.callback_query.register(order1, F.data == "Tolov")
dp.callback_query.register(order2, F.data == "Tolov1")
dp.callback_query.register(order3, F.data == "Tolov2")
dp.pre_checkout_query.register(pre_checkout_query)
dp.message.register(successful_payment, F.successful_payment)


async def main() -> None:
    bot = Bot(token=Token)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
