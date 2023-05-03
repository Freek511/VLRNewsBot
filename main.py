import telebot
import os
from dotenv import load_dotenv
from telebot import types
from parcer import ValorantInfo

load_dotenv()
API_TOKEN = os.getenv("TOKEN")  # '5885213211:AAFaccPlQX4ruVPj-w67qORirs49Myn7DNo'
bot = telebot.TeleBot(API_TOKEN)
valorant_info = ValorantInfo()


def generate_button_list(names):
    return [types.KeyboardButton(name) for name in names]


@bot.message_handler(commands=['start'])
def wellcome_msg(message):
    msg = f' <b>Привет, {message.from_user.first_name}, я VLRNewsBot! </b> \nЯ помогу тебе с нахождением ' \
          f'новых лайнапов для каждого агента! Все что тебе нужно, это указать карту и понравившегося агента!'

    markup = types.ReplyKeyboardMarkup()
    initial_actions = ['Далее', 'help']
    markup.add(*generate_button_list(initial_actions))

    msg = bot.send_message(message.chat.id, msg, parse_mode='html', reply_markup=markup)
    bot.register_next_step_handler(msg, agent_step)


def agent_step(message):
    markup = types.ReplyKeyboardMarkup(row_width=3)
    heroes = valorant_info.heroes()
    markup.add(*generate_button_list(heroes))

    msg = bot.send_message(message.chat.id, 'Выберите имя агента', reply_markup=markup)
    bot.register_next_step_handler(msg, map_step)


def map_step(message):
    user_info = {'agent': message.text}

    markup = types.ReplyKeyboardMarkup(row_width=3)
    maps = valorant_info.maps()
    markup.add(*generate_button_list(maps))
    markup.add(types.KeyboardButton('Назад'))

    msg = bot.send_message(message.chat.id, 'Выберите название карты', reply_markup=markup)
    bot.register_next_step_handler(msg, side_step, user_info)


def side_step(message, user_info):
    if message.text == 'Назад':
        agent_step(message)

    else:
        user_info['map'] = message.text

        markup = types.ReplyKeyboardMarkup()
        sides = valorant_info.sides()
        markup.add(*generate_button_list(sides))
        markup.add(types.KeyboardButton('Назад'))

        msg = bot.send_message(message.chat.id, 'Выберите сторону', reply_markup=markup)
        bot.register_next_step_handler(msg, result, user_info)


def result(message, user_info):
    if message.text == 'Назад':
        message.text = user_info['agent']
        map_step(message)

    else:
        user_info['side'] = message.text

        markup = types.ReplyKeyboardRemove(selective=False)
        bot.send_message(message.chat.id, 'Вот результат по вашему запросу', reply_markup=markup)

        print(user_info)


bot.polling(none_stop=True)
