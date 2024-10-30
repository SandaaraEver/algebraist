from flask import Flask, request
import telebot
from telebot import types
import time

secret = ''
BOT_TOKEN = ''
bot = telebot.TeleBot(BOT_TOKEN, threaded=False)

bot.remove_webhook()
time.sleep(1)
bot.set_webhook(url="https://sandaaraeverstova.pythonanywhere.com/{}".format(secret))

app = Flask(__name__)

@app.route('/{}'.format(secret), methods=["POST"])
def webhook():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    print("Message")
    return "ok", 200

@bot.message_handler(commands=['start', 'привет'])
def send_welcome(message):
    menu = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    menu.add(types.KeyboardButton('Теорема Виета'))
    menu.add(types.KeyboardButton('Решение квадратного уравнения'))
    menu.add(types.KeyboardButton('Формулы сокращенного умножения'))
    menu.add(types.KeyboardButton('Свойства степеней'))

    bot.reply_to(message, "Здравствуйте! Вы пользуетесь Ботом Алгебраист! Я подскажу вам основные формулы по Алгебре! Наберите /help для получения справки!", reply_markup=menu)

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "/виета - Теорема Виета\n/квуравнение - Решение квадратного уровнения\n/фсуразнкв - Формула сокращенного умножения разность квадратов\n/фсуквсуммы - формула сокращенного уравнение квадрат суммы\n/фсуквразн - ормула сокращенного уровнения квадрат разности\n/фсуразнкуб - формула сокращенного уравнение разность кубов\n/фсусуммыкуб - формула сокращенного уравнение сумма кубов\n/фсукубсум - формула сокращенного уравнение куб суммы\n/фсукубразн - формула сокращенного уравнение куб разности\n/степноль - Нулевая степень числа\n/степодин - Единичная степень числа\n/произвстеп - Произведение степеней\n/деленстеп - Деление степеней\n/степвстеп - Степень в степени\n/степпроизв - Степень произведения\n/степделение - Степень деления\n/степотриц - Отрицательная степень\n")

@bot.message_handler(commands=['виета'])
def send_vieta(message):
    f = open('/home/sandaaraeverstova/mysite/formulas/vieta.png', 'rb')
    bot.send_photo(message.chat.id, f, 'Теорема виета о корнях квадратного уровнения')

@bot.message_handler(commands=['квуравнение'])
def send_kvuravnenie(message):
    f = open('/home/sandaaraeverstova/mysite/formulas/kvur.png', 'rb')
    bot.send_photo(message.chat.id, f, 'Нахождение корней квадратного уровнения')


@bot.message_handler(commands=[ 'фсуразнкв'])
def send_fsuraznkv(message):
    f = open('/home/sandaaraeverstova/mysite/formulas/fsuraznkv.png', 'rb')
    bot.send_photo(message.chat.id, f, 'разность квадратов')


@bot.message_handler(commands=[ 'фсуквсуммы'])
def send_fsukvsum(message):
    f = open('/home/sandaaraeverstova/mysite/formulas/fsukvsum.png', 'rb')
    bot.send_photo(message.chat.id, f, 'квадрат суммы')


@bot.message_handler(commands=[ 'фсуквразн'])
def send_fsukvrazn(message):
    f = open('/home/sandaaraeverstova/mysite/formulas/fsukvsum.png', 'rb')
    bot.send_photo(message.chat.id, f, 'квадрат разности')


@bot.message_handler(commands=[ 'фсусуммакуб'])
def send_fsusumkub(message):
    f = open('/home/sandaaraeverstova/mysite/formulas/fsusumkub.png', 'rb')
    bot.send_photo(message.chat.id, f, 'сумма кубов')

@bot.message_handler(commands=[ 'фсуразнкуб'])
def send_fsuraznkub(message):
    f = open('/home/sandaaraeverstova/mysite/formulas/fsuraznkub.png', 'rb')
    bot.send_photo(message.chat.id, f, 'разность кубов')


@bot.message_handler(commands=[ 'фсукубсум'])
def send_fsukubsum(message):
    f = open('/home/sandaaraeverstova/mysite/formulas/fsukubsum.png', 'rb')
    bot.send_photo(message.chat.id, f, 'куб суммы двух чисел')


@bot.message_handler(commands=[ 'фсукубразн'])
def send_fsukubrazn(message):
    f = open('/home/sandaaraeverstova/mysite/formulas/fsukubrazn.png', 'rb')
    bot.send_photo(message.chat.id, f, 'куб разности двух чисел')

@bot.message_handler(commands=[ 'степноль'])
def send_stepnul(message):
    f = open('/home/sandaaraeverstova/mysite/formulas/stepnul.png', 'rb')
    bot.send_photo(message.chat.id, f, 'Нулевая степень числа')

