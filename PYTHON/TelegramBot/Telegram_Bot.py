import telebot
from config import keys, TOKEN
from extensions import ConvertionExсeption, CryptoConverter

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def start_message(message: telebot.types.Message):
    bot.send_message(message.chat.id, f" Привет, {message.chat.username}!\n"
                                      f"\n"
                                      f"       Чтобы продолжить работу введите команду:\n"
                                      f"<имя валюты>  <в какую валюту перевести>  <количество вводимой валюты>\n"
                                      f"\n"
                                      f" * Для примера: биткоин доллар 100 *\n"
                                      f"\n"
                                      f" Увидеть список всех доступных валют /values")

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text = '\n'.join((text,key, ))
    bot.reply_to(message,text)

@bot.message_handler(content_types=['text',])
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(' ')

        if len(values) != 3:
            raise ConvertionExсeption(f"Слишком много параметров")

        quote, base, amount = values
        total_base = CryptoConverter.get_price(quote, base, amount)

    except ConvertionExсeption as e:
        bot.reply_to(message, f'Ошибка пользователя\n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду\n{e}')
    else:
        amount = int(amount)
        total_base = int(total_base)
        text = f'Цена {amount} единиц {quote} в {base} = {total_base * amount} {base}'
        bot.send_message(message.chat.id, text)

@bot.message_handler(content_types=['photo', ])
def say_lmao(message: telebot.types.Message):
    bot.reply_to(message, f'Nice meme XDD {message.chat.username}')

@bot.message_handler(content_types=['audio',])
def get_text_messages(message):
    bot.send_message(message.chat.id, f"аудио добавлено в историю  {message.chat.username}")

@bot.message_handler(content_types=['voice',])
def get_text_messages(message):
    bot.send_message(message.chat.id, f"голосовое сообщение добавлено в историю {message.chat.username}")

@bot.message_handler(content_types=['video',])
def get_text_messages(message):
    bot.send_message(message.chat.id, f"видео добавлено в историю {message.chat.username}")

@bot.message_handler(content_types=['contact',])
def get_text_messages(message):
    bot.send_message(message.chat.id, f"контакт добавлен в историю  {message.chat.username}")

@bot.message_handler(content_types=['sticker',])
def get_text_messages(message):
    bot.send_message(message.chat.id, f"стикер добавлен в историю  {message.chat.username}")

@bot.message_handler(content_types=['document',])
def get_text_messages(message):
    bot.send_message(message.chat.id, f"файл загружен  {message.chat.username}")

@bot.message_handler(content_types=['location',])
def get_text_messages(message):
    bot.send_message(message.chat.id, f"добавлена геолокация  {message.chat.username}")



bot.polling()




