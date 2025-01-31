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


@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text.strip() == 'Создать задачу':
        bot.send_message(message.chat.id, 'Создание задачи. Введите название задачи.')
        bot.register_next_step_handler(message, get_create_issue_summary)
    elif message.text.strip() == 'Найти задачу':
        bot.register_next_step_handler(message, get_search_issue)
    elif message.text.strip() == 'Открыть задачу':
        bot.send_message(message.chat.id, 'Открытые задачи. Введите номер задачи TJ-...')
        bot.register_next_step_handler(message, get_open_issue)

bot.polling(none_stop=True)