"""
Sana : 18/11/2022
Sobirjonov Khusanboy
Matnni shifrlab beruvchi hamda shifrdan chiqaruvchi bot 2 - qism
Amaliyot
"""
from shifr import is_num
import telebot

TOKEN = "5877375796:AAH_Jl0Glx6U7MHyeywR5oDJIwazmRuf6co"
bot = telebot.TeleBot(token=TOKEN)

@bot.message_handler(commands=["start"])
def send_welcome(message):
    xabar = f"👋 Assalomu alaykum, {message.from_user.first_name} {message.from_user.last_name} 👤\n🤖 Cipher to Text botiga xush kelibsiz!"
    xabar += "\nMatningizni yuboring. 🗒 \nMatningizni shifrdan chiqarish kerak bo'lsa, 🔐 shu tarzda botga tashlang : \ncipher\n1110011 1100001 1101100 1101111 1101101"
    bot.reply_to(message, xabar)


# matnlar uchun mas'ul funksiya
@bot.message_handler(func=lambda msg: msg.text is not None)
def translit(message):
    msg = is_num(message.text)
    if len(msg) > 4096: msg = "❌ Siz yuborgan ma'lumot natijasi 4096 ta belgidan oshib ketdi 🚫\n\n 👮‍♂️ Iltimos qisqaroq matn jo'nating ✅"
    bot.reply_to(message, msg)


bot.polling()




















