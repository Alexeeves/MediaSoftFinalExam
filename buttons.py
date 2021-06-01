import telebot

from telebot import types
from environment import tg_bot_token
from weather import get_weather
from exchangerate_usd import ex_rate_usd
from exchangerate_eur import ex_rate_eur

bot = telebot.TeleBot(tg_bot_token)


@bot.message_handler(commands=['start'])
def run_bot(message):
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton('Погода в Ульяновске', callback_data='wheather')
    button2 = types.InlineKeyboardButton('Курс валют', callback_data='exchangerate')
    keyboard.add(button1, button2)
    msg = bot.send_message(message.chat.id, 'Привет, выбери действие', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        def add_keybuttom():
            keyboard = types.InlineKeyboardMarkup(row_width=2)
            usd_button = types.InlineKeyboardButton(text='USD', callback_data='ex_rate_us')
            eur_button = types.InlineKeyboardButton(text='EUR', callback_data='ex_rate_eu')
            keyboard.add(usd_button, eur_button)
            return keyboard

        if call.data == 'wheather':

            weather = get_weather('Ульяновск')
            bot.send_message(call.message.chat.id, weather)

        elif call.data == 'exchangerate':

            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.message_id,
                                  text='Выбери',
                                  reply_markup=add_keybuttom())

        elif call.data == 'ex_rate_us':
            ex_rate_us = ex_rate_usd()
            ex_rate_us = f' За один доллар просят {ex_rate_us} рублей'
            bot.send_message(call.message.chat.id, ex_rate_us)

        elif call.data == 'ex_rate_eu':
            ex_rate_eu = ex_rate_eur()
            ex_rate_eu = f' За один евро просят {ex_rate_eu} рублей'
            bot.send_message(call.message.chat.id, ex_rate_eu)

    except Exception as e:
        print(e)


def bot_polling():
    bot.polling(none_stop=True)
