from aiogram.types import CallbackQuery
from aiogram_dialog import Window, DialogManager
from aiogram_dialog.widgets.media import DynamicMedia
from aiogram_dialog.widgets.text import Const, Format, Case
from aiogram_dialog.widgets.kbd import Button, Url
from dialog.user_sg import UserSG


async def click_catalog(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    await dialog_manager.switch_to(state=UserSG.catalog)

async def get_data(dialog_manager: DialogManager, **kwargs):
   data = {"media": MediaAttachment(ContentType.PHOTO, path="media/menu.png")}

window = Window(
    DynamicMedia("media"),
    Const("Добро пожаловать в магазин футболок!"),
    Button(
        text=Const("Каталог"),
        id="button_catalog",
        on_click=click_catalog,
    ),
    Url(
        text=Const("Менеджер"),
        id="button_manager_url",
        url=Const("https://google.com/"),
    ),
    state=UserSG.menu,
    getter=UserSG.get_data,

)