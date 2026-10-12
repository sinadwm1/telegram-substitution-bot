import logging
import os
os.system("cls")
import telebot
from telebot import types


TOKEN = os.getenv("BOT_TOKEN", "")
if not TOKEN:
    raise RuntimeError("Set BOT_TOKEN before starting the bot.")
#Init the  bot with token
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    
    about_button = types.KeyboardButton('درباره ما')
    username_button = types.KeyboardButton('تبدیل متن')
    donate_button = types.KeyboardButton('حمایت مالی')
    
    markup.add(username_button, about_button)
    bot.send_message(message.chat.id, "سلام! لطفاً یکی از گزینه‌های زیر را انتخاب کنید:", reply_markup=markup)
    
    
@bot.message_handler(func=lambda message: message.text == 'درباره ما')
def about_us(message):
    about_text = "این ربات توسط من توسعه داده شده است. من یک توسعه‌دهنده با تجربه در زمینه برنامه‌نویسی هستم و این ربات برای ارتباط با کاربران و ارائه اطلاعات به آنها طراحی شده است."
    bot.send_message(message.chat.id, about_text)

@bot.message_handler(func=lambda message: message.text == 'تبدیل متن')
def send_text_prompt(message):
    text_prompt = "خوش اومدید، متن مورد نظرتون رو بفرستید:"
    bot.send_message(message.chat.id, text_prompt)

    
    
    
  
@bot.message_handler(func=lambda message: True)
def process_data(message):
    data = message.text
    conversion_code = {
    	# Uppercase Alphabets
    	'A': 'Z', 'B': 'Y', 'C': 'X', 'D': 'W', 'E': 'V', 'F': 'U',
    	'G': 'T', 'H': 'S', 'I': 'R', 'J': 'Q', 'K': 'P', 'L': 'O',
    	'M': 'N', 'N': 'M', 'O': 'L', 'P': 'K', 'Q': 'J', 'R': 'I',
    	'S': 'H', 'T': 'G', 'U': 'F', 'V': 'E', 'W': 'D', 'X': 'C',
    	'Y': 'B', 'Z': 'A', 
    	# Lowercase Alphabets
    	'a': 'z', 'b': 'y', 'c': 'x', 'd': 'w', 'e': 'v', 'f': 'u',
    	'g': 't', 'h': 's', 'i': 'r', 'j': 'q', 'k': 'p', 'l': 'o',
    	'm': 'n', 'n': 'm', 'o': 'l', 'p': 'k', 'q': 'j', 'r': 'i',
    	's': 'h', 't': 'g', 'u': 'F', 'v': 'e', 'w': 'd', 'x': 'c',
    	'y': 'b', 'z': 'a'
    }
    # Creating converted output
    converted_data = ""
    for i in range(0, len(data)):
	    if data[i] in conversion_code.keys():
		    converted_data += conversion_code[data[i]]
	    else:
	    	converted_data += data[i]
    # Printing converted output
    bot.send_message(message.chat.id,f"processed output : {converted_data}")


bot.infinity_polling()
