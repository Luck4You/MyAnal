from src.ddl import bot_text
import telebot 



bot = telebot.TeleBot("7088145772:AAH-xwQGCWjHttMfA9hdNC9cFk29rkKymAs")

@bot.message_handler(content_types=["text"])
def start(message):
    if  message.text.lower() == "/start":
        bot.send_message(message.chat.id, bot_text.__help)  
        bot.register_next_step_handler(message, foo)
        
    if  message.text.lower() == "/name":
        bot.send_message(message.chat.id, f"Твоё имя: {name}") 
  
def foo(message):
    global name
    name = message.text.lower()
    bot.send_message(message.chat.id, "Спасибо, я запомню")
    
bot.polling(none_stop=True)


