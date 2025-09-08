from keyboards import main_menu

def register_start_handler(bot):
    @bot.message_handler(commands=['start'])
    def start(message):
        user = message.from_user
        welcome_message = (
            "🍻 Приветствуем вас в *Paulaner Brauhaus Almaty*! 🍻\n\n"
            f"Привет, {user.first_name}!\n\n"
            "🌟 Аутентичное пиво и вкуснейшие блюда.\n"
            "🍽️ Выбирайте из нашего меню и погружайтесь в культуру!\n"
            "🎉 Присоединяйтесь на мероприятия и дегустации.\n\n"
            "🍺 Давайте создадим пивные истории вместе! 🍺"
        )
        bot.send_message(message.chat.id, welcome_message, reply_markup=main_menu(), parse_mode="MARKDOWN")
