#!/usr/bin/env python3
# Dev:???
token = "8813237748:AAFCzliA30Dzyf-bfB4dnkwdXVZk5sIJA70"

import os
from random import randint
from telebot import TeleBot
from telebot.types import Message
from fake_useragent import FakeUserAgent

fua = FakeUserAgent()
bot = TeleBot(token)
print("started")

print("making by @ghost_of_notover")

def createString(string: str) -> str:
    return string.lower().translate(string.maketrans("qwertyuiopasdfghjklzxcvbnm-0123456789", "ǫᴡᴇʀᴛʏᴜɪᴏᴘᴀsᴅғɢʜᴊᴋʟᴢxᴄᴠʙɴᴍ-0123456789"))

@bot.message_handler(content_types=["text"], chat_types=["private", "supergroup"])
def onMessages(msg: Message):
    print(msg.text + " " + msg.from_user.full_name)

    if msg.text in ("/start", "/help"):
        bot.reply_to(msg, createString("🔺️ Welcome to Fake Useragent Generator bot, use") + " /generate " + createString("to create a fake one 🌐\n\nalso use") + " /addrange <NUMBER> " + createString("to create user agents more than one 🕷"))

    elif msg.text.strip() == "/generate":
        bot.reply_to(msg, createString("User Agent: ") + f"```{fua.random}```", parse_mode="Markdown")

    elif msg.text.strip().startswith( "/addrange"):
        splt = msg.text.strip()[10:].strip()

        if splt.isdigit():
            if 1 < int(splt) < 1000:
                rnd_range = randint(100, 999999)
                file = open(f"rut_{rnd_range}.txt", "a")
                for useragent in range(int(splt)):
                    file.write( fua.random + "\n" )

                file.close()
                bot.send_document(msg.chat.id, document=open(f"rut_{rnd_range}.txt", "rb"), caption=createString(f"{splt} User Agents "), reply_to_message_id=msg.message_id)

                os.remove(f"rut_{rnd_range}.txt")

            else:
                bot.reply_to(msg, createString("range should be in between of 1 - 1000 "))

        else: bot.reply_to(msg, createString("range was not detect "))


bot.polling()
