#!/usr/bin/env python
# -*- coding: utf-8 -*-


import requests
import datetime

import config
import telebot

## TOKEN - INSERT YOUR TOKEN HERE
token = "500356225:AAEzQwaTne7NgT1sxpJThEm7YrER7aGtxxg"


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе
    bot.send_message(message.chat.id, message.text)

if __name__ == '__main__':
     bot.polling(none_stop=True)
