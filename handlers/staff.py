from telebot import types
from keyboards import staff_menu
import states

PASSWORD = "1111"  # потом можно вынести в .env

def register_staff_handlers(bot):
    @bot.message_handler(func=lambda message: message.text == '🗒️ Для сотрудников')
    def ask_for_password(message):
        if states.user_states.get(message.chat.id) == 'authenticated':
            bot.send_message(message.chat.id, "Вы уже авторизованы ✅", reply_markup=staff_menu())
        else:
            states.user_states[message.chat.id] = 'waiting_password'
            states.user_password_attempts[message.chat.id] = 0
            bot.send_message(message.chat.id, "Введите пароль:")

    @bot.message_handler(func=lambda message: states.user_states.get(message.chat.id) == 'waiting_password')
    def handle_password(message):
        if message.text == PASSWORD:
            states.user_states[message.chat.id] = 'authenticated'
            states.user_password_attempts[message.chat.id] = 0
            bot.send_message(message.chat.id, "Пароль верный ✅", reply_markup=staff_menu())
        else:
            states.user_password_attempts[message.chat.id] += 1
            remaining_attempts = 3 - states.user_password_attempts[message.chat.id]
            if remaining_attempts > 0:
                bot.send_message(message.chat.id, f"Неверный пароль ❌. Осталось попыток: {remaining_attempts}")
            else:
                bot.send_message(message.chat.id, "Превышено количество попыток. Попробуйте позже.")
                states.user_states[message.chat.id] = None
                states.user_password_attempts[message.chat.id] = 0
