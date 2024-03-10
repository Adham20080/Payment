from aiogram.types import InlineKeyboardMarkup, KeyboardButton, InlineKeyboardButton, ReplyKeyboardMarkup

blog = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Ahmadjon Abdulfotih Blog", url="https://t.me/Ahmadjon_Abdulfotiyev")]])

men_but = [
    [KeyboardButton(text="Mahsulotlar"),
     KeyboardButton(text="Profil")],
    [KeyboardButton(text="Depozit"),
     KeyboardButton(text="Admin")]
]
menu = ReplyKeyboardMarkup(keyboard=men_but, resize_keyboard=True)

key = [
    [KeyboardButton(text="Phone 📱"),
     KeyboardButton(text="Laptop 💻")],
    [KeyboardButton(text="Orqaga")]
]
keyboard = ReplyKeyboardMarkup(keyboard=key, resize_keyboard=True)

iphone = [
    [KeyboardButton(text="iPhone 15 PRO"),
     KeyboardButton(text="iPhone 14 Plus")],
    [KeyboardButton(text="Orqaga")]
]
IPhone = ReplyKeyboardMarkup(keyboard=iphone, resize_keyboard=True)

mac = [
    [KeyboardButton(text="MacBook Air 13"), ],
    [KeyboardButton(text="Orqaga")]
]
macBook = ReplyKeyboardMarkup(keyboard=mac, resize_keyboard=True)

inline_btn = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="To'lov qilish", callback_data="Tolov")]
])

inline_btn1 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="To'lov qilish", callback_data="Tolov1")]
])

inline_btn2 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="To'lov qilish", callback_data="Tolov2")]
])
