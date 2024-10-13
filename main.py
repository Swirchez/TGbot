import telebot

API_TOKEN = "<api_token>"

bot = telebot.TeleBot(My_ToKeN)


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
