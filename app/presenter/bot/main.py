import asyncio
import logging

from aiogram import (
    Bot,
    Dispatcher,
    F,
    types,
)
from aiogram.client.default import DefaultBotProperties
from aiogram.exceptions import TelegramBadRequest
from aiogram.filters import CommandStart
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from app.infrastructure.database.utils import (
    db_clear_finally_cart,
    db_create_user_cart,
    db_delete_product,
    db_get_product_by_id,
    db_get_product_by_name,
    db_get_user_cart,
    db_get_user_info,
    db_ins_or_upd_finally_cart,
    db_register_user,
    db_update_to_cart,
    db_update_user,
)

from app.presenter.bot.keyboards.inline import (
    generate_category_menu,
    generate_constructor_button,
    generate_delete_product,
    show_product_by_category,
)
from app.presenter.bot.keyboards.reply import (
    back_arrow_button,
    back_to_main_menu,
    generate_main_menu,
    share_phone_button,
)
from app.presenter.bot.utils import (
    counting_products_from_cart,
    text_for_caption,
)
from app.settings.config import config

# loging qilish
logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.TELEGRAM_TOKEN, default=DefaultBotProperties(parse_mode="HTML"))

dp = Dispatcher()


@dp.message(CommandStart())
async def start_command(message: types.Message):
    builder = ReplyKeyboardBuilder()

    builder.row(
        types.KeyboardButton(text="Restoran menyusi"),
        types.KeyboardButton(text="Biz bilan bog'lanish")
    )

    keyboard = builder.as_markup(resize_keyboard=True)

    await message.answer(
        "Assalomu aleykum",
        reply_markup=keyboard
    )


@dp.message(F.text == "Restoran menyusi")
async def show_menu(message: types.Message):
    await message.answer("Restoran menyusi: \nSalatlar\nFast food\nIssiq taomlar\nOrqaga")


@dp.message(F.text == "Biz bilan bog'lanish")
async def contact_us(message: types.Message):
    await message.answer("Bizning nomer: +7 (999) 000-00-00")

@dp.message(F.text == "Orqaga")
async def back_menu(message: types.Message):
    await message.answer(show_menu)


@dp.message(F.text == "Salatlar")
async def salat(message: types.Message):
    await message.answer("Salatlar: \nSezar\nOlivye salat\nOrqaga")

@dp.message(F.text == "Orqaga")
async def back_menu(message: types.Message):
    await message.answer(show_menu)

@dp.message(F.text == "Fast food")
async def fast(message: types.Message):
    await message.answer("Fast food: \nBurger\nHot-dog\nOrqaga")

@dp.message(F.text == "Orqaga")
async def back_menu(message: types.Message):
    await message.answer(show_menu)

@dp.message(F.text == "Issiq taomlar")
async def food(message: types.Message):
    await message.answer("Taomlar: \nOsh\nSho'rva\nOrqaga")

@dp.message(F.text == "Orqaga")
async def back_menu(message: types.Message):
    await message.answer(show_menu)


if __name__ == "__main__":
    dp.run_polling(bot)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
