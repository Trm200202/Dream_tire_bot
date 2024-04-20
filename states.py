from aiogram.dispatcher.filters.state import State, StatesGroup






class OrderProductState(StatesGroup):
    select_product = State()


class UzbeklangState(StatesGroup):
    ask_name = State()
    ask_phone = State()
    CHOOSE_CATEGORY = State()
    CHOOSE_TYPE = State()
    CHOOSE_SIZE = State()
    choose_size = State()
    choose_siz = State()
    select_product = State()
    


class UZSpestexnikaState(StatesGroup):
    CHOOSE_TYPE = State()
    CHOOSE_SIZE = State()
    choose_size = State()

class UZGruzavoyState(StatesGroup):
    CHOOSE_TYPE = State()
    CHOOSE_SIZE = State()
    choose_size = State()

class RUSpestexnikaState(StatesGroup):
    CHOOSE_TYPE = State()
    CHOOSE_SIZE = State()
    choose_size = State()

class RUGruzavoyState(StatesGroup):
    CHOOSE_TYPE = State()
    CHOOSE_SIZE = State()
    choose_size = State()


class RuslangState(StatesGroup):
    ask_imya = State()
    ask_tel = State()
    CHOOSE_CATEGORY = State()
    CHOOSE_TYPE = State()
    CHOOSE_SIZE = State()
    choose_size = State()
    choose_siz = State()


class OrderProductState(StatesGroup):
    select_product = State()
    set_quantity = State()

class CartState(StatesGroup):
    cart = State()
    buyurtma = State()

class RUOrderProductState(StatesGroup):
    select_product = State()
    set_quantity = State()

class RUCartState(StatesGroup):
    cart = State()
    buyurtma = State()