#!/usr/bin/env python3
# -*- coding: UTF8 -*-
import os

import requests
import re
from src.chat import chatbot_response
from src.weather import get_weather
from src.wikipedia_search import search_on_wikipedia

TELEGRAM_API_KEY = os.environ.get("TELEGRAM_API_KEY")
MODEL_PATH = os.getcwd() + '/src//model/chatbot_model.h5'
INTENTS_PATH = os.getcwd() + '/src/model/intents.json'
WORDS_PATH = os.getcwd() + '/src/model/words.pkl'
CLASSES_PATH = os.getcwd() + '/src/model/classes.pkl'


class BotHandler:
    def __init__(self, token):
        self.token = token
        self.api_url = "https://api.telegram.org/bot{}/".format(token)
        print(self.api_url)

    def get_updates(self, offset=0, timeout=30):
        method = 'getUpdates'
        params = {'timeout': timeout, 'offset': offset}
        resp = requests.get(self.api_url + method, params)
        result_json = resp.json()['result']
        return result_json

    def send_message(self, chat_id, text):
        params = {'chat_id': chat_id, 'text': text, 'parse_mode': 'HTML'}
        method = 'sendMessage'
        resp = requests.post(self.api_url + method, params)
        return resp

    def get_first_update(self):
        get_result = self.get_updates()

        if len(get_result) > 0:
            last_update = get_result[0]
        else:
            last_update = None

        return last_update

    def answer(self, message: str):
        return ""

    def check_msg_for_bot(self, message: str):
        msg = re.search(r"^(@Alfredo_bot)", message)
        if msg is not None:
            return True
        else:
            return False


bot = BotHandler(TELEGRAM_API_KEY)


def main():
    new_offset = 0
    print('En cours d\'execution')

    while True:
        all_updates = bot.get_updates(new_offset)

        if len(all_updates) > 0:
            for current_update in all_updates:
                first_update_id = current_update['update_id']
                try:
                    if 'message' in current_update:
                        if 'text' not in current_update['message']:
                            first_chat_text = 'New member'
                        else:
                            first_chat_text = current_update['message']['text']
                            first_chat_id = current_update['message']['chat']['id']

                        if 'first_name' in current_update['message']:
                            first_chat_name = current_update['message']['chat']['first_name']

                        elif 'new_chat_member' in current_update['message']:
                            first_chat_name = current_update['message']['new_chat_member']['first_name']

                        elif 'from' in current_update['message']:
                            first_chat_name = current_update['message']['from']['first_name']
                        else:
                            first_chat_name = "unknown"


                except Exception as e:
                    print("Error {}".format(e))

                if bot.check_msg_for_bot(first_chat_text) is True:
                    first_chat_text = re.split("^@[a-zA-Z]*", first_chat_text)[1]

                    intent, response = chatbot_response(first_chat_text, MODEL_PATH, INTENTS_PATH, WORDS_PATH, CLASSES_PATH)

                    if intent[0]["intent"] == "meteo":
                        first_chat_id, first_chat_text, new_offset = send_meteo(first_chat_id, first_chat_text,
                                                                                first_update_id, new_offset, response)
                    if intent[0]["intent"] == "recherche_wikipedia":
                        first_chat_id, first_chat_text, new_offset = send_result_research_wikipedia(first_chat_id,
                                                                                                    first_chat_text,
                                                                                                    first_update_id,
                                                                                                    new_offset,
                                                                                                    response)

                    else:
                        print(response)
                        bot.send_message(first_chat_id, response)
                        new_offset = first_update_id + 1


def send_result_research_wikipedia(first_chat_id, first_chat_text, first_update_id, new_offset, response):
    bot.send_message(first_chat_id, response)
    bot.send_message(first_chat_id, "Pouvez vous me donner le mot clé de votre recherche?")
    new_offset = first_update_id + 1
    receive_message = False
    while receive_message is False:
        updates = bot.get_updates(new_offset)
        for current_update in updates:
            first_update_id = current_update['update_id']

            if 'message' in current_update:
                if 'text' not in current_update['message']:
                    first_chat_text = 'New member'
                else:
                    first_chat_text = current_update['message']['text']
                    first_chat_id = current_update['message']['chat']['id']
                    weather_response = search_on_wikipedia(first_chat_text)
                    bot.send_message(first_chat_id, weather_response)
                    receive_message = True
    return first_chat_id, first_chat_text, new_offset


def send_meteo(first_chat_id, first_chat_text, first_update_id, new_offset, response):
    bot.send_message(first_chat_id, response)
    bot.send_message(first_chat_id, "Pouvez vous me donner le nom de la ville ?")
    new_offset = first_update_id + 1
    receive_message = False
    while receive_message is False:
        updates = bot.get_updates(new_offset)
        for current_update in updates:
            first_update_id = current_update['update_id']

            if 'message' in current_update:
                if 'text' not in current_update['message']:
                    first_chat_text = 'New member'
                else:
                    first_chat_text = current_update['message']['text']
                    first_chat_id = current_update['message']['chat']['id']
                    weather_response = get_weather(first_chat_text)
                    bot.send_message(first_chat_id, weather_response)
                    receive_message = True
    return first_chat_id, first_chat_text, new_offset


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
