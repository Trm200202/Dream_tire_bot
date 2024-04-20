## asosiy file main.py########
import logging
from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from config import BOT_TOKEN, URL
import requests
from aiogram.dispatcher.filters import Text
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from buttons import *
from states import *



TOKEN = BOT_TOKEN
logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)






@dp.message_handler(Command("start"),)
async def start_command(message: types.Message):
    keyboard1 = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard1.add(
        KeyboardButton(text="🇺🇿 O'zbek tili"),
        KeyboardButton(text="🇷🇺 Русский язык")
    )
    await message.answer(f"Tilni tanlang / Выберите язык👇",reply_markup=keyboard1)







############## O'zbek tili uchun ###########
    

@dp.message_handler(Text(equals="🇺🇿 O'zbek tili"))
async def Hodim_kerak(message: types.Message):
    await message.answer(text=f"Assalomu alekom!\nHurmatli mijoz, tanishib olsak.\nIltimos ismingizni yozing.",
            reply_markup=types.ReplyKeyboardRemove())
    await UzbeklangState.ask_name.set()




@dp.message_handler(state=UzbeklangState.ask_name)
async def ask_name_handler(message: types.Message, state: FSMContext):
    keyboard = create_phone_number_keyboard()
    name = message.text
    await state.update_data(first_name=name)
    await message.answer(text=
                f"Rahmat {name} !\nmenedjer va dasturchiklar siz bilan bog'lanish uchun nomeringizni kiritishingizni iltimos qilamiz",
                reply_markup=keyboard
            )
    await UzbeklangState.next()

def create_phone_number_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    button = KeyboardButton(text=f"Telefon raqamini yuborish\nОтправить номер телефона", request_contact=True)
    keyboard.add(button)
    return keyboard

@dp.message_handler(state=UzbeklangState.ask_phone)
async def error_phone(message: types.Message, state: FSMContext):
        print(message.text)
        keyboard = create_phone_number_keyboard()
        await message.answer("Iltimos, telefon raqamingizni pastdagi tugma orqali yuboring.", reply_markup=keyboard)


@dp.message_handler(content_types=[types.ContentType.CONTACT], state=UzbeklangState.ask_phone)
async def ask_phone_handler(message: types.Message,state: FSMContext):
        await state.update_data(ask_phone=message.text)
        first_name = await state.get_data()
        await message.answer(
            f"Tabriklaymiz {first_name.get('first_name')}!\nSiz DREAM TIRE mijoziga aylandingiz😊\nIltimos o'z avtomabilingizni tanlang!👇",
            reply_markup=none_parent_cat(a)
        )
        await UzbeklangState.CHOOSE_CATEGORY.set()



############## Rus tili uchun##############

@dp.message_handler(Text(equals="🇷🇺 Русский язык"))
async def Hodim_kerak(message: types.Message):
    await message.answer(text=f"Здравствуйте!\nУважаемый клиент, давайте знакомиться.\nПожалуйста, напишите свое имя",
             reply_markup=types.ReplyKeyboardRemove())
    await RuslangState.ask_imya.set()


@dp.message_handler(state=RuslangState.ask_imya)
async def ask_name_handler(message: types.Message, state: FSMContext):
    keyboard = create_phone_number_keyboard()
    name = message.text
    await state.update_data(first_name=name)
    await message.answer(text=
                f"Спасибо {name}!\nПросим ваш номер, чтобы менеджер и программисты могли с вами связаться",
                reply_markup=keyboard
            )
    await RuslangState.next()


@dp.message_handler(state=RuslangState.ask_tel)
async def error_phone(message: types.Message, state: FSMContext):
        keyboard = create_phone_number_keyboard()
        await message.answer("Пожалуйста, отправьте свой номер телефона, нажав кнопку ниже", reply_markup=keyboard)



@dp.message_handler(content_types=[types.ContentType.CONTACT], state=RuslangState.ask_tel)
async def ask_phone_handler(message: types.Message,state: FSMContext):
        await state.update_data(ask_phone=message.text)
        first_name = await state.get_data()
        await message.answer(
            f"Поздравляем {first_name.get('first_name')}!\nВы стали клиентом DREAM TIRE😊\nПожалуйста, выберите свой автомобиль!👇",
            reply_markup=none_parent_cat(a)
        )
        await RuslangState.CHOOSE_CATEGORY.set()

















def create_inline_keyboard():
    minus_button = InlineKeyboardButton(text='➖', callback_data='minus')
    plus_button = InlineKeyboardButton(text='➕', callback_data='plus')
    count_button = InlineKeyboardButton(text='0', callback_data='count')
    save_button = InlineKeyboardButton(text='📥 Savatga yuklash', callback_data='savat')
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[minus_button, count_button, plus_button]])
    keyboard.add(save_button)
    return keyboard


def create_inline_keyboard_count(count):
    minus_button = InlineKeyboardButton(text='➖', callback_data='minus')
    plus_button = InlineKeyboardButton(text='➕', callback_data='plus')
    count_button = InlineKeyboardButton(text=str(count), callback_data='count')
    save_button = InlineKeyboardButton(text='📥 Savatga yuklash', callback_data='savat')
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[minus_button, count_button, plus_button]])
    keyboard.add(save_button)
    return keyboard



def ru_create_inline_keyboard():
    minus_button = InlineKeyboardButton(text='➖', callback_data='minus')
    plus_button = InlineKeyboardButton(text='➕', callback_data='plus')
    count_button = InlineKeyboardButton(text='0', callback_data='count')
    save_button = InlineKeyboardButton(text='📥 Добавить в корзину', callback_data='savat')
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[minus_button, count_button, plus_button]])
    keyboard.add(save_button)
    return keyboard


def ru_create_inline_keyboard_count(count):
    minus_button = InlineKeyboardButton(text='➖', callback_data='minus')
    plus_button = InlineKeyboardButton(text='➕', callback_data='plus')
    count_button = InlineKeyboardButton(text=str(count), callback_data='count')
    save_button = InlineKeyboardButton(text='📥 Добавить в корзину', callback_data='savat')
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[minus_button, count_button, plus_button]])
    keyboard.add(save_button)
    return keyboard



####### fura uchun fura.py nomli python file ochib ochiga shularni yozdim#############
####### O'zbek tili uchun ########


@dp.message_handler(Text(equals="Fura -- Фура"), state=UzbeklangState.CHOOSE_CATEGORY)
async def start(message: types.Message):
    await message.answer("O'lchamni tanlang👇", reply_markup=SizeCategory_buuton(b))
    await UzbeklangState.CHOOSE_SIZE.set()




@dp.message_handler(Text(equals=["Katta"]), state=UzbeklangState.CHOOSE_SIZE)
async def Kat_size(message: types.Message, state: FSMContext):
    urls = f"{URL}api/fura-katta-category/"
    result = requests.get(urls)
    r = result.json()
    count_button = 0
    for i in r:
        caption = f"Malumotlar:\nBrend: {i['brend']}\nModel: {i['model']}\nO'lchami: {i['size']}\nNarx: {i['price']}\nSloy: {i['layer']}"
        image_url = f"{URL}{i['imagess']}"
        await bot.send_photo(chat_id=message.chat.id, photo=image_url, caption=caption, reply_markup=create_inline_keyboard())
        await state.update_data(count_button=count_button)



@dp.callback_query_handler(state=UzbeklangState.CHOOSE_SIZE)
async def handle_callback(callback_query: types.CallbackQuery, state: FSMContext):
    callback_data = callback_query.data
    data = await state.get_data()
    count_button = data.get('count_button')
    if callback_data == 'plus':
        count_button = int(count_button) + 1
        await state.update_data(count_button=count_button)
        await bot.edit_message_reply_markup(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, reply_markup=create_inline_keyboard_count(count_button))
    elif callback_data == 'minus':
        if count_button>0:
            count_button = int(count_button) - 1
            await state.update_data(count_button=count_button)
        await bot.edit_message_reply_markup(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, reply_markup=create_inline_keyboard_count(count_button))
        


