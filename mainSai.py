import telebot
# import constans
# from telebot import types

bot = telebot.TeleBot('620264496:AAGhmkwE_ayuLOGma76CSvfWB8IX1LySMg4')
users = [410819637]

@bot.message_handler(commands=['start'])
def handle_start(message, text=True):
    if message.from_user.id in users:
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False )
        user_markup.row('Прайсы', 'Остатки по складу', 'Цены на каталоги:')
        user_markup.row('Звонок менеджеру', 'Facebook', 'Instagram')
        if text:
            bot.send_message(message.from_user.id, 'Приветствую {} Выберите пункт меню'
                             .format(message.from_user.first_name), reply_markup=user_markup)
        else:
            bot.send_message(message.from_user.id, 'Выберите пункт меню',
                             reply_markup=user_markup)
    else:
        bot.send_message(message.from_user.id, 'Для вас доступ запрещен, {}, id - {}'
                         .format(message.from_user.first_name, message.from_user.id))


@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.from_user.id in users:
        if message.text == "Прайсы":
            bot.send_message(message.from_user.id, "https://docs.google.com/spreadsheets/d/1r4AWJN1l1g2w_uSRg9fPvsXCSr-GYA-oBqMEdaZgo38/edit#gid=1451937519")
        elif message.text == "Остатки по складу":
            stock_markup = telebot.types.ReplyKeyboardMarkup(True, False)
            stock_markup.row('Cклад1', 'Склад2', 'Склад3')
            stock_markup.row('Назад')
            bot.send_message(message.from_user.id, "Выберите пункт меню", reply_markup=stock_markup)
        elif message.text == "Facebook":
            bot.send_message(message.from_user.id, "https://www.facebook.com/suerte.elegancia/?fref=mentions")
        elif message.text == "Instagram":
            bot.send_message(message.from_user.id, "https://www.instagram.com/suerte.elegancia/")
        elif message.text == "Цены на каталоги:":
            bot.send_message(message.from_user.id, "https://www.instagram.com/suerte.elegancia/")
        elif message.text == "Назад":
            handle_start(message, text=False)
    else:
        bot.send_message(message.from_user.id, 'Для вас доступ запрещен, {}, id - {}'
                         .format(message.from_user.first_name, message.from_user.id))


bot.polling(none_stop=True)
