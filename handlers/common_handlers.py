from keyboards import get_back_keyboard

def register_common_handlers(bot, db):
    
    @bot.on.message(payload={"cmd": "common"})
    async def common(message):
        text = db.get_common_question()
        await message.answer(text, keyboard=get_back_keyboard())