@dp.message_handler(Text(equals=["O'rta"]), state=UzbeklangState.CHOOSE_SIZE)
async def Kat_size(message: types.Message, state: FSMContext):
    urls = f"{URL}api/fura-orta-category/"
    result = requests.get(urls)
    r = result.json()
    count_button = 0
    for i in r:
        caption = f"Malumotlar:\nBrend: {i['brend']}\nModel: {i['model']}\nO'lchami: {i['size']}\nNarx: {i['price']}\nSloy: {i['layer']}"
        image_url = f"{URL}{i['imagess']}"
        await bot.send_photo(chat_id=message.chat.id, photo=image_url,caption=caption, reply_markup=create_inline_keyboard())
        await state.update_data(count_button=count_button)



@dp.message_handler(Text(equals=["Kichik"]), state=UzbeklangState.CHOOSE_SIZE)
async def Kat_size(message: types.Message, state: FSMContext):
    urls = f"{URL}api/fura-kichik-category/"
    result = requests.get(urls)
    r = result.json()
    count_button = 0
    for i in r:
            caption = f"Malumotlar:\nBrend: {i['brend']}\nModel: {i['model']}\nO'lchami: {i['size']}\nNarx: {i['price']}\nSloy: {i['layer']}"
            image_url = f"{URL}{i['imagess']}"
            await bot.send_photo(chat_id=message.chat.id, photo=image_url,caption=caption, reply_markup=create_inline_keyboard())
            await state.update_data(count_button=count_button)


@dp.message_handler(Text(equals=("📞 Aloqa")), state=UzbeklangState.CHOOSE_SIZE)
async def help_command(message: types.Message, state: FSMContext):
    urls = f"{URL}api/conferens/"
    result = requests.get(urls)
    r = result.json()
    await message.answer(f"{r[0]['bio']}")


@dp.message_handler(Text(equals=["⬅️ Orqaga"]), state=UzbeklangState.CHOOSE_SIZE)
async def get_branch(message: types.Message, state: FSMContext):
    await message.answer(
            f"Iltimos o'z avtomabilingizni tanlang!👇",
            reply_markup=none_parent_cat(a)
        )
    await UzbeklangState.CHOOSE_CATEGORY.set()




######### Rus tili uchun #########################

@dp.message_handler(Text(equals="Fura -- Фура"), state=RuslangState.CHOOSE_CATEGORY)
async def start(message: types.Message):
    await message.answer("Выберите размер👇", reply_markup=SizeCategory_Notparent_button(b))
    await RuslangState.CHOOSE_SIZE.set()


@dp.callback_query_handler(state=RuslangState.CHOOSE_SIZE)
async def handle_callback(callback_query: types.CallbackQuery, state: FSMContext):
    callback_data = callback_query.data
    data = await state.get_data()
    count_button = data.get('count_button')
    if callback_data == 'plus':
        count_button = int(count_button) + 1
        await state.update_data(count_button=count_button)
        await bot.edit_message_reply_markup(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, reply_markup=ru_create_inline_keyboard_count(count_button))
    elif callback_data == 'minus':
        if count_button>0:
            count_button = int(count_button) - 1
            await state.update_data(count_button=count_button)
        await bot.edit_message_reply_markup(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, reply_markup=ru_create_inline_keyboard_count(count_button))
        

    

@dp.message_handler(Text(equals=["Большой"]), state=RuslangState.CHOOSE_SIZE)
async def Kat_size(message: types.Message, state: FSMContext):
    urls = f"{URL}api/fura-katta-category/"
    result = requests.get(urls)
    r = result.json()
    count_button = 0
    for i in r:
        caption = f"Информация:\nБренд: {i['brend']}\nМодель: {i['model']}\nРазмер: {i['size']}\nЦена: {i['price']}\nСлой: {i['layer']}"
        image_url = f"{URL}{i['imagess']}"
        await bot.send_photo(chat_id=message.chat.id, photo=image_url,caption=caption, reply_markup=ru_create_inline_keyboard())
        await state.update_data(count_button=count_button)



@dp.message_handler(Text(equals=["Средний"]), state=RuslangState.CHOOSE_SIZE)
async def Kat_size(message: types.Message, state: FSMContext):
    urls = f"{URL}api/fura-orta-category/"
    result = requests.get(urls)
    r = result.json()
    count_button = 0
    for i in r:
            caption = f"Информация:\nБренд: {i['brend']}\nМодель: {i['model']}\nРазмер: {i['size']}\nЦена: {i['price']}\nСлой: {i['layer']}"
            image_url = f"{URL}{i['imagess']}"
            await bot.send_photo(chat_id=message.chat.id, photo=image_url,caption=caption, reply_markup=ru_create_inline_keyboard())
            await state.update_data(count_button=count_button)



@dp.message_handler(Text(equals=["Маленький"]), state=RuslangState.CHOOSE_SIZE)
async def Kat_size(message: types.Message, state: FSMContext):
    urls = f"{URL}api/fura-kichik-category/"
    result = requests.get(urls)
    r = result.json()
    count_button = 0
    for i in r:
            caption = f"Информация:\nБренд: {i['brend']}\nМодель: {i['model']}\nРазмер: {i['size']}\nЦена: {i['price']}\nСлой: {i['layer']}"
            image_url = f"{URL}{i['imagess']}"
            await bot.send_photo(chat_id=message.chat.id, photo=image_url,caption=caption, reply_markup=ru_create_inline_keyboard())
            await state.update_data(count_button=count_button)

@dp.message_handler(Text(equals=("📞 Контакты")), state=RuslangState.CHOOSE_SIZE)
async def help_command(message: types.Message, state: FSMContext):
    urls = f"{URL}api/conferens/"
    result = requests.get(urls)
    r = result.json()
    await message.answer(f"{r[1]['bio']}")



@dp.message_handler(Text(equals=["⬅️ Назад"]), state=RuslangState.CHOOSE_SIZE)
async def get_branch(message: types.Message, state: FSMContext):
    await message.answer(
            f"Пожалуйста, выберите свой автомобиль!👇",
            reply_markup=none_parent_cat(a)
        )
    await RuslangState.CHOOSE_CATEGORY.set()




















####### Lexkavoy uchun lexkavoy.py nomli file ochib ochiga shularni yozdim#############
########## O'zbek tili uchun ########################################


@dp.message_handler(Text(equals="Lexkavoy -- Лехкавой"),  state=UzbeklangState.CHOOSE_CATEGORY)
async def start(message: types.Message):
    await message.answer("O'lchamni tanlang👇", reply_markup=SizeCategory_buuton(b))
    await UzbeklangState.choose_size.set()


@dp.callback_query_handler(state=UzbeklangState.choose_size)
async def handle_callback(callback_query: types.CallbackQuery, state: FSMContext):
    callback_data = callback_query.data
    data = await state.get_data()
    count_button = data.get('count_button')
    if callback_data == 'plus':
        count_button = int(count_button) + 1
        await state.update_data(count_button=count_button)
        await bot.edit_message_reply_markup(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, reply_markup=create_inline_keyboard_count(count_button))
    elif callback_data == 'minus':
        if count_button>0:
            count_button = int(count_button) - 1
            await state.update_data(count_button=count_button)
        await bot.edit_message_reply_markup(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, reply_markup=create_inline_keyboard_count(count_button))
        


@dp.message_handler(Text(equals=["Katta"]), state=UzbeklangState.choose_size)
async def Kat_size(message: types.Message, state: FSMContext):
    urls = f"{URL}api/lexkavoy-katta-category/"
    result = requests.get(urls)
    r = result.json()
    count_button = 0
    for i in r:
            caption = f"Malumotlar:\nBrend: {i['brend']}\nModel: {i['model']}\n\nO'lchami: {i['size']}\nNarx: {i['price']}\nSloy: {i['layer']}"
            image_url = f"{URL}{i['imagess']}"
            await bot.send_photo(chat_id=message.chat.id, photo=image_url,caption=caption, reply_markup=create_inline_keyboard())
            await state.update_data(count_button=count_button)


@dp.message_handler(Text(equals=["O'rta"]), state=UzbeklangState.choose_size)
async def Kat_size(message: types.Message, state: FSMContext):
    urls = f"{URL}api/lexkavoy-orta-category/"
    result = requests.get(urls)
    r = result.json()
    count_button = 0
    for i in r:
            caption = f"Malumotlar:\nBrend: {i['brend']}\nModel: {i['model']}\nO'lchami: {i['size']}\nNarx: {i['price']}\nSloy: {i['layer']}"
            image_url = f"{URL}{i['imagess']}"
            await bot.send_photo(chat_id=message.chat.id, photo=image_url,caption=caption, reply_markup=create_inline_keyboard())
            await state.update_data(count_button=count_button)

