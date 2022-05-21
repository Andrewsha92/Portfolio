import telebot

token = "5385667767:AAEmHy_prqezWV5BRW7e7lo8MRWUfjBpTL4"

bot = telebot.TeleBot(token)


@bot.message_handler(content_types=["text"])

def echo(message):
    if message.text == "Андрей":
        bot.send_message(message.chat.id,"Ба! Знакомые все лица!")
    else:
        bot.send_message(message.chat.id, message.text)


bot.polling(none_stop=True)

