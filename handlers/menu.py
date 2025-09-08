from telebot import types
from keyboards import address_menu, main_menu, staff_menu
import states

def register_menu_handlers(bot):
    @bot.message_handler(content_types=['text'])
    def menu_router(message):
        if message.text == "📖 Меню":
            button = types.InlineKeyboardButton("Узнать подробнее:😊", url="https://drive.google.com/file/d/1RygonK4cSUhoKrZymD59h7WpYpDev77o/view")
            markup = types.InlineKeyboardMarkup().add(button)
            bot.send_message(message.chat.id, "Здесь вы можете ознакомиться с нашим меню:", reply_markup=markup)

        elif message.text == "🎉 Октоберфест":
            button = types.InlineKeyboardButton("Узнать подробнее:", url="https://telegra.ph/Istoriya-Oktoberfesta-09-03")
            markup = types.InlineKeyboardMarkup().add(button)
            bot.send_message(message.chat.id, "История Октоберфеста:", reply_markup=markup)

        elif message.text == "👨‍🍳 Наш шеф-повар":
            button = types.InlineKeyboardButton("Узнать подробнее:", url="https://telegra.ph/O-nashem-shef-povare-09-12")
            markup = types.InlineKeyboardMarkup().add(button)
            bot.send_message(message.chat.id, "🍽️ Наш шеф-повар:", reply_markup=markup)

        elif message.text == "🍽️ Уникальное предложение":
            button = types.InlineKeyboardButton("Узнать подробнее:", url="https://telegra.ph/Novinki-08-15-3")
            markup = types.InlineKeyboardMarkup().add(button)
            bot.send_message(message.chat.id, "🌟 Уникальное предложение:", reply_markup=markup)

        elif message.text == "📍 Наш адрес":
            bot.send_message(message.chat.id, "Выберите карту:", reply_markup=address_menu())

        elif message.text == "🌍 Яндекс.Карты":
            bot.send_message(message.chat.id, "https://yandex.ru/maps/org/paulaner_brauhaus/50803496758/?ll=76.915955%2C43.247914&z=17")

        elif message.text == "🗺 2GIS":
            bot.send_message(message.chat.id, "https://2gis.kz/almaty/firm/70000001055876564")

        elif message.text == "🗺 Google Карты":
            bot.send_message(message.chat.id, "https://www.google.com/maps/place/Paulaner+Br%C3%A4uhaus+Almaty")

        elif message.text == "⬅️ Назад":
            bot.send_message(message.chat.id, "⬅️ Назад", reply_markup=main_menu())

        # сотрудники
        elif message.text == "🔄 Ротации":
            btn = types.InlineKeyboardButton("Ротации", url="https://docs.google.com/presentation/d/1ZEO-9smKw7qfRpvzAc4YdkRXXhk3VOtsF6Qx9Q0rL4Q")
            bot.send_message(message.chat.id, "Вы переходите к ротациям 😊", reply_markup=types.InlineKeyboardMarkup().add(btn))

        elif message.text == "📜 История пивоварни":
            btn = types.InlineKeyboardButton("Перейти:", url="https://telegra.ph/Istorii-pivovarni-Paulaner-08-15")
            bot.send_message(message.chat.id, "Интересные факты о нашей пивоварне 😊", reply_markup=types.InlineKeyboardMarkup().add(btn))

        elif message.text == "🍻 Процесс пивоварения":
            btn = types.InlineKeyboardButton("Перейти:", url="https://telegra.ph/Process-pivovareniya-08-16")
            bot.send_message(message.chat.id, "Процесс пивоварения 😊", reply_markup=types.InlineKeyboardMarkup().add(btn))

        elif message.text == "🍺 Виды пива":
            btn = types.InlineKeyboardButton("Перейти:", url="https://telegra.ph/Kak-varyat-pivovidyinteresnye-fakty-08-16")
            bot.send_message(message.chat.id, "Разные сорта пива 😊", reply_markup=types.InlineKeyboardMarkup().add(btn))

        elif message.text == "📚 Файлы":
            btn = types.InlineKeyboardButton("Перейти:", url="https://drive.google.com/drive/folders/1WhRMuz6OmkN0PiLm8SF1N03tXgkL4eeF")
            bot.send_message(message.chat.id, "Полезные файлы 😊", reply_markup=types.InlineKeyboardMarkup().add(btn))

        elif message.text == "🍽 Сервис":
            btn = types.InlineKeyboardButton("Перейти:", url="https://telegra.ph/Standarty-restorannogo-servisa-08-28")
            bot.send_message(message.chat.id, "7 шагов сервиса 😊", reply_markup=types.InlineKeyboardMarkup().add(btn))