@dp.message_handler(Text(equals=["Kichik"]), state=UzbeklangState.choose_size)
async def Kat_size(message: types.Message, state: FSMContext):
    urls = f"{URL}api/lexkavoy-kichik-category/"
    result = requests.get(urls)
    r = result.json()
    count_button = 0
    for i in r:
            caption = f"Malumotlar:\nBrend: {i['brend']}\nModel: {i['model']}\nO'lchami: {i['size']}\nNarx: {i['price']}\nSloy: {i['layer']}"
            image_url = f"{URL}{i['imagess']}"
            await bot.send_photo(chat_id=message.chat.id, photo=image_url,caption=caption, reply_markup=create_inline_keyboard())
            await state.update_data(count_button=count_button)

@dp.message_handler(Text(equals=("📞 Aloqa")), state=UzbeklangState.choose_size)
async def help_command(message: types.Message, state: FSMContext):
    urls = f"{URL}api/conferens/"
    result = requests.get(urls)
    r = result.json()
    await message.answer(f"{r[0]['bio']}")


@dp.message_handler(Text(equals=["⬅️ Orqaga"]), state=UzbeklangState.choose_size)
async def get_branch(message: types.Message, state: FSMContext):
    await message.answer(
            f"Iltimos o'z avtomabilingizni tanlang!👇",
            reply_markup=none_parent_cat(a)
        )
    await UzbeklangState.CHOOSE_CATEGORY.set()








########### Rus tili uchun ################
            


@dp.message_handler(Text(equals="Lexkavoy -- Лехкавой"),  state=RuslangState.CHOOSE_CATEGORY)
async def start(message: types.Message):
    await message.answer("Выберите размер👇", reply_markup=SizeCategory_Notparent_button(b))
    await RuslangState.choose_size.set()


@dp.callback_query_handler(state=RuslangState.choose_size)
async def handle_callback(callback_query: types.CallbackQuery, state: FSMContext):
    callback_data = callback_query.data
    data = await state.get_data()
    count_button = data.get('count_button')
    if callback_data == 'plus':
        count_button = int(count_button) + 1
        await state.update_data(count_button=count_button)
        await bot.edit_message_reply_markup(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, reply_markup=ru_create_inline_keyboard_count(count_button))
    elif callback_data == 'minus':
        if count_button>0:
            count_button = int(count_button) - 1
            await state.update_data(count_button=count_button)
        await bot.edit_message_reply_markup(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, reply_markup=ru_create_inline_keyboard_count(count_button))
        


@dp.message_handler(Text(equals=["Большой"]), state=RuslangState.choose_size)
async def Kat_size(message: types.Message, state: FSMContext):
    urls = f"{URL}api/lexkavoy-katta-category/"
    result = requests.get(urls)
    r = result.json()
    count_button = 0
    for i in r:
            caption = f"Информация:\nБренд: {i['brend']}\nМодель: {i['model']}\nРазмер: {i['size']}\nЦена: {i['price']}\nСлой: {i['layer']}"
            image_url = f"{URL}{i['imagess']}"
            await bot.send_photo(chat_id=message.chat.id, photo=image_url,caption=caption, reply_markup=ru_create_inline_keyboard())
            await state.update_data(count_button=count_button)

@dp.message_handler(Text(equals=["Средний"]), state=RuslangState.choose_size)
async def Kat_size(message: types.Message, state: FSMContext):
    urls = f"{URL}api/lexkavoy-orta-category/"
    result = requests.get(urls)
    r = result.json()
    count_button = 0
    for i in r:
            caption = f"Информация:\nБренд: {i['brend']}\nМодель: {i['model']}\nРазмер: {i['size']}\nЦена: {i['price']}\nСлой: {i['layer']}"
            image_url = f"{URL}{i['imagess']}"
            await bot.send_photo(chat_id=message.chat.id, photo=image_url,caption=caption, reply_markup=ru_create_inline_keyboard())
            await state.update_data(count_button=count_button)



@dp.message_handler(Text(equals=["Маленький"]), state=RuslangState.choose_size)
async def Kat_size(message: types.Message, state: FSMContext):
    urls = f"{URL}api/lexkavoy-kichik-category/"
    result = requests.get(urls)
    r = result.json()
    count_button = 0
    for i in r:
            caption = f"Информация:\nБренд: {i['brend']}\nМодель: {i['model']}\nРазмер: {i['size']}\nЦена: {i['price']}\nСлой: {i['layer']}"
            image_url = f"{URL}{i['imagess']}"
            await bot.send_photo(chat_id=message.chat.id, photo=image_url,caption=caption, reply_markup=ru_create_inline_keyboard())
            await state.update_data(count_button=count_button)



@dp.message_handler(Text(equals=("📞 Контакты")), state=RuslangState.choose_size)
async def help_command(message: types.Message, state: FSMContext):
    urls = f"{URL}api/conferens/"
    result = requests.get(urls)
    r = result.json()
    await message.answer(f"{r[1]['bio']}")



@dp.message_handler(Text(equals=["⬅️ Назад"]), state=RuslangState.choose_size)
async def get_branch(message: types.Message, state: FSMContext):
    await message.answer(
            f"Пожалуйста, выберите свой автомобиль!👇",
            reply_markup=none_parent_cat(a)
        )
    await RuslangState.CHOOSE_CATEGORY.set()
















####### Selxoz texnikalari uchun selxoztexnika.py nomli python file ochib ochiga shularni yozdim#############
##################### O'zbek tili uchun ################


@dp.message_handler(Text(equals="Selxoz texnika -- Сельхозтехника"),  state=UzbeklangState.CHOOSE_CATEGORY)
async def start(message: types.Message):
    await message.answer("O'lchamni tanlang👇", reply_markup=SizeCategory_buuton(b))
    await UzbeklangState.choose_siz.set()


@dp.callback_query_handler(state=UzbeklangState.choose_siz)
async def handle_callback(callback_query: types.CallbackQuery, state: FSMContext):
    callback_data = callback_query.data
    data = await state.get_data()
    count_button = data.get('count_button')
    if callback_data == 'plus':
        count_button = int(count_button) + 1
        await state.update_data(count_button=count_button)
        await bot.edit_message_reply_markup(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, reply_markup=create_inline_keyboard_count(count_button))
    elif callback_data == 'minus':
        if count_button>0:
            count_button = int(count_button) - 1
            await state.update_data(count_button=count_button)
        await bot.edit_message_reply_markup(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, reply_markup=create_inline_keyboard_count(count_button))
        


@dp.message_handler(Text(equals=["Katta"]), state=UzbeklangState.choose_siz)
async def Kat_size(message: types.Message, state: FSMContext):
    urls = f"{URL}api/selxoztexnika-katta-category/"
    result = requests.get(urls)
    r = result.json()
    count_button = 0
    for i in r:
            caption = f"Malumotlar:\nBrend: {i['brend']}\nModel: {i['model']}\nO'lchami: {i['size']}\nNarx: {i['price']}\nSloy: {i['layer']}"
            image_url = f"{URL}{i['imagess']}"
            await bot.send_photo(chat_id=message.chat.id, photo=image_url,caption=caption, reply_markup=create_inline_keyboard())
            await state.update_data(count_button=count_button)

@dp.message_handler(Text(equals=["O'rta"]), state=UzbeklangState.choose_siz)
async def Kat_size(message: types.Message, state: FSMContext):
    urls = f"{URL}api/selxoztexnika-orta-category/"
    result = requests.get(urls)
    r = result.json()
    count_button = 0
    for i in r:
            caption = f"selxoztexnika:\nBrend: {i['brend']}\nModel: {i['model']}\nO'lchami: {i['size']}\nNarx: {i['price']}\nSloy: {i['layer']}"
            image_url = f"{URL}{i['imagess']}"
            await bot.send_photo(chat_id=message.chat.id, photo=image_url,caption=caption, reply_markup=create_inline_keyboard())
            await state.update_data(count_button=count_button)



