from vkbottle.bot import Bot
from database import Database
from handlers import (
    register_main_handlers,
    register_svo_handlers,
    register_large_handlers,
    register_laws_handlers,
    register_common_handlers
)

TOKEN = "vk1.a.yIy9ZjXc_H4zSlFvqP3n-JnHA6PwW7tC5Se4w3AqrdCcCfjy3YY0U-fOfTwSJAArSABLlL_EFN3ogozdtriHlqytWC3DfL6FORw8si0PcfSs5XMj9BCXXoMSUl_jUVmBxBXRbzfJkG5WalHPDchWvOVGizFL36bRYzauz7bzwqDlR7VDBj-J0LNuzBBpvhb8Ev07cDmN_NL2AiI2MtN3dg"

bot = Bot(token=TOKEN)
db = Database()

# Подключаемся к БД
db.connect()
print("Подключение к PostgreSQL установлено")

# Регистрируем обработчики
register_main_handlers(bot, db)
register_svo_handlers(bot, db)
register_large_handlers(bot, db)
register_laws_handlers(bot, db)
register_common_handlers(bot, db)

if __name__ == "__main__":
    print("Бот запущен!")
    bot.run_forever()