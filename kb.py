""" все клавиатуры, используемые ботом. """
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove

start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Предоставить доступ к местоположению', request_location=True),
        ]
    ],
    resize_keyboard=True
)