@dp.message_handler(Text(equals=["Kichik"]), state=UzbeklangState.choose_siz)
async def Kat_size(message: types.Message, state: FSMContext):
    urls = f"{URL}api/selxoztexnika-kichik-category/"
    result = requests.get(urls)
    r = result.json()
    count_button = 0
    for i in r:
            caption = f"Malumotlar:\nBrend: {i['brend']}\nModel: {i['model']}\nO'lchami: {i['size']}\nNarx: {i['price']}\nSloy: {i['layer']}"
            image_url = f"{URL}{i['imagess']}"
            await bot.send_photo(chat_id=message.chat.id, photo=image_url,caption=caption, reply_markup=create_inline_keyboard())
            await state.update_data(count_button=count_button)


@dp.message_handler(Text(equals=("📞 Aloqa")), state=UzbeklangState.choose_siz)
async def help_command(message: types.Message, state: FSMContext):
    urls = f"{URL}api/conferens/"
    result = requests.get(urls)
    r = result.json()
    await message.answer(f"{r[0]['bio']}")



@dp.message_handler(Text(equals=["⬅️ Orqaga"]), state=UzbeklangState.choose_siz)
async def get_branch(message: types.Message, state: FSMContext):
    await message.answer(
            f"Iltimos o'z avtomabilingizni tanlang!👇",
            reply_markup=none_parent_cat(a)
        )
    await UzbeklangState.CHOOSE_CATEGORY.set()





######### Rustili uchun ##################
            


            
@dp.message_handler(Text(equals="Selxoz texnika -- Сельхозтехника"),  state=RuslangState.CHOOSE_CATEGORY)
async def start(message: types.Message):
    await message.answer("Выберите размер👇", reply_markup=SizeCategory_Notparent_button(b))
    await RuslangState.choose_siz.set()


@dp.callback_query_handler(state=RuslangState.choose_siz)
async def handle_callback(callback_query: types.CallbackQuery, state: FSMContext):
    callback_data = callback_query.data
    data = await state.get_data()
    count_button = data.get('count_button')
    if callback_data == 'plus':
        count_button = int(count_button) + 1
        await state.update_data(count_button=count_button)
        await bot.edit_message_reply_markup(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, reply_markup=ru_create_inline_keyboard_count(count_button))
    elif callback_data == 'minus':
        if count_button>0:
            count_button = int(count_button) - 1
            await state.update_data(count_button=count_button)
        await bot.edit_message_reply_markup(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, reply_markup=ru_create_inline_keyboard_count(count_button))
        


@dp.message_handler(Text(equals=["Большой"]), state=RuslangState.choose_siz)
async def Kat_size(message: types.Message, state: FSMContext):
    urls = f"{URL}api/selxoztexnika-katta-category/"
    result = requests.get(urls)
    r = result.json()
    count_button = 0
    for i in r:
            caption = f"Информация:\nБренд: {i['brend']}\nМодель: {i['model']}\nРазмер: {i['size']}\nЦена: {i['price']}\nСлой: {i['layer']}"
            image_url = f"{URL}{i['imagess']}"
            await bot.send_photo(chat_id=message.chat.id, photo=image_url,caption=caption, reply_markup=ru_create_inline_keyboard())
            await state.update_data(count_button=count_button)

@dp.message_handler(Text(equals=["Средний"]), state=RuslangState.choose_siz)
async def Kat_size(message: types.Message, state: FSMContext):
    urls = f"{URL}api/selxoztexnika-orta-category/"
    result = requests.get(urls)
    r = result.json()
    count_button = 0
    for i in r:
            caption = f"Информация:\nБренд: {i['brend']}\nМодель: {i['model']}\nРазмер: {i['size']}\nЦена: {i['price']}\nСлой: {i['layer']}"
            image_url = f"{URL}{i['imagess']}"
            await bot.send_photo(chat_id=message.chat.id, photo=image_url,caption=caption, reply_markup=ru_create_inline_keyboard())
            await state.update_data(count_button=count_button)



@dp.message_handler(Text(equals=["Маленький"]), state=RuslangState.choose_siz)
async def Kat_size(message: types.Message, state: FSMContext):
    urls = f"{URL}api/selxoztexnika-kichik-category/"
    result = requests.get(urls)
    r = result.json()
    count_button = 0
    for i in r:
            caption = f"Информация:\nБренд: {i['brend']}\nМодель: {i['model']}\nРазмер: {i['size']}\nЦена: {i['price']}\nСлой: {i['layer']}"
            image_url = f"{URL}{i['imagess']}"
            await bot.send_photo(chat_id=message.chat.id, photo=image_url,caption=caption, reply_markup=ru_create_inline_keyboard())
            await state.update_data(count_button=count_button)


@dp.message_handler(Text(equals=("📞 Контакты")), state=RuslangState.choose_siz)
async def help_command(message: types.Message, state: FSMContext):
    urls = f"{URL}api/conferens/"
    result = requests.get(urls)
    r = result.json()
    await message.answer(f"{r[1]['bio']}")



@dp.message_handler(Text(equals=["⬅️ Назад"]), state=RuslangState.choose_siz)
async def get_branch(message: types.Message, state: FSMContext):
    await message.answer(
            f"Пожалуйста, выберите свой автомобиль!👇",
            reply_markup=none_parent_cat(a)
        )
    await RuslangState.CHOOSE_CATEGORY.set()













###### gruzavoy uchun gruzavoy.py nomli python file ochib ichiga shularni yozdim#########
############ O'zbek tili uchun ###################            


@dp.message_handler(Text(equals="Gruzavoy -- Грузовой"),  state=UzbeklangState.CHOOSE_CATEGORY)
async def start(message: types.Message):
    await message.answer("Mashina turini tanlang👇", reply_markup=gruzavoy_parent_cat(a))
    await UZGruzavoyState.CHOOSE_TYPE.set()




@dp.message_handler(Text(equals=("📞 Aloqa")), state=UZGruzavoyState.CHOOSE_TYPE)
async def help_command(message: types.Message, state: FSMContext):
    urls = f"{URL}api/conferens/"
    result = requests.get(urls)
    r = result.json()
    await message.answer(f"{r[0]['bio']}")


@dp.message_handler(Text(equals=["⬅️ Orqaga"]), state=UZGruzavoyState.CHOOSE_TYPE)
async def get_branch(message: types.Message, state: FSMContext):
    await message.answer(
            f"Iltimos o'z avtomabilingizni tanlang!👇",
            reply_markup=none_parent_cat(a)
        )
    await UzbeklangState.CHOOSE_CATEGORY.set()

@dp.message_handler(Text(equals=["Kamaz/zil -- Камаз/Зил"]), state=UZGruzavoyState.CHOOSE_TYPE)
async def start(message: types.Message):
    await message.answer("O'lchamni tanlang:", reply_markup=SizeCategory_buuton(b))
    await UZGruzavoyState.CHOOSE_SIZE.set()

@dp.callback_query_handler(state=UZGruzavoyState.CHOOSE_SIZE)
async def handle_callback(callback_query: types.CallbackQuery, state: FSMContext):
    callback_data = callback_query.data
    data = await state.get_data()
    count_button = data.get('count_button')
    if callback_data == 'plus':
        count_button = int(count_button) + 1
        await state.update_data(count_button=count_button)
        await bot.edit_message_reply_markup(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, reply_markup=create_inline_keyboard_count(count_button))
    elif callback_data == 'minus':
        if count_button>0:
            count_button = int(count_button) - 1
            await state.update_data(count_button=count_button)
        await bot.edit_message_reply_markup(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, reply_markup=create_inline_keyboard_count(count_button))
        


@dp.message_handler(Text(equals=["Katta"]), state=UZGruzavoyState.CHOOSE_SIZE)
async def Kat_size(message: types.Message, state: FSMContext):
    urls = f"{URL}api/kamazzil-katta-category/"
    result = requests.get(urls)
    r = result.json()
    count_button = 0
    for i in r:
            caption = f"Malumotlar:\nBrend: {i['brend']}\nModel: {i['model']}\nO'lchami: {i['size']}\nNarx: {i['price']}\nSloy: {i['layer']}"
            image_url = f"{URL}{i['imagess']}"
            await bot.send_photo(chat_id=message.chat.id, photo=image_url,caption=caption, reply_markup=create_inline_keyboard())
            await state.update_data(count_button=count_button)

