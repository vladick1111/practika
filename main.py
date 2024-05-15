import telebot
from jira import JIRA
from telebot import types

bot = telebot.TeleBot('6378161589:AAGYPNCfZncb4u5UBBvOdZDvdnLBb0t-YiE')

login = 'vlad2005sainov@gmail.com'
api_key = 'ATATT3xFfGF0z5uHVKEssufMpIXSrYzqZ2pjqVAZoq3qELkEvuYwoLR9GXlTP8pPwFh_-Xp1MzkKIcYMAwceAJJuvcNT5D-N-c-qZ_zUI9dfn8dx3X8vzDOHzIg4OD9N3WDzkZ4XGSArBwlS-BGbU7pkujjmYsv_lLr_UwPC3wEMhBI8ZpTFV28=44363045'
jira_options = {'server': 'https://praktika-pi311.atlassian.net'}
jira = JIRA(options=jira_options, basic_auth=(login, api_key))

@bot.message_handler(commands=["start"])
def bot_messages(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Создать задачу")
    markup.add(item1)
    item2 = types.KeyboardButton("Найти задачу")
    markup.add(item2)
    item3 = types.KeyboardButton("Открыть задачу")
    markup.add(item3)

    bot.send_message(message.chat.id, 'Я могу исполнить три желания:\n Создать задачу\n Найти задачу\n Открыть задачу', reply_markup=markup)

bot.polling(none_stop=True)