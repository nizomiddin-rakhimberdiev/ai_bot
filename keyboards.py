from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu_btn = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Psixolog'),
            KeyboardButton(text='Dietolog'),
            KeyboardButton(text='Dasturchi')
        ]
    ],
    resize_keyboard=True
)