@dp.message_handler(Text(equals=["O'rta"]), state=UZGruzavoyState.CHOOSE_SIZE)
async def Kat_size(message: types.Message, state: FSMContext):
    urls = f"{URL}api/kamazzil-orta-category/"
    result = requests.get(urls)
    r = result.json()
    count_button = 0
    for i in r:
            caption = f"Malumotlar:\nBrend: {i['brend']}\nModel: {i['model']}\nO'lchami: {i['size']}\nNarx: {i['price']}\nSloy: {i['layer']}"
            image_url = f"{URL}{i['imagess']}"
            await bot.send_photo(chat_id=message.chat.id, photo=image_url,caption=caption, reply_markup=create_inline_keyboard())
            await state.update_data(count_button=count_button)



@dp.message_handler(Text(equals=["Kichik"]), state=UZGruzavoyState.CHOOSE_SIZE)
async def Kat_size(message: types.Message, state: FSMContext):
    urls = f"{URL}api/kamazzil-kichik-category/"
    result = requests.get(urls)
    r = result.json()
    count_button = 0
    for i in r:
            caption = f"Malumotlar:\nBrend: {i['brend']}\nModel: {i['model']}\nO'lchami: {i['size']}\nNarx: {i['price']}\nSloy: {i['layer']}"
            image_url = f"{URL}{i['imagess']}"
            await bot.send_photo(chat_id=message.chat.id, photo=image_url,caption=caption, reply_markup=create_inline_keyboard())
            await state.update_data(count_button=count_button)



@dp.message_handler(Text(equals=("📞 Aloqa")), state=UZGruzavoyState.CHOOSE_SIZE)
async def help_command(message: types.Message, state: FSMContext):
    urls = f"{URL}api/conferens/"
    result = requests.get(urls)
    r = result.json()
    await message.answer(f"{r[0]['bio']}")


@dp.message_handler(Text(equals=["⬅️ Orqaga"]), state=UZGruzavoyState.CHOOSE_SIZE)
async def get_branch(message: types.Message, state: FSMContext):
    await message.answer(
            f"Mashina turini tanlang👇",
            reply_markup=gruzavoy_parent_cat(a)
        )
    await UZGruzavoyState.CHOOSE_TYPE.set()
    




@dp.message_handler(Text(equals=["Isizu/tral -- Исузу/трал"]), state=UZGruzavoyState.CHOOSE_TYPE)
async def start(message: types.Message):
    await message.answer("O'lchamni tanlang👇", reply_markup=SizeCategory_buuton(b))
    await UZGruzavoyState.choose_size.set()


@dp.callback_query_handler(state=UZGruzavoyState.choose_size)
async def handle_callback(callback_query: types.CallbackQuery, state: FSMContext):
    callback_data = callback_query.data
    data = await state.get_data()
    count_button = data.get('count_button')
    if callback_data == 'plus':
        count_button = int(count_button) + 1
        await state.update_data(count_button=count_button)
        await bot.edit_message_reply_markup(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, reply_markup=create_inline_keyboard_count(count_button))
    elif callback_data == 'minus':
        if count_button>0:
            count_button = int(count_button) - 1
            await state.update_data(count_button=count_button)
        await bot.edit_message_reply_markup(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, reply_markup=create_inline_keyboard_count(count_button))
        


@dp.message_handler(Text(equals=["Katta"]), state=UZGruzavoyState.choose_size)
async def Kat_size(message: types.Message, state: FSMContext):
    urls = f"{URL}api/isizutral-katta-category/"
    result = requests.get(urls)
    r = result.json()
    count_button = 0
    for i in r:
            caption = f"Malumotlar:\nBrend: {i['brend']}\nModel: {i['model']}\nO'lchami: {i['size']}\nNarx: {i['price']}\nSloy: {i['layer']}"
            image_url = f"{URL}{i['imagess']}"
            await bot.send_photo(chat_id=message.chat.id, photo=image_url,caption=caption, reply_markup=create_inline_keyboard())
            await state.update_data(count_button=count_button)

@dp.message_handler(Text(equals=["O'rta"]), state=UZGruzavoyState.choose_size)
async def Kat_size(message: types.Message, state: FSMContext):
    urls = f"{URL}api/isizutral-orta-category/"
    result = requests.get(urls)
    r = result.json()
    count_button = 0
    for i in r:
            caption = f"Malumotlar:\nBrend: {i['brend']}\nModel: {i['model']}\nO'lchami: {i['size']}\nNarx: {i['price']}\nSloy: {i['layer']}"
            image_url = f"{URL}{i['imagess']}"
            await bot.send_photo(chat_id=message.chat.id, photo=image_url,caption=caption, reply_markup=create_inline_keyboard())
            await state.update_data(count_button=count_button)



@dp.message_handler(Text(equals=["Kichik"]), state=UZGruzavoyState.choose_size)
async def Kat_size(message: types.Message, state: FSMContext):
    urls = f"{URL}api/isizutral-kichik-category/"
    result = requests.get(urls)
    r = result.json()
    count_button = 0
    for i in r:
            caption = f"Malumotlar:\nBrend: {i['brend']}\nModel: {i['model']}\nO'lchami: {i['size']}\nNarx: {i['price']}\nSloy: {i['layer']}"
            image_url = f"{URL}{i['imagess']}"
            await bot.send_photo(chat_id=message.chat.id, photo=image_url,caption=caption, reply_markup=create_inline_keyboard())
            await state.update_data(count_button=count_button)


@dp.message_handler(Text(equals=("📞 Aloqa")), state=UZGruzavoyState.choose_size)
async def help_command(message: types.Message, state: FSMContext):
    urls = f"{URL}api/conferens/"
    result = requests.get(urls)
    r = result.json()
    await message.answer(f"{r[0]['bio']}")



@dp.message_handler(Text(equals=["⬅️ Orqaga"]), state=UZGruzavoyState.choose_size)
async def get_branch(message: types.Message, state: FSMContext):
    await message.answer(
            f"Mashina turini tanlang👇",
            reply_markup=gruzavoy_parent_cat(a)
        )
    await UZGruzavoyState.CHOOSE_TYPE.set()
    



############ Rus tili uchun ################
            
@dp.message_handler(Text(equals="Gruzavoy -- Грузовой"),  state=RuslangState.CHOOSE_CATEGORY)
async def start(message: types.Message):
    await message.answer("Выберите тип машины👇", reply_markup=ru_gruzavoy_parent_cat(a))
    await RUGruzavoyState.CHOOSE_TYPE.set()



@dp.message_handler(Text(equals=("📞 Контакты")), state=RUGruzavoyState.CHOOSE_TYPE)
async def help_command(message: types.Message, state: FSMContext):
    urls = f"{URL}api/conferens/"
    result = requests.get(urls)
    r = result.json()
    await message.answer(f"{r[1]['bio']}")
    

@dp.message_handler(Text(equals=["⬅️ Назад"]), state=RUGruzavoyState.CHOOSE_TYPE)
async def get_branch(message: types.Message, state: FSMContext):
    await message.answer(
            f"Пожалуйста, выберите свой автомобиль!👇",
            reply_markup=none_parent_cat(a)
        )
    await RuslangState.CHOOSE_CATEGORY.set()


@dp.message_handler(Text(equals=["Kamaz/zil -- Камаз/Зил"]), state=RUGruzavoyState.CHOOSE_TYPE)
async def start(message: types.Message):
    await message.answer("Выберите размер👇", reply_markup=SizeCategory_Notparent_button(b))
    await RUGruzavoyState.CHOOSE_SIZE.set()

@dp.callback_query_handler(state=RUGruzavoyState.CHOOSE_SIZE)
async def handle_callback(callback_query: types.CallbackQuery, state: FSMContext):
    callback_data = callback_query.data
    data = await state.get_data()
    count_button = data.get('count_button')
    if callback_data == 'plus':
        count_button = int(count_button) + 1
        await state.update_data(count_button=count_button)
        await bot.edit_message_reply_markup(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, reply_markup=ru_create_inline_keyboard_count(count_button))
    elif callback_data == 'minus':
        if count_button>0:
            count_button = int(count_button) - 1
            await state.update_data(count_button=count_button)
        await bot.edit_message_reply_markup(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, reply_markup=ru_create_inline_keyboard_count(count_button))
        


