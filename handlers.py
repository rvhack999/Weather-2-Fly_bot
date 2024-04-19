""" основной файл, в котором будет содержать почти весь код бота. """

from aiogram import Router, types, F
from aiogram.types import Message
from aiogram.filters import Command
import kb
import text

router = Router()


@router.message(Command('start'))
async def start_handler(msg: Message):
    await msg.answer(text.greet.format(name=msg.from_user.full_name), reply_markup=kb.start_kb)


@router.message(F.location)
async def get_cords(msg: Message):
    lon = msg.location.longitude
    lat = msg.location.latitude
    await msg.answer(f'{lon}, {lat}')


