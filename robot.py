#!/usr/bin/env python
# -*- coding: utf-8 -*-


import requests
import datetime

class BotHandler:

    def __init__(self, token):
        self.token = token
        self.api_url = "https://api.telegram.org/bot{}/".format(token)

    def get_updates(self, offset=None, timeout=5):
        method = 'getUpdates'
        params = {'timeout': timeout, 'offset': offset}
        resp = requests.get(self.api_url + method, params)
        result_json = resp.json()['result']
        return result_json

    def send_message(self, chat_id, text):
        params = {'chat_id': chat_id, 'text': text}
        method = 'sendMessage'
        resp = requests.post(self.api_url + method, params)
        return resp

    def get_last_update(self):
        get_result = self.get_updates()

        if len(get_result) > 0:
            last_update = get_result[-1]
        else:
            last_update = None

        return last_update

## TOKEN - INSERT YOUR TOKEN HERE
token = "500356225:AAEzQwaTne7NgT1sxpJThEm7YrER7aGtxxg"


@bot.message_handler(commands=['start'])
def start(m):
    msg = bot.send_message(m.chat.id, 'Как тебя зовут?')


bot.polling()