@dp.message_handler(Text(equals=["Большой"]), state=RUGruzavoyState.CHOOSE_SIZE)
async def Kat_size(message: types.Message, state: FSMContext):
    urls = f"{URL}api/kamazzil-katta-category/"
    result = requests.get(urls)
    r = result.json()
    count_button = 0
    for i in r:
            caption = f"Информация:\nБренд: {i['brend']}\nМодель: {i['model']}\nРазмер: {i['size']}\nЦена: {i['price']}\nСлой: {i['layer']}"
            image_url = f"{URL}{i['imagess']}"
            await bot.send_photo(chat_id=message.chat.id, photo=image_url,caption=caption, reply_markup=ru_create_inline_keyboard())
            await state.update_data(count_button=count_button)


@dp.message_handler(Text(equals=["Средний"]), state=RUGruzavoyState.CHOOSE_SIZE)
async def Kat_size(message: types.Message, state: FSMContext):
    urls = f"{URL}api/kamazzil-orta-category/"
    result = requests.get(urls)
    r = result.json()
    count_button = 0
    for i in r:
            caption = f"Информация:\nБренд: {i['brend']}\nМодель: {i['model']}\nРазмер: {i['size']}\nЦена: {i['price']}\nСлой: {i['layer']}"
            image_url = f"{URL}{i['imagess']}"
            await bot.send_photo(chat_id=message.chat.id, photo=image_url,caption=caption, reply_markup=ru_create_inline_keyboard())
            await state.update_data(count_button=count_button)



@dp.message_handler(Text(equals=["Маленький"]), state=RUGruzavoyState.CHOOSE_SIZE)
async def Kat_size(message: types.Message, state: FSMContext):
    urls = f"{URL}api/kamazzil-kichik-category/"
    result = requests.get(urls)
    r = result.json()
    count_button = 0
    for i in r:
            caption = f"Информация:\nБренд: {i['brend']}\nМодель: {i['model']}\nРазмер: {i['size']}\nЦена: {i['price']}\nСлой: {i['layer']}"
            image_url = f"{URL}{i['imagess']}"
            await bot.send_photo(chat_id=message.chat.id, photo=image_url,caption=caption, reply_markup=ru_create_inline_keyboard())
            await state.update_data(count_button=count_button)




@dp.message_handler(Text(equals=("📞 Контакты")), state=RUGruzavoyState.CHOOSE_SIZE)
async def help_command(message: types.Message, state: FSMContext):
    urls = f"{URL}api/conferens/"
    result = requests.get(urls)
    r = result.json()
    await message.answer(f"{r[1]['bio']}")



@dp.message_handler(Text(equals=["⬅️ Назад"]), state=RUGruzavoyState.CHOOSE_SIZE)
async def get_branch(message: types.Message, state: FSMContext):
    await message.answer(
            f"Выберите тип машины👇",
            reply_markup=ru_gruzavoy_parent_cat(a)
        )
    await RUGruzavoyState.CHOOSE_TYPE.set()






@dp.message_handler(Text(equals=["Isizu/tral -- Исузу/трал"]), state=RUGruzavoyState.CHOOSE_TYPE)
async def start(message: types.Message):
    await message.answer("Выберите размер👇", reply_markup=SizeCategory_Notparent_button(b))
    await RUGruzavoyState.choose_size.set()


@dp.callback_query_handler(state=RUGruzavoyState.choose_size)
async def handle_callback(callback_query: types.CallbackQuery, state: FSMContext):
    callback_data = callback_query.data
    data = await state.get_data()
    count_button = data.get('count_button')
    if callback_data == 'plus':
        count_button = int(count_button) + 1
        await state.update_data(count_button=count_button)
        await bot.edit_message_reply_markup(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, reply_markup=ru_create_inline_keyboard_count(count_button))
    elif callback_data == 'minus':
        if count_button>0:
            count_button = int(count_button) - 1
            await state.update_data(count_button=count_button)
        await bot.edit_message_reply_markup(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, reply_markup=ru_create_inline_keyboard_count(count_button))
        


@dp.message_handler(Text(equals=["Большой"]), state=RUGruzavoyState.choose_size)
async def Kat_size(message: types.Message, state: FSMContext):
    urls = f"{URL}api/isizutral-katta-category/"
    result = requests.get(urls)
    r = result.json()
    count_button = 0
    for i in r:
            caption = f"Информация:\nБренд: {i['brend']}\nМодель: {i['model']}\nРазмер: {i['size']}\nЦена: {i['price']}\nСлой: {i['layer']}"
            image_url = f"{URL}{i['imagess']}"
            await bot.send_photo(chat_id=message.chat.id, photo=image_url,caption=caption, reply_markup=ru_create_inline_keyboard())
            await state.update_data(count_button=count_button)

@dp.message_handler(Text(equals=["Средний"]), state=RUGruzavoyState.choose_size)
async def Kat_size(message: types.Message, state: FSMContext):
    urls = f"{URL}api/isizutral-orta-category/"
    result = requests.get(urls)
    r = result.json()
    count_button = 0
    for i in r:
            caption = f"Информация:\nБренд: {i['brend']}\nМодель: {i['model']}\nРазмер: {i['size']}\nЦена: {i['price']}\nСлой: {i['layer']}"
            image_url = f"{URL}{i['imagess']}"
            await bot.send_photo(chat_id=message.chat.id, photo=image_url,caption=caption, reply_markup=ru_create_inline_keyboard())
            await state.update_data(count_button=count_button)



@dp.message_handler(Text(equals=["Маленький"]), state=RUGruzavoyState.choose_size)
async def Kat_size(message: types.Message, state: FSMContext):
    urls = f"{URL}api/isizutral-kichik-category/"
    result = requests.get(urls)
    r = result.json()
    count_button = 0
    for i in r:
            caption = f"Информация:\nБренд: {i['brend']}\nМодель: {i['model']}\nРазмер: {i['size']}\nЦена: {i['price']}\nСлой: {i['layer']}"
            image_url = f"{URL}{i['imagess']}"
            await bot.send_photo(chat_id=message.chat.id, photo=image_url,caption=caption, reply_markup=ru_create_inline_keyboard())
            await state.update_data(count_button=count_button)




@dp.message_handler(Text(equals=("📞 Контакты")), state=RUGruzavoyState.choose_size)
async def help_command(message: types.Message, state: FSMContext):
    urls = f"{URL}api/conferens/"
    result = requests.get(urls)
    r = result.json()
    await message.answer(f"{r[1]['bio']}")



@dp.message_handler(Text(equals=["⬅️ Назад"]), state=RUGruzavoyState.choose_size)
async def get_branch(message: types.Message, state: FSMContext):
    await message.answer(
            f"Выберите тип машины👇",
            reply_markup=ru_gruzavoy_parent_cat(a)
        )
    await RUGruzavoyState.CHOOSE_TYPE.set()









###### Spestexnikalari uchun spestexnika.py nomli python file ochib ichiga shularni yozdim#########
            

@dp.message_handler(Text(equals="Spestexnika -- Cпециальная техника"),  state=UzbeklangState.CHOOSE_CATEGORY)
async def start(message: types.Message):
    await message.answer("Mashina turini tanlang👇", reply_markup=spestexnika_parent_cat(a))
    await UZSpestexnikaState.CHOOSE_TYPE.set()




@dp.message_handler(Text(equals=("📞 Aloqa")), state=UZSpestexnikaState.CHOOSE_TYPE)
async def help_command(message: types.Message, state: FSMContext):
    urls = f"{URL}api/conferens/"
    result = requests.get(urls)
    r = result.json()
    await message.answer(f"{r[0]['bio']}")


@dp.message_handler(Text(equals=["⬅️ Orqaga"]), state=UZSpestexnikaState.CHOOSE_TYPE)
async def get_branch(message: types.Message, state: FSMContext):
    await message.answer(
            f"Iltimos o'z avtomabilingizni tanlang!👇",
            reply_markup=none_parent_cat(a)
        )
    await UzbeklangState.CHOOSE_CATEGORY.set()


@dp.message_handler(Text(equals=["Kara -- Кара"]), state=UZSpestexnikaState.CHOOSE_TYPE)
async def start(message: types.Message):
    await message.answer("O'lchamni tanlang👇", reply_markup=SizeCategory_buuton(b))
    await UZSpestexnikaState.CHOOSE_SIZE.set()


