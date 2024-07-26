from src.ddl import bot_text
from src import json_extract as je
import telebot 



bot = telebot.TeleBot("7088145772:AAE7q550EfrV4iofg_v8ow1FEsA9NNtmfeM")

@bot.message_handler(content_types=["text"])
def start(message):
    if  message.text.lower() == "/start":
        bot.send_message(message.chat.id, bot_text.__help)  
        bot.register_next_step_handler(message, foo)
        
  
def foo(message):
    dict_with = je.send_request_to_dict(message.text)
    for obj in dict_with:
        bot.send_message(message.chat.id, f"Покупка: {obj}") 
        
bot.polling(none_stop=True)