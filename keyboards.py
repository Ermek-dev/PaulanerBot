from telebot import types

def main_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(
        types.KeyboardButton('📖 Меню'),
        types.KeyboardButton('🎉 Октоберфест'),
        types.KeyboardButton('👨‍🍳 Наш шеф-повар'),
        types.KeyboardButton('🍽️ Уникальное предложение'),
        types.KeyboardButton('📍 Наш адрес'),
        types.KeyboardButton('🗒️ Для сотрудников'),
    )
    return markup

def staff_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(
        types.KeyboardButton('🔄 Ротации'),
        types.KeyboardButton('📜 История пивоварни'),
        types.KeyboardButton('🍻 Процесс пивоварения'),
        types.KeyboardButton('🍺 Виды пива'),
        types.KeyboardButton('📚 Файлы'),
        types.KeyboardButton('🍽 Сервис'),
        types.KeyboardButton('⬅️ Назад'),
    )
    return markup

def address_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(
        types.KeyboardButton('🗺 Google Карты'),
        types.KeyboardButton('🌍 Яндекс.Карты'),
        types.KeyboardButton('🗺 2GIS'),
        types.KeyboardButton('⬅️ Назад'),
    )
    return markup
