from aiogram.types import InlineKeyboardMarkup, KeyboardButton, InlineKeyboardButton, ReplyKeyboardMarkup

blog = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Ahmadjon Abdulfotih Blog", url="https://t.me/Ahmadjon_Abdulfotiyev")]])

key = [
    [KeyboardButton(text="Iphone 📱"),
     KeyboardButton(text="MacBook 💻")],
]
keyboard = ReplyKeyboardMarkup(keyboard=key, resize_keyboard=True)

inline_btn = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="To'lov tizimi", callback_data="Tolov")]
])
