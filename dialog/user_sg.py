from aiogram.fsm.state import State, StatesGroup

class UserSG(StatesGroup):
    menu = State()
    catalog = State()
    product = State()
    cart = State()
    delivery = State()
    fullname = State()
    address = State()
    phone = State()
    email = State()
    payment_method = State()
    order = State()