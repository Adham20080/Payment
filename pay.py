from aiogram import Bot, types
from aiogram import Dispatcher
from aiogram.types import LabeledPrice, PreCheckoutQuery
from config import PAYMENT_TOKEN

dp = Dispatcher()


async def order1(call: types.CallbackQuery, bot: Bot):
    await bot.send_invoice(call.from_user.id,
                           title="iPhone 15 PRO",
                           description="Smartfon Apple iPhone 15 PRO NanoSIM+eSIM, 5G, NFC, Wi-Fi 6",
                           provider_token=PAYMENT_TOKEN,
                           currency='UZS',
                           photo_url="https://images.uzum.uz/cn7hgprifoubkc6s4cs0/original.jpg",
                           photo_height=1080,
                           photo_width=1440,
                           photo_size=100,
                           is_flexible=False,
                           prices=[
                               LabeledPrice(label="Narxi", amount=17_990_000),
                               LabeledPrice(label="QQS", amount=2_023_875),
                               LabeledPrice(label="Chegirma", amount=-4_010_000)
                           ],
                           start_parameter='time-machine-example',
                           payload='some-invoice-payload-for-our-internal-use',
                           request_timeout=15
                           )


async def order2(call: types.CallbackQuery, bot: Bot):
    await bot.send_invoice(call.from_user.id,
                           title="iPhone 14 Plus",
                           description="Smartfon Apple iPhone 14 Plus",
                           provider_token=PAYMENT_TOKEN,
                           currency='UZS',
                           photo_url="https://images.uzum.uz/cnk67og4idugcqegf1l0/original.jpg",
                           photo_height=1080,
                           photo_width=1440,
                           photo_size=100,
                           is_flexible=False,
                           prices=[
                               LabeledPrice(label="Narxi", amount=12_299_000),
                               LabeledPrice(label="QQS", amount=1_383_637),
                               LabeledPrice(label="Chegirma", amount=-4_401_000)
                           ],
                           start_parameter='time-machine-example',
                           payload='some-invoice-payload-for-our-internal-use',
                           request_timeout=15
                           )


async def order3(call: types.CallbackQuery, bot: Bot):
    await bot.send_invoice(call.from_user.id,
                           title="MacBook Air 13",
                           description="Noutbuk Apple MacBook Air 13 M1 8GB/256GB, Gray",
                           provider_token=PAYMENT_TOKEN,
                           currency='UZS',
                           photo_url="https://images.uzum.uz/cnat9s1s99ouqbfvegsg/original.jpg",
                           photo_height=1080,
                           photo_width=1440,
                           photo_size=100,
                           is_flexible=False,
                           prices=[
                               LabeledPrice(label="Narxi", amount=12_299_000),
                               LabeledPrice(label="QQS", amount=1_461_375),
                               LabeledPrice(label="Chegirma", amount=-3_691_000)
                           ],
                           start_parameter='time-machine-example',
                           payload='some-invoice-payload-for-our-internal-use',
                           request_timeout=15
                           )


async def pre_checkout_query(pre_checkout_query: PreCheckoutQuery, bot: Bot):
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


async def successful_payment(message: types.Message):
    await message.answer(f"""
To'lov muvaffaqiyatli amalga oshirildi ✅
Maxsulot nomi : {message.successful_payment.invoice_payload}
Summa: {message.successful_payment.total_amount // 100} {message.successful_payment.currency} 💸
Menejerimiz so'rovingizni oldi va allaqachon sizga termoqda 💻
""")
