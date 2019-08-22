"""820408109:AAGJlhVTqouPR0QWPVtRax-ntTY11ji51E4"""
import youtube

""" https://github.com/eternnoir/pyTelegramBotAPI/blob/master/README.md """
import telebot
import sqlite3
from telebot import types



bot = telebot.TeleBot('820408109:AAGJlhVTqouPR0QWPVtRax-ntTY11ji51E4')

keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
button_phone = types.KeyboardButton(text="Музыка")
button_geo1 = types.KeyboardButton(text="Новинки кино")
button_geo2 = types.KeyboardButton(text="Интересные факты")
button_geo3 = types.KeyboardButton(text="Смешные моменты")
button_geo4 = types.KeyboardButton(text="Посетить сайт joy-pup.com")
keyboard.add(button_phone, button_geo1,button_geo2,button_geo3,button_geo4)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Добрый день ' + str(message.from_user.username) + ' видео на какую тему желаете посмотреть?', reply_markup=keyboard)
    cc1 = message.from_user.username
    db = sqlite3.connect('db.sqlite3')
    cursor = db.cursor()
    # query = "SELECT * FROM polls_user_name WHERE unique = %s"
    # query = ("select count(*) as count FROM polls_user_name WHERE unique = '%s' "%(cc1))
    # query = "INSERT INTO polls_user_name unique VALUES %s"
    c = "select * from polls_user_name"
    cursor.execute(c)
    status = cursor.fetchone()
    db.commit()
    print(status)


@bot.message_handler(content_types=['text'])
def send_text(message):
    greeting = ['привет', "hi", "hello", "здрасте", "здравствуйте"]

    if message.text.lower() in greeting:
        bot.send_message(message.chat.id, message.text,reply_markup=keyboard1)

    elif message.text.lower() == 'новинки кино':
        links_fan = str(youtube.random_link_trail())
        bot.send_message(message.chat.id,'https://www.youtube.com'+links_fan)
        # bot.send_audio(message.chat.id, audio=open('audio/03969.mp3', 'rb'))

    elif message.text.lower() == 'музыка':
        links_fan1 = str(youtube.random_link_musik())
        bot.send_message(message.chat.id, 'https://www.youtube.com' + links_fan1)

    elif message.text.lower() == 'интересные факты':
        links_fan2 = str(youtube.random_link_fackts())
        bot.send_message(message.chat.id, 'https://www.youtube.com' + links_fan2)

    elif message.text.lower() == 'смешные моменты':
        links_fan3 = str(youtube.random_link_fun())
        bot.send_message(message.chat.id, 'https://www.youtube.com' + links_fan3)

    elif message.text.lower() == 'посетить сайт joy-pup.com':
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="➡️ Перейти на Joy-Pup", url="http://joy-pup.com")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Привет! Нажми на кнопку и перейди в поисковик.", reply_markup=keyboard)

    # Эти параметры для клавиатуры необязательны, просто для удобства





# """ отправка музыки и  получение id"""
# bot = telebot.TeleBot('8Rax-ntTY11ji51E4')
#
# @bot.message_handler(commands=['test'])
# def find_file_ids(message):
#     for file in os.listdir('audio/'):
#         if file.split('.')[-1] == 'mp3':
#             f = open('audio/'+file, 'rb')
#             msg = bot.send_voice(message.chat.id, f, None)
#             # А теперь отправим вслед за файлом его file_id
#             bot.send_message(message.chat.id, msg.voice.file_id, reply_to_message_id=msg.message_id)
#         time.sleep(3)
#
#
if __name__ == '__main__':
    bot.polling(none_stop=True)


# не забудьте про

""" https://github.com/eternnoir/pyTelegramBotAPI/blob/master/README.md """

