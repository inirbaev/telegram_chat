from aiogram import types, F, Router
from aiogram.filters.command import Command
from keyboards.keyboards import kb1
import requests

router = Router()


#Хэндлер на команду start
@router.message(Command('start'))
async def cmd_start(message: types.Message):
    name = message.chat.first_name
    await message.answer(f'Привет, {name}', reply_markup=kb1)

#Хэндлер на команду stop
@router.message(Command('stop'))
async def cmd_stop(message: types.Message):
    name = message.chat.first_name
    await message.answer(f'Пока {name}')

#Функция генерирование цитат
def generate_russian_quote_from_api():
    api_url = "http://api.forismatic.com/api/1.0/"
    params = {
        "method": "getQuote",
        "lang": "ru",
        "format": "json",
    }

    try:
        response = requests.get(api_url, params=params)
        data = response.json()

        if "quoteText" in data:
            quote = data["quoteText"]
            return quote
        else:
            return "Не удалось получить цитату."
    except Exception as e:
        return f"Ошибка при запросе цитаты: {str(e)}"


#Хэндлер на команду /qutoes
@router.message(Command('quote'))
@router.message(Command('цитата'))
@router.message(F.text.lower() == 'случайная цитата')
async def cmd_quotes(message: types.Message):
    await message.answer(generate_russian_quote_from_api())

#Хэндлер на сообщения
@router.message(F.text)
async def cmd_echo(message: types.Message):
    msg = message.text.lower()
    name = message.chat.first_name
    if 'ты кто' in msg:
        await message.answer("Я бот")
    elif 'ифно' in msg:
        await message.answer('Чат бот создан для домашнего задания GeekBrains')
    elif 'закрыть' == msg:
        await message.answer(f'Пока {name}', reply_markup=types.ReplyKeyboardRemove())
    else:
        await message.answer('Я не знаю такого слова')