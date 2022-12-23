import telebot

bot = telebot.Telebot('5985504292:AAFu7uGRvyb52NYg_g16G9YL5R0iw2yNB3k')

@bot.message_handlers(commands=['start'])
def start(message):
    bot.send_massage(message.chat.id, '<b>Привет</b>', parse_mode='html')

bot.polling(none_stop=True)