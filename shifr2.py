"""
Sana : 18/11/2022
Sobirjonov Khusanboy
Matnni shifrlab beruvchi hamda shifrdan chiqaruvchi bot 2 - qism
Amaliyot
"""
from shifr import is_num
import telebot

TOKEN = "" # bot tokeni yoziladi
bot = telebot.TeleBot(token=TOKEN)

@bot.message_handler(commands=["start"])
def send_welcome(message):
    xabar = f"š Assalomu alaykum, {message.from_user.first_name} {message.from_user.last_name} š¤\nš¤ Cipher to Text botiga xush kelibsiz!"
    xabar += "\nMatningizni yuboring. š \nMatningizni shifrdan chiqarish kerak bo'lsa, š shu tarzda botga tashlang : \ncipher1\n1110011 1100001 1101100 1101111 1101101"
    xabar += "\n1ļøā£ Sezar usulida shifrlash uchun :\n2\nsalom\n1ļøā£ Shifrdan chiqarish uchun esa :\ncipher2\n5#vdorp\nāļø Tarzida amalga oshirasiz."
    bot.reply_to(message, xabar)

# matnlar uchun mas'ul funksiya
@bot.message_handler(func=lambda msg: msg.text is not None)
def translit(message):
    msg = is_num(message.text)
    if len(msg) > 4096: msg = "ā Siz yuborgan ma'lumot natijasi 4096 ta belgidan oshib ketdi š«\n\n š®āāļø Iltimos qisqaroq matn jo'nating ā"
    bot.reply_to(message, msg)


bot.polling()




















