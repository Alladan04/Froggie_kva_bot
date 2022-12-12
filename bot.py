import telebot
import random
from telebot import types
TOKEN = "5691725353:AAEY1lbBz8Hk2RRnfaXnS3t6pn59LZfReqQ"
bot= telebot.TeleBot(TOKEN)
FROGS = [
"C:/Users/allad/OneDrive/Документы/Frogs/zhivotnye_cherepaha_zhaba_28996.jpg",
"C:/Users/allad/OneDrive/Документы/Frogs/zhivotnye_korona_zhaba_1943.jpg",
"C:/Users/allad/OneDrive/Документы/Frogs/5810bda05abd8b4e67f6158d3f499b00.jpg",
"C:/Users/allad/OneDrive/Документы/Frogs/mesmo-what-means-word.jpeg",
"C:/Users/allad/OneDrive/Документы/Frogs/maxresdefault.jpg",
"C:/Users/allad/OneDrive/Документы/Frogs/1373109097_priroda-v-fokuse-19.jpg",
"C:/Users/allad/OneDrive/Документы/Frogs/zhivotnye_zhaba_7791.jpg"]
@bot.message_handler(commands = ['start'])
def start_handler (msg):
    chat_id = msg.chat.id 
    name = msg.chat.first_name
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard = types.KeyboardButton(text = "Хочу лягуху!")
    markup. add(keyboard)
    bot.send_message(chat_id, f"Ну приветик,{name}!",reply_markup=markup)
    #bot.reply_to(msg, text= "Привет, начнем!")
@bot.message_handler(content_types= 'text')
def text (msg):
    if msg.text == "Хочу лягуху!":
        chat_id = msg.chat.id
        name = msg.chat.first_name
        photo = open(FROGS[random.randint(0,len(FROGS))-1],"rb")
        bot.send_message(chat_id, f"Лови лягуху,{name}!")
        bot.send_photo(chat_id, photo)

@bot.message_handler(func=lambda m: True)
def echo_all(message):
	bot.reply_to(message, message.text)


if __name__ == "__main__":
    bot.infinity_polling()