@dp.callback_query_handler(state=UZSpestexnikaState.CHOOSE_SIZE)
async def handle_callback(callback_query: types.CallbackQuery, state: FSMContext):
    callback_data = callback_query.data
    data = await state.get_data()
    count_button = data.get('count_button')
    if callback_data == 'plus':
        count_button = int(count_button) + 1
        await state.update_data(count_button=count_button)
        await bot.edit_message_reply_markup(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, reply_markup=create_inline_keyboard_count(count_button))
    elif callback_data == 'minus':
        if count_button>0:
            count_button = int(count_button) - 1
            await state.update_data(count_button=count_button)
        await bot.edit_message_reply_markup(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, reply_markup=create_inline_keyboard_count(count_button))
        


@dp.message_handler(Text(equals=["Katta"]), state=UZSpestexnikaState.CHOOSE_SIZE)
async def Kat_size(message: types.Message, state: FSMContext):
    urls = f"{URL}api/kara-katta-category/"
    result = requests.get(urls)
    r = result.json()
    count_button = 0
    for i in r:
            caption = f"Malumotlar:\nBrend: {i['brend']}\nModel: {i['model']}\nO'lchami: {i['size']}\nNarx: {i['price']}\nSloy: {i['layer']}"
            image_url = f"{URL}{i['imagess']}"
            await bot.send_photo(chat_id=message.chat.id, photo=image_url,caption=caption, reply_markup=create_inline_keyboard())
            await state.update_data(count_button=count_button)

@dp.message_handler(Text(equals=["O'rta"]), state=UZSpestexnikaState.CHOOSE_SIZE)
async def Kat_size(message: types.Message, state: FSMContext):
    urls = f"{URL}api/kara-orta-category/"
    result = requests.get(urls)
    r = result.json()
    count_button = 0
    for i in r:
            caption = f"Malumotlar:\nBrend: {i['brend']}\nModel: {i['model']}\nO'lchami: {i['size']}\nNarx: {i['price']}\nSloy: {i['layer']}"
            image_url = f"{URL}{i['imagess']}"
            await bot.send_photo(chat_id=message.chat.id, photo=image_url,caption=caption, reply_markup=create_inline_keyboard())
            await state.update_data(count_button=count_button)



@dp.message_handler(Text(equals=["Kichik"]), state=UZSpestexnikaState.CHOOSE_SIZE)
async def Kat_size(message: types.Message, state: FSMContext):
    urls = f"{URL}api/kara-kichik-category/"
    result = requests.get(urls)
    r = result.json()
    count_button = 0
    for i in r:
            caption = f"Malumotlar:\nBrend: {i['brend']}\nModel: {i['model']}\nO'lchami: {i['size']}\nNarx: {i['price']}\nSloy: {i['layer']}"
            image_url = f"{URL}{i['imagess']}"
            await bot.send_photo(chat_id=message.chat.id, photo=image_url,caption=caption, reply_markup=create_inline_keyboard())
            await state.update_data(count_button=count_button)


@dp.message_handler(Text(equals=("📞 Aloqa")), state=UZSpestexnikaState.CHOOSE_SIZE)
async def help_command(message: types.Message, state: FSMContext):
    urls = f"{URL}api/conferens/"
    result = requests.get(urls)
    r = result.json()
    await message.answer(f"{r[0]['bio']}")



@dp.message_handler(Text(equals=["⬅️ Orqaga"]), state=UZSpestexnikaState.CHOOSE_SIZE)
async def get_branch(message: types.Message, state: FSMContext):
    await message.answer(
            f"Mashina turini tanlang👇",
            reply_markup=spestexnika_parent_cat(a)
        )
    await UZSpestexnikaState.CHOOSE_TYPE.set()



@dp.message_handler(Text(equals=["Avto pagruzchik -- Авто пагрузчик"]), state=UZSpestexnikaState.CHOOSE_TYPE)
async def start(message: types.Message):
    await message.answer("O'lchamni tanlang👇", reply_markup=SizeCategory_buuton(b))
    await UZSpestexnikaState.choose_size.set()

@dp.callback_query_handler(state=UZSpestexnikaState.choose_size)
async def handle_callback(callback_query: types.CallbackQuery, state: FSMContext):
    callback_data = callback_query.data
    data = await state.get_data()
    count_button = data.get('count_button')
    if callback_data == 'plus':
        count_button = int(count_button) + 1
        await state.update_data(count_button=count_button)
        await bot.edit_message_reply_markup(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, reply_markup=create_inline_keyboard_count(count_button))
    elif callback_data == 'minus':
        if count_button>0:
            count_button = int(count_button) - 1
            await state.update_data(count_button=count_button)
        await bot.edit_message_reply_markup(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, reply_markup=create_inline_keyboard_count(count_button))
       


@dp.message_handler(Text(equals=["Katta"]), state=UZSpestexnikaState.choose_size)
async def Kat_size(message: types.Message, state: FSMContext):
    urls = f"{URL}api/avtopagruschik-katta-category/"
    result = requests.get(urls)
    r = result.json()
    count_button = 0
    for i in r:
            caption = f"Malumotlar:\nBrend: {i['brend']}\nModel: {i['model']}\nO'lchami: {i['size']}\nNarx: {i['price']}\nSloy: {i['layer']}"
            image_url = f"{URL}{i['imagess']}"
            await bot.send_photo(chat_id=message.chat.id, photo=image_url,caption=caption, reply_markup=create_inline_keyboard())
            await state.update_data(count_button=count_button)

@dp.message_handler(Text(equals=["O'rta"]), state=UZSpestexnikaState.choose_size)
async def Kat_size(message: types.Message, state: FSMContext):
    urls = f"{URL}api/avtopagruschik-orta-category/"
    result = requests.get(urls)
    r = result.json()
    count_button = 0
    for i in r:
            caption = f"Malumotlar:\nBrend: {i['brend']}\nModel: {i['model']}\nO'lchami: {i['size']}\nNarx: {i['price']}\nSloy: {i['layer']}"
            image_url = f"{URL}{i['imagess']}"
            await bot.send_photo(chat_id=message.chat.id, photo=image_url,caption=caption, reply_markup=create_inline_keyboard())
            await state.update_data(count_button=count_button)



@dp.message_handler(Text(equals=["Kichik"]), state=UZSpestexnikaState.choose_size)
async def Kat_size(message: types.Message, state: FSMContext):
    urls = f"{URL}api/avtopagruschik-kichik-category/"
    result = requests.get(urls)
    r = result.json()
    count_button = 0
    for i in r:
            caption = f"Malumotlar:\nBrend: {i['brend']}\nModel: {i['model']}\nO'lchami: {i['size']}\nNarx: {i['price']}\nSloy: {i['layer']}"
            image_url = f"{URL}{i['imagess']}"
            await bot.send_photo(chat_id=message.chat.id, photo=image_url,caption=caption, reply_markup=create_inline_keyboard())
            await state.update_data(count_button=count_button)


@dp.message_handler(Text(equals=("📞 Aloqa")), state=UZSpestexnikaState.choose_size)
async def help_command(message: types.Message, state: FSMContext):
    urls = f"{URL}api/conferens/"
    result = requests.get(urls)
    r = result.json()
    await message.answer(f"{r[0]['bio']}")



@dp.message_handler(Text(equals=["⬅️ Orqaga"]), state=UZSpestexnikaState.choose_size)
async def get_branch(message: types.Message, state: FSMContext):
    await message.answer(
            f"Mashina turini tanlang👇",
            reply_markup=spestexnika_parent_cat(a)
        )
    await UZSpestexnikaState.CHOOSE_TYPE.set()




####### Rus tili uchun ##############
    

@dp.message_handler(Text(equals="Spestexnika -- Cпециальная техника"),  state=RuslangState.CHOOSE_CATEGORY)
async def start(message: types.Message):
    await message.answer("Выберите тип машины👇", reply_markup=ru_spestexnika_parent_cat(a))
    await RUSpestexnikaState.CHOOSE_TYPE.set()


@dp.message_handler(Text(equals=("📞 Контакты")), state=RUSpestexnikaState.CHOOSE_TYPE)
async def help_command(message: types.Message, state: FSMContext):
    urls = f"{URL}api/conferens/"
    result = requests.get(urls)
    r = result.json()
    await message.answer(f"{r[1]['bio']}")


