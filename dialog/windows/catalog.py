from aiogram.types import CallbackQuery
from aiogram_dialog import Window, DialogManager
from aiogram_dialog.widgets.media import DynamicMedia
from aiogram_dialog.widgets.text import Const, Format, Case
from aiogram_dialog.widgets.kbd import Button, Url, ListGroup
from dialog.user_sg import UserSG
from dialog.custom_widgets.switch_inline_query_current_chat import SwitchInlineQueryCurrentChat


async def click_catalog(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    await dialog_manager.switch_to(state=UserSG.catalog)

async def click_back(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    await dialog_manager.switch_to(state=UserSG.menu)

async def get_data(dialog_manager: DialogManager, **kwargs):
   data = {"media": MediaAttachment(ContentType.PHOTO, path="media/catalog.png"),
           "categories": [("Мужская", "Мужская"),
                          ("Женская", "Женская"),
                          ("Детская", "Детская")]}
   return data

window = Window(
    DynamicMedia("media"),
    Const("Выберите категорию товара"),
    ListGroup(
        SwitchInlineQueryCurrentChat(
            Format("{item[0]}"),
            Format("{item[1]}"),
        ),
        id="lg",
        item_id_getter=str,
        items="categories",
    ),
    Button(
        text=Const("Каталог"),
        id="button_catalog",
        on_click=click_catalog,
    ),
    Button(
        text=Const("Назад"),
        id="button_back",
        on_click=click_back,
    ),
    state=UserSG.catalog,
    getter=get_data,
)