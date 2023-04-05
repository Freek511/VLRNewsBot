import telebot
from telebot import types

API_TOKEN = '5885213211:AAFaccPlQX4ruVPj-w67qORirs49Myn7DNo'

bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=['start'])
def wellcome_msg(message):
    msg = f' <b>Привет, {message.from_user.first_name}, я VLRNewsBot! </b> \nЯ помогу тебе с нахождением ' \
          f'новых лайнапов для каждого агента! Все что тебе нужно, это указать карту и понравившегося агента!'
    markup = types.ReplyKeyboardMarkup()
    next = types.KeyboardButton('Далее')
    help = types.KeyboardButton('/help')
    markup.add(next, help)
    msg = bot.send_message(message.chat.id, f' <b>Привет, {message.from_user.first_name}, я VLRNewsBot! </b> '
                                            f'\nЯ помогу тебе с нахождением новых лайнапов для каждого агента! '
                                            f'Все что тебе нужно, это указать карту и понравившегося агента!',
                           parse_mode='html', reply_markup=markup)
    bot.register_next_step_handler(msg, main)


def main(message):
    # buttons
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    brim = types.KeyboardButton('Brimstone')
    viper = types.KeyboardButton('Viper')
    omen = types.KeyboardButton('Omen')
    kj = types.KeyboardButton('KillJoy')
    cyph = types.KeyboardButton('Cypher')
    sova = types.KeyboardButton('Sova')
    sage = types.KeyboardButton('Sage')
    ph = types.KeyboardButton('Phoenix')
    jett = types.KeyboardButton('Jett')
    reyna = types.KeyboardButton('Reyna')
    breach = types.KeyboardButton('Breach')
    raze = types.KeyboardButton('Raze')
    skye = types.KeyboardButton('Skye')
    yoru = types.KeyboardButton('Yoru')
    astra = types.KeyboardButton('Astra')
    kayo = types.KeyboardButton('KAY/O')
    cham = types.KeyboardButton('Chamber')
    neon = types.KeyboardButton('Neon')
    fade = types.KeyboardButton('Fade')
    harb = types.KeyboardButton('Harbor')
    gekko = types.KeyboardButton('Gekko')
    markup.add(brim, viper, omen, kj, cyph, sova, sage, ph, jett, reyna, breach, raze, skye, yoru, astra, kayo, cham,
               neon, fade, harb, gekko)

    msg = bot.send_message(message.chat.id, 'Введите имя агента', reply_markup=markup)
    bot.register_next_step_handler(msg, agent_step)


def agent_step(message):
    # user request
    user_info = {}
    user_info['agent'] = message.text

    # buttons
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    bind = types.KeyboardButton('Bind')
    haven = types.KeyboardButton('Haven')
    split = types.KeyboardButton('Split')
    ascent = types.KeyboardButton('Ascent')
    icebox = types.KeyboardButton('Icebox')
    breeze = types.KeyboardButton('Breeze')
    frac = types.KeyboardButton('Fracture')
    pearl = types.KeyboardButton('Pearl')
    lotus = types.KeyboardButton('Lotus')
    markup.add(bind, haven, split, ascent, icebox, breeze, frac, pearl, lotus)

    msg = bot.send_message(message.chat.id, 'Введите название карты', reply_markup=markup)
    bot.register_next_step_handler(msg, map_step, user_info)


def map_step(message, user_info):
    user_info['map'] = message.text

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    attack = types.KeyboardButton('Атака')
    defense = types.KeyboardButton('Защита')
    both = types.KeyboardButton('Обе')
    markup.add(attack, defense, both)

    msg = bot.send_message(message.chat.id, 'Выберите сторону', reply_markup=markup)
    bot.register_next_step_handler(msg, side_step, user_info)


def side_step(message, user_info):
    user_info['side'] = message.text
    markup = types.ReplyKeyboardRemove(selective=False)
    bot.send_message(message.chat.id, 'Вот результат по вашму запросу', reply_markup=markup)
    print(user_info)


bot.polling(none_stop=True)