@dp.message_handler(Text(equals=["⬅️ Назад"]), state=RUSpestexnikaState.CHOOSE_TYPE)
async def get_branch(message: types.Message, state: FSMContext):
    await message.answer(
            f"Пожалуйста, выберите свой автомобиль!👇",
            reply_markup=none_parent_cat(a)
        )
    await RuslangState.CHOOSE_CATEGORY.set()




@dp.message_handler(Text(equals=["Kara -- Кара"]), state=RUSpestexnikaState.CHOOSE_TYPE)
async def start(message: types.Message):
    await message.answer("Выберите размер👇", reply_markup=SizeCategory_Notparent_button(b))
    await RUSpestexnikaState.CHOOSE_SIZE.set()


@dp.callback_query_handler(state=RUSpestexnikaState.CHOOSE_SIZE)
async def handle_callback(callback_query: types.CallbackQuery, state: FSMContext):
    callback_data = callback_query.data
    data = await state.get_data()
    count_button = data.get('count_button')
    if callback_data == 'plus':
        count_button = int(count_button) + 1
        await state.update_data(count_button=count_button)
        await bot.edit_message_reply_markup(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, reply_markup=ru_create_inline_keyboard_count(count_button))
    elif callback_data == 'minus':
        if count_button>0:
            count_button = int(count_button) - 1
            await state.update_data(count_button=count_button)
        await bot.edit_message_reply_markup(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, reply_markup=ru_create_inline_keyboard_count(count_button))
       


@dp.message_handler(Text(equals=["Большой"]), state=RUSpestexnikaState.CHOOSE_SIZE)
async def Kat_size(message: types.Message, state: FSMContext):
    urls = f"{URL}api/kara-katta-category/"
    result = requests.get(urls)
    r = result.json()
    count_button = 0
    for i in r:
            caption = f"Информация:\nБренд: {i['brend']}\nМодель: {i['model']}\nРазмер: {i['size']}\nЦена: {i['price']}\nСлой: {i['layer']}"
            image_url = f"{URL}{i['imagess']}"
            await bot.send_photo(chat_id=message.chat.id, photo=image_url,caption=caption, reply_markup=ru_create_inline_keyboard())
            await state.update_data(count_button=count_button)

@dp.message_handler(Text(equals=["Средний"]), state=RUSpestexnikaState.CHOOSE_SIZE)
async def Kat_size(message: types.Message, state: FSMContext):
    urls = f"{URL}api/kara-orta-category/"
    result = requests.get(urls)
    r = result.json()
    count_button = 0
    for i in r:
            caption = f"Информация:\nБренд: {i['brend']}\nМодель: {i['model']}\nРазмер: {i['size']}\nЦена: {i['price']}\nСлой: {i['layer']}"
            image_url = f"{URL}{i['imagess']}"
            await bot.send_photo(chat_id=message.chat.id, photo=image_url,caption=caption, reply_markup=ru_create_inline_keyboard())
            await state.update_data(count_button=count_button)



@dp.message_handler(Text(equals=["Маленький"]), state=RUSpestexnikaState.CHOOSE_SIZE)
async def Kat_size(message: types.Message, state: FSMContext):
    urls = f"{URL}api/kara-kichik-category/"
    result = requests.get(urls)
    r = result.json()
    count_button = 0
    for i in r:
            caption = f"Информация:\nБренд: {i['brend']}\nМодель: {i['model']}\nРазмер: {i['size']}\nЦена: {i['price']}\nСлой: {i['layer']}"
            image_url = f"{URL}{i['imagess']}"
            await bot.send_photo(chat_id=message.chat.id, photo=image_url,caption=caption, reply_markup=ru_create_inline_keyboard())
            await state.update_data(count_button=count_button)




@dp.message_handler(Text(equals=("📞 Контакты")), state=RUSpestexnikaState.CHOOSE_SIZE)
async def help_command(message: types.Message, state: FSMContext):
    urls = f"{URL}api/conferens/"
    result = requests.get(urls)
    r = result.json()
    await message.answer(f"{r[1]['bio']}")




@dp.message_handler(Text(equals=["⬅️ Назад"]), state=RUSpestexnikaState.CHOOSE_SIZE)
async def get_branch(message: types.Message, state: FSMContext):
    await message.answer(
            f"Выберите тип машины👇",
            reply_markup=ru_spestexnika_parent_cat(a)
        )
    await RUSpestexnikaState.CHOOSE_TYPE.set()





@dp.message_handler(Text(equals=["Avto pagruzchik -- Авто пагрузчик"]), state=RUSpestexnikaState.CHOOSE_TYPE)
async def start(message: types.Message):
    await message.answer("Выберите размер👇", reply_markup=SizeCategory_Notparent_button(b))
    await RUSpestexnikaState.choose_size.set()



@dp.callback_query_handler(state=RUSpestexnikaState.choose_size)
async def handle_callback(callback_query: types.CallbackQuery, state: FSMContext):
    callback_data = callback_query.data
    data = await state.get_data()
    count_button = data.get('count_button')
    if callback_data == 'plus':
        count_button = int(count_button) + 1
        await state.update_data(count_button=count_button)
        await bot.edit_message_reply_markup(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, reply_markup=ru_create_inline_keyboard_count(count_button))
    elif callback_data == 'minus':
        if count_button>0:
            count_button = int(count_button) - 1
            await state.update_data(count_button=count_button)
        await bot.edit_message_reply_markup(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, reply_markup=ru_create_inline_keyboard_count(count_button))
       

@dp.message_handler(Text(equals=["Большой"]), state=RUSpestexnikaState.choose_size)
async def Kat_size(message: types.Message, state: FSMContext):
    urls = f"{URL}api/avtopagruschik-katta-category/"
    result = requests.get(urls)
    r = result.json()
    count_button = 0
    for i in r:
            caption = f"Malumotlar:\nBrend: {i['brend']}\nModel: {i['model']}\nO'lchami: {i['size']}\nNarx: {i['price']}\nSloy: {i['layer']}"
            image_url = f"{URL}{i['imagess']}"
            await bot.send_photo(chat_id=message.chat.id, photo=image_url,caption=caption, reply_markup=ru_create_inline_keyboard())
            await state.update_data(count_button=count_button)


@dp.message_handler(Text(equals=["Средний"]), state=RUSpestexnikaState.choose_size)
async def Kat_size(message: types.Message, state: FSMContext):
    urls = f"{URL}api/avtopagruschik-orta-category/"
    result = requests.get(urls)
    r = result.json()
    count_button = 0
    for i in r:
            caption = f"Malumotlar:\nBrend: {i['brend']}\nModel: {i['model']}\nO'lchami: {i['size']}\nNarx: {i['price']}\nSloy: {i['layer']}"
            image_url = f"{URL}{i['imagess']}"
            await bot.send_photo(chat_id=message.chat.id, photo=image_url,caption=caption, reply_markup=ru_create_inline_keyboard())
            await state.update_data(count_button=count_button)




@dp.message_handler(Text(equals=["Маленький"]), state=RUSpestexnikaState.choose_size)
async def Kat_size(message: types.Message, state: FSMContext):
    urls = f"{URL}api/avtopagruschik-kichik-category/"
    result = requests.get(urls)
    r = result.json()
    count_button = 0
    for i in r:
            caption = f"Malumotlar:\nBrend: {i['brend']}\nModel: {i['model']}\nO'lchami: {i['size']}\nNarx: {i['price']}\nSloy: {i['layer']}"
            image_url = f"{URL}{i['imagess']}"
            await bot.send_photo(chat_id=message.chat.id, photo=image_url,caption=caption, reply_markup=ru_create_inline_keyboard())
            await state.update_data(count_button=count_button)




@dp.message_handler(Text(equals=("📞 Контакты")), state=RUSpestexnikaState.choose_size)
async def help_command(message: types.Message, state: FSMContext):
    urls = f"{URL}api/conferens/"
    result = requests.get(urls)
    r = result.json()
    await message.answer(f"{r[1]['bio']}")


@dp.message_handler(Text(equals=["⬅️ Назад"]), state=RUSpestexnikaState.choose_size)
async def get_branch(message: types.Message, state: FSMContext):
    await message.answer(
            f"Выберите тип машины👇",
            reply_markup=ru_spestexnika_parent_cat(a)
        )
    await RUSpestexnikaState.CHOOSE_TYPE.set()





    

if __name__ =="__main__":
    logging.info("Bot ishga tushirildi.")
    executor.start_polling(dispatcher=dp, skip_updates=True)