from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from config import  URL
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import requests
from aiogram import types











category_urls = f"{URL}api/category-list/"
resullt = requests.get(category_urls)
if resullt.status_code == 200:
    a = resullt.json()
else:
    a = {}
def none_parent_cat(a):
    reply_buttons = ReplyKeyboardMarkup(resize_keyboard=True)
    row=[]
    for i in a:
        d=i['parent']
        if d==None: 
            b=i['name']
            knopka = KeyboardButton(text=b)
            row.append(knopka)
            if len(row)==2:
                reply_buttons.row(*row)
                row = []
    if row:
        reply_buttons.row(*row)

    return reply_buttons

    
def gruzavoy_parent_cat(a):
    reply_button = ReplyKeyboardMarkup(resize_keyboard=True)
    row=[]
    for i in a:
        d=i['parent']
        if d==1: 
            b=i['name']
            knopka = KeyboardButton(text=b)
            to_back = KeyboardButton(text="⬅️ Orqaga")
            to_help = KeyboardButton(text= "📞 Aloqa")
            karzina = KeyboardButton(text="🛒 Savatcham")
            row.append(knopka)
            if len(row)==2:
                reply_button.row(*row)
                row = []
    row.append(to_back)
    row.append(to_help)
    row.append(karzina)
    if row:
        reply_button.row(*row)

    return reply_button

###### Rus gruzavoy ######
    ##Моя корзина
def ru_gruzavoy_parent_cat(a):
    reply_button = ReplyKeyboardMarkup(resize_keyboard=True)
    row=[]
    for i in a:
        d=i['parent']
        if d==1: 
            b=i['name']
            knopka = KeyboardButton(text=b)
            to_back = KeyboardButton(text="⬅️ Назад")
            to_help = KeyboardButton(text="📞 Контакты")
            karzina = KeyboardButton(text="🛒 Моя корзина")
            row.append(knopka)
            if len(row)==2:
                reply_button.row(*row)
                row = []
    row.append(to_back)
    row.append(to_help)
    row.append(karzina)
    if row:
        reply_button.row(*row)

    return reply_button


def spestexnika_parent_cat(a):
    reply_button = ReplyKeyboardMarkup(resize_keyboard=True)
    row=[]
    for i in a:
        d=i['parent']
        if d==2: 
            b=i['name']
            knopka = KeyboardButton(text=b)
            to_back = KeyboardButton(text="⬅️ Orqaga")
            to_help = KeyboardButton(text= "📞 Aloqa")
            karzina = KeyboardButton(text="🛒 Savatcham")
            row.append(knopka)
            if len(row)==2:
                reply_button.row(*row)
                row = []
    row.append(to_back)
    row.append(to_help)
    row.append(karzina)
    if row:
        reply_button.row(*row)

    return reply_button

### Rus Gruzavoy uchun ##### 

def ru_spestexnika_parent_cat(a):
    reply_button = ReplyKeyboardMarkup(resize_keyboard=True)
    row=[]
    for i in a:
        d=i['parent']
        if d==2: 
            b=i['name']
            knopka = KeyboardButton(text=b)
            to_back = KeyboardButton(text="⬅️ Назад")
            to_help = KeyboardButton(text= "📞 Контакты")
            karzina = KeyboardButton(text="🛒 Моя корзина")
            row.append(knopka)
            if len(row)==2:
                reply_button.row(*row)
                row = []
    row.append(to_back)
    row.append(to_help)
    row.append(karzina)
    if row:
        reply_button.row(*row)

    return reply_button



size_category_url = f"{URL}api/size-category-list/"
results = requests.get(size_category_url)
if results.status_code == 200:
    b= results.json()
else:
    b={}
def SizeCategory_buuton(b):
    reply_button = ReplyKeyboardMarkup(resize_keyboard=True)
    row=[]
    for i in b:
        d=i['parent']
        if d==None: 
            c=i['differens']
            knopka = KeyboardButton(text=c)
            to_back =KeyboardButton(text="⬅️ Orqaga")
            to_help = KeyboardButton(text= "📞 Aloqa")
            karzina = KeyboardButton(text="🛒 Savatcham")
            row.append(knopka)          
            if len(row)==3:
                reply_button.row(*row)
                row = []
    row.append(to_back)
    row.append(to_help)
    row.append(karzina)
    if row:
        reply_button.row(*row)

    return reply_button





size_category_url = f"{URL}api/size-category-list/"
resullts = requests.get(size_category_url)
if resullts.status_code==200:
    b = resullts.json()
else:
    b={}

def SizeCategory_Notparent_button(b):
    reply_button = ReplyKeyboardMarkup(resize_keyboard=True)
    row=[]
    for i in b:
        d=i['parent']
        if d!=None: 
            c=i['differens']
            knopka = KeyboardButton(text=c)
            to_back = KeyboardButton(text="⬅️ Назад")
            to_help = KeyboardButton(text= "📞 Контакты")
            karzina = KeyboardButton(text="🛒 Моя корзина")
            row.append(knopka)
            if len(row)==3:
                reply_button.row(*row)
                row = []
    row.append(to_back)
    row.append(to_help)
    row.append(karzina)
    if row:
        reply_button.row(*row)

    return reply_button


def generate_quantity_keyboard(product_id, quantity) -> types.InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup()

    btn_decrease = InlineKeyboardButton("-", callback_data=f"decrease_{product_id}")
    btn_increase = InlineKeyboardButton("+", callback_data=f"increase_{product_id}")
    btn_cart = InlineKeyboardButton("Savatga qo'shish",
                                    callback_data=f"add_to_cart_{product_id}")

    keyboard.row(btn_decrease,
                 InlineKeyboardButton(str(quantity), callback_data="quantity"),
                 btn_increase)

    return keyboard.add(btn_cart)

