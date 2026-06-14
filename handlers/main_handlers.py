from keyboards.keyboards import get_main_keyboard, get_categories_keyboard

def register_main_handlers(bot, db):

    @bot.on.message(text=["/start", "Начать", "Старт", "Привет"])
    async def start(message):
        await message.answer("Здравствуйте! Я бот о мерах поддержки граждан.", keyboard=get_main_keyboard())

    @bot.on.message(payload={"cmd": "main"})
    async def main(message):
        await message.answer("Главное меню:", keyboard=get_main_keyboard())

    @bot.on.message(payload={"cmd": "categories"})
    async def categories(message):
        await message.answer("Выберите категорию граждан:", keyboard=get_categories_keyboard())