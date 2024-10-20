import telebot
import os
import random
import requests
API_TOKEN = "<api_token>"

bot = telebot.TeleBot('7976398571:AAF1maIY7bVLPR4Frct9YQSM7a8sqroAdUg')
img = random.randint(0, 3)

if img == 0:
    @bot.message_handler(commands=['mem'])
    def send_mem(message):
        with open("images/mem1.jpeg", 'rb') as f:
            bot.send_photo(message.chat.id, f)
            
elif img == 1:
    @bot.message_handler(commands=['mem'])
    def send_mem(message):
        with open("images/mem2.jpeg", 'rb') as d:
            bot.send_photo(message.chat.id, d)
            
elif img == 2 or 3:
    @bot.message_handler(commands=['mem'])
    def send_mem(message):
        with open("images/mem3.jpeg", 'rb') as c:
            bot.send_photo(message.chat.id, c)
            
def get_duck_image_url():    
        url = 'https://random-d.uk/api/random'
        res = requests.get(url)
        data = res.json()
        return data['url']

@bot.message_handler(commands=['pymem'])
def send_mem(message):
    with open("images/mem4.jpg", 'rb') as v:
        bot.send_photo(message.chat.id, v)
    
@bot.message_handler(commands=['duck'])
def duck(message):
        '''По команде duck вызывает функцию get_duck_image_url и отправляет URL изображения утки'''
        image_url = get_duck_image_url()
        bot.reply_to(message, image_url)
@bot.message_handler(commands=["poll"])
def create_poll(message):
    bot.send_message(message.chat.id, "English Article Test")
    answer_options = ["a", "an", "the", "-"]

    bot.send_poll(
        chat_id=message.chat.id,
        question="We are going to '' park.",
        options=answer_options,
        type="quiz",
        correct_option_id=2,
        is_anonymous=False,
    )

@bot.message_handler(commands=["poll2"])
def create_poll(message):
    bot.send_message(message.chat.id, "Тест на знание млекопитающих.")
    answer_options = ["Кашалот", "Белый медведь", "Синий кит", "Морской слон"]

    bot.send_poll(
        chat_id=message.chat.id,
        question="Самое круное ХИЩНОЕ млекопитающее, это?",
        options=answer_options,
        type="quiz",
        correct_option_id=0,
        is_anonymous=False,
    )

@bot.message_handler(commands=["poll3"])
def create_poll(message):
    bot.send_message(message.chat.id, "Тест на знание рептилий.")
    answer_options = ["Кошка", "Лягушка", "Змея", "Летучая мышь"]

    bot.send_poll(
        chat_id=message.chat.id,
        question="Какое животное ялвяется рептилией?",
        options=answer_options,
        type="quiz",
        correct_option_id=2,
        is_anonymous=False,
    )

@bot.message_handler(commands=["help"])
def help_user(message):
    bot.send_message(message.chat.id, "Команды: /poll - первый квиз, /poll2 - второй квиз, /poll3 -  третий квиз")

@bot.poll_answer_handler()
def handle_poll(poll):
    # This handler can be used to log User answers and to send next poll
    pass


bot.infinity_polling()
