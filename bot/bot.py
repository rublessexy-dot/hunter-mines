import asyncio

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import (
    Message,
    ReplyKeyboardMarkup,
    KeyboardButton,
    WebAppInfo,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)

from config import BOT_TOKEN, WEBAPP_URL

bot = Bot(BOT_TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: Message):

    # Нижняя кнопка (Mini App)
    reply_keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(
                    text="💎ПОЛУЧИТЬ СИГНАЛ💎",
                    web_app=WebAppInfo(url=WEBAPP_URL),
                )
            ]
        ],
        resize_keyboard=True,
    )

    # Кнопка со ссылкой
    inline_keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="💠Регистрация💠",
                    url="https://one-vv5693.com/casino/list?open=register&p=4uwv",
                )
            ]
        ]
    )

    await message.answer(
    """
🧠 Бот основан и обучен на кластере нейросети BitsGap.

🎰 Для обучения было проанализировано более 10 000 игр.

💰 Пользователи уже достигают доходности 15–25% от капитала ежедневно.

📈 Точность прогнозов бота составляет 92% и продолжает улучшаться.

""",
    reply_markup=reply_keyboard,

    )

    await message.answer(
    """
💸 1. Для начала зарегистрируйтесь на сайте, нажав кнопку 💠 Регистрация 💠.

💸 2. Введите промокод HUNTER2K26 при регистрации.

💸 3. После регистрации бот автоматически проверит ваш аккаунт.

💸 4. Если у вас уже есть аккаунт — создайте новый на новую почту.
Номер телефона может быть любой, главное — ваша электронная почта!

💸 5. Делайте депозизит с минимальным пополнением🏦

💸 6. Открываете игру "MINES". Играете строго на весь депозит, советуем ставить 6 ловушек.

💸 7. Открываем 7-8 ячеек и ВЫВОДИМ прибыль.

""",
    reply_markup=inline_keyboard,
)


async def main():
    print("Бот запущен...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())