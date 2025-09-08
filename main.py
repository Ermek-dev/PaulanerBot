import telebot
from config import TOKEN


# подключаем хендлеры
from handlers.start import register_start_handler
from handlers.staff import register_staff_handlers
from handlers.menu import register_menu_handlers

bot = telebot.TeleBot(TOKEN)

# регистрируем хендлеры
register_start_handler(bot)
register_staff_handlers(bot)
register_menu_handlers(bot)

if __name__ == "__main__":
    bot.polling(none_stop=True)