@bot.message_handler(commands=[ 'степодин'])
def send_stepodin(message):
    f = open('/home/sandaaraeverstova/mysite/formulas/stepodin.png', 'rb')
    bot.send_photo(message.chat.id, f, 'Единичная степень числа')

@bot.message_handler(commands=[ 'произвстеп'])
def send_proizvstep(message):
    f = open('/home/sandaaraeverstova/mysite/formulas/proizvstep.png', 'rb')
    bot.send_photo(message.chat.id, f, 'Произведение степеней с одинаковым основанием')

@bot.message_handler(commands=[ 'деленстеп'])
def send_deleniestep(message):
    f = open('/home/sandaaraeverstova/mysite/formulas/deleniestep.png', 'rb')
    bot.send_photo(message.chat.id, f, 'Деление степеней с одинаковым основанием')


@bot.message_handler(commands=[ 'степвстеп'])
def send_stepvstep(message):
    f = open('/home/sandaaraeverstova/mysite/formulas/stepvstep.png', 'rb')
    bot.send_photo(message.chat.id, f, 'Возводение числа в степени x в степень y')


@bot.message_handler(commands=[ 'степпроизв'])
def send_stepproizv(message):
    f = open('/home/sandaaraeverstova/mysite/formulas/proizvstep.png', 'rb')
    bot.send_photo(message.chat.id, f, 'Степень произведения двух чисел')


@bot.message_handler(commands=[ 'степделение'])
def send_stepdelenia(message):
    f = open('/home/sandaaraeverstova/mysite/formulas/stepdelenie.png', 'rb')
    bot.send_photo(message.chat.id, f, 'Степень деления двух чисел')

@bot.message_handler(commands=[ 'степотриц'])
def send_stepotriz(message):
    f = open('/home/sandaaraeverstova/mysite/formulas/stepotriz.png', 'rb')
    bot.send_photo(message.chat.id, f, 'Отрицательная степень')

@bot.message_handler()
def send_keyboard(message):
    match message.text:
        case 'Теорема Виета':
            send_vieta(message)
        case 'Решение квадратного уравнения':
            send_kvuravnenie(message)
        case 'Формулы сокращенного умножения':
            menu = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
            menu.add(types.KeyboardButton('Разность квадратов'))
            menu.add(types.KeyboardButton('Квадрат суммы'))
            menu.add(types.KeyboardButton('Квадрат разности'))
            menu.add(types.KeyboardButton('Сумма кубов'))
            menu.add(types.KeyboardButton('Разность кубов'))
            menu.add(types.KeyboardButton('Куб суммы'))
            menu.add(types.KeyboardButton('Куб разности'))
            menu.add(types.KeyboardButton('Назад'))
            bot.reply_to(message, "Выберите формулу!", reply_markup=menu)
        case 'Свойства степеней':
            menu = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
            menu.add(types.KeyboardButton('Нулевая степень числа'))
            menu.add(types.KeyboardButton('Число в первой степени'))
            menu.add(types.KeyboardButton('Произведение степней с одинаковым основанием'))
            menu.add(types.KeyboardButton('Деление степеней с одинаковым основанием'))
            menu.add(types.KeyboardButton('Возводение числа в степени x в степень y'))
            menu.add(types.KeyboardButton('Степень произведения двух чисел'))
            menu.add(types.KeyboardButton('Степень деления двух чисел'))
            menu.add(types.KeyboardButton('Отрицательная степень числа'))
            menu.add(types.KeyboardButton('Назад'))
            bot.reply_to(message, "Выберите формулу!", reply_markup=menu)
        case 'Назад':
            send_welcome(message)
        case 'Разность квадратов':
            send_fsuraznkv(message)
        case 'Квадрат суммы':
            send_fsukvsum(message)
        case 'Разность квадратов':
            send_fsuraznkv(message)
        case 'Квадрат суммы':
            send_fsukvsum(message)
        case 'Квадрат разности':
            send_fsukvrazn(message)
        case 'Сумма кубов':
            send_fsusumkub(message)
        case 'Разность кубов':
            send_fsuraznkub(message)
        case 'Куб суммы':
            send_fsukubsum(message)
        case 'Куб разности':
            send_fsukubrazn(message)
        case 'Нулевая степень числа':
            send_stepnul(message)
        case 'Число в первой степени':
            send_stepodin(message)
        case 'Произведение степней с одинаковым основанием':
            send_proizvstep(message)
        case 'Деление степеней с одинаковым основанием':
            send_deleniestep(message)
        case 'Возводение числа в степени x в степень y':
            send_stepvstep(message)
        case 'Степень произведения двух чисел':
            send_stepproizv(message)
        case 'Степень деления двух чисел':
            send_stepdelenia(message)
        case 'Отрицательная степень числа':
            send_stepotriz(message)
        case _:
            bot.reply_to(message, "Я вас не понял")
