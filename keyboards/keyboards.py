from aiogram import types

button1 = types.KeyboardButton(text="/start")
button2 = types.KeyboardButton(text="/погода")
button3 = types.KeyboardButton(text="Ифно")
button4 = types.KeyboardButton(text="Случайная цитата")
button5 = types.KeyboardButton(text="Закрыть")

keyboard1 = [
    [button1, button2, button3],
    [button4, button5]
]

kb1 = types.ReplyKeyboardMarkup(keyboard=keyboard1, resize_keyboard=True)