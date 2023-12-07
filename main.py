import telebot
from telebot import types

bot = telebot.TeleBot('6673352748:AAEpUZVeyAqeO617rvZqhrjwzonivSOZyk8')



@bot.message_handler(content_types=['photo','audio','video'])
def get_content(message):
    bot.reply_to(message, 'Вибач, мені це не цікаво. Давай перейдемо до справи')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Купити 💸', url='https://t.me/+dkbJTOmmF_MxZmVi')
    markup.row(btn1)
    btn2 = types.InlineKeyboardButton('Звязатись з менеджером 💬', url='https://t.me/Renat_Kost')
    markup.row(btn2)
    btn3 = types.InlineKeyboardButton('Каталог каналів 📱', url='https://tgsell.me/catalog')
    btn4 = types.InlineKeyboardButton('Калькулятор вартості ⚖️', url='https://tgsell.me')
    markup.row(btn3, btn4)
    btn5 = types.InlineKeyboardButton('Чат TgSell 📢', url='https://t.me/+0lPrC3YwYlQyZGMy')
    markup.row(btn5)

    bot.send_message(message.chat.id,'<b>Дякую що користуєшся TgSell🇺🇦.</b> \n \n <b>Купити 💸 </b> - <em>Тебе відправить в чат с продавцем і гарнтом угоди.</em>\n \n <b>Звязатись з менеджером 💬</b> - Всі питання крім купівлі вирішуються з менеджером.\n \n <b>Каталог каналів 📱</b> - Повернутись на сайт для перегляду каналів\n \n <b>Калькулятор вартості ⚖️</b> - TgSell допоможе тобі визначити вартість каналу\n \n <b>Чат TgSell 📢</b> - Чат для спілкування і обговорення ', parse_mode='html', reply_markup=markup)


bot.polling(none_stop=True)