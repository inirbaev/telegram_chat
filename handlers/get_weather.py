from aiogram import types, Router, F
from aiogram.filters.command import Command
from keyboards.city_keyboards import make_row_keyboard
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
import requests

router = Router()
available_city_names = ["Москва", "Волгоград", "Санкт-Петербург", "Новосибирск"]

class ChoiceCityNames(StatesGroup):
    choice_city_names = State()

#Хэндлер на команду weather
@router.message(Command('weather'))
@router.message(Command('погода'))
async def cmd_weather(message: types.Message, state: FSMContext):
    name = message.chat.first_name
    await message.answer(f'Привет {name}, выберите город',
        reply_markup=make_row_keyboard(available_city_names)
    )
    await state.set_state(ChoiceCityNames.choice_city_names)

@router.message(ChoiceCityNames.choice_city_names, F.text.in_(available_city_names))
async def city_chosen(message: types.Message, state: FSMContext):
    city = message.text
    api = 'fa1b7809d6d6e8db0cab83ae564b1502' + '&q='
    url = 'https://api.openweathermap.org/data/2.5/weather?appid='
    for_celsius = '&units=metric'
    response = requests.get(url+api+city+for_celsius)
    data = response.json()
    temp = data['main']['temp']
    await message.answer(
        f'Сейчас в городе {city} {int(temp)}°C',
        reply_markup=types.ReplyKeyboardRemove()
    )
    await state.clear()


@router.message(ChoiceCityNames.choice_city_names)
async def cmd_weather_incorrectly(message: types.Message):
    await message.answer(
        f'Я не знаю такой город',
        reply_markup=make_row_keyboard(available_city_names)
    )