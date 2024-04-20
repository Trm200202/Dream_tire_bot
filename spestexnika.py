###### gruzavoy uchun gruzavoy.py nomli python file ochib ichiga shularni yozdim#########
import logging
from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext, Dispatcher, filters
from aiogram.dispatcher.filters import Command
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from config import BOT_TOKEN, URL
from aiogram.dispatcher.filters import Text
import requests

TOKEN = BOT_TOKEN


logging.basicConfig(level=logging.INFO)


bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


    



class MeasurementState(StatesGroup):
    CHOOSE_TYPE = State()
    CHOOSE_SIZE = State()
    choose_size = State()






@dp.message_handler(Text(equals="Spestexnika"))
async def start(message: types.Message):
    types = ["Kara", "Avto pagruzchik"]
    type_buttons = [KeyboardButton(type) for type in types]
    type_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(*type_buttons)
    await message.answer("Mashina turini tanlang:", reply_markup=type_keyboard)
    await MeasurementState.CHOOSE_TYPE.set()

@dp.message_handler(filters.Text(equals=["Kara"]), state=MeasurementState.CHOOSE_TYPE)
async def start(message: types.Message):
    sizes = ["Kichik", "O'rta", "Katta"]
    size_buttons = [KeyboardButton(size) for size in sizes]
    size_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(*size_buttons)
    await message.answer("O'lchamni tanlang:", reply_markup=size_keyboard)
    await MeasurementState.CHOOSE_SIZE.set()

@dp.message_handler(filters.Text(equals=["Katta"]), state=MeasurementState.CHOOSE_SIZE)
async def Kat_size(message: types.Message, state: FSMContext):
    urls = f"{URL}api/kara-katta-category/"
    result = requests.get(urls)
    r = result.json()
    for i in r:
            caption = f"Malumotlar:\nModel: {i['model']},\nBrend: {i['brend']},\nNarx: {i['price']},\nSloy: {i['layer']}"
            image_url = f"{URL}{i['imagess']}"
            await bot.send_photo(chat_id=message.chat.id, photo=image_url,caption=caption)


@dp.message_handler(filters.Text(equals=["O'rta"]), state=MeasurementState.CHOOSE_SIZE)
async def Kat_size(message: types.Message, state: FSMContext):
    urls = f"{URL}api/kara-orta-category/"
    result = requests.get(urls)
    r = result.json()
    for i in r:
            caption = f"Malumotlar:\nModel: {i['model']},\nBrend: {i['brend']},\nNarx: {i['price']},\nSloy: {i['layer']}"
            image_url = f"{URL}{i['imagess']}"
            await bot.send_photo(chat_id=message.chat.id, photo=image_url,caption=caption)




@dp.message_handler(filters.Text(equals=["Kichik"]), state=MeasurementState.CHOOSE_SIZE)
async def Kat_size(message: types.Message, state: FSMContext):
    urls = f"{URL}api/kara-kichik-category/"
    result = requests.get(urls)
    r = result.json()
    for i in r:
            caption = f"Malumotlar:\nModel: {i['model']},\nBrend: {i['brend']},\nO'lchami: {i['size']}\nNarx: {i['price']},\nSloy: {i['layer']}"
            image_url = f"{URL}{i['imagess']}"
            await bot.send_photo(chat_id=message.chat.id, photo=image_url,caption=caption)







@dp.message_handler(filters.Text(equals=["Avto pagruzchik"]), state=MeasurementState.CHOOSE_TYPE)
async def start(message: types.Message):
    sizes = ["Kichik", "O'rta", "Katta"]
    size_buttons = [KeyboardButton(size) for size in sizes]
    size_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(*size_buttons)
    await message.answer("O'lchamni tanlang:", reply_markup=size_keyboard)
    await MeasurementState.choose_size.set()


@dp.message_handler(filters.Text(equals=["Katta"]), state=MeasurementState.choose_size)
async def Kat_size(message: types.Message, state: FSMContext):
    urls = f"{URL}api/avtopagruschik-katta-category/"
    result = requests.get(urls)
    r = result.json()
    for i in r:
            caption = f"Malumotlar:\nModel: {i['model']},\nBrend: {i['brend']},\nNarx: {i['price']},\nSloy: {i['layer']}"
            image_url = f"{URL}{i['imagess']}"
            await bot.send_photo(chat_id=message.chat.id, photo=image_url,caption=caption)


@dp.message_handler(filters.Text(equals=["O'rta"]), state=MeasurementState.choose_size)
async def Kat_size(message: types.Message, state: FSMContext):
    urls = f"{URL}api/avtopagruschik-orta-category/"
    result = requests.get(urls)
    r = result.json()
    for i in r:
            caption = f"Malumotlar:\nModel: {i['model']},\nBrend: {i['brend']},\nNarx: {i['price']},\nSloy: {i['layer']}"
            image_url = f"{URL}{i['imagess']}"
            await bot.send_photo(chat_id=message.chat.id, photo=image_url,caption=caption)




@dp.message_handler(filters.Text(equals=["Kichik"]), state=MeasurementState.choose_size)
async def Kat_size(message: types.Message, state: FSMContext):
    urls = f"{URL}api/avtopagruschik-kichik-category/"
    result = requests.get(urls)
    r = result.json()
    for i in r:
            caption = f"Malumotlar:\nModel: {i['model']},\nBrend: {i['brend']},\nO'lchami: {i['size']}\nNarx: {i['price']},\nSloy: {i['layer']}"
            image_url = f"{URL}{i['imagess']}"
            await bot.send_photo(chat_id=message.chat.id, photo=image_url,caption=caption)

            await state.finish()




if __name__ =="__main__":
    logging.info("Bot ishga tushirildi.")
    executor.start_polling(dispatcher=dp, skip_updates=True)