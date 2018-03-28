import telebot

TOKEN='500356225:AAEzQwaTne7NgT1sxpJThEm7YrER7aGtxxg' # полученный у @BotFather

bot=telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    sent = bot.send_message(message.chat.id, 'Как тебя зовут?')
    bot.register_next_step_handler(sent, hello)


def hello(message):
    bot.send_message(
    message.chat.id,
    'Привет, {name}. Рад тебя видеть.'.format(name=message.text))


bot.polling()
