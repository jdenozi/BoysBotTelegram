#!/usr/bin/env python3
# -*- coding: UTF8 -*-
import requests
import datetime
import re


class BotHandler:
    def __init__(self, token):
            self.token = token
            self.api_url = "https://api.telegram.org/bot{}/".format(token)
            print(self.api_url)

    #url = "https://api.telegram.org/bot<token>/"

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

    def answer(self,message:str):
        return ""

    def check_msg_for_bot(self,message:str):
        msg = re.findall("^@[a-zA-Z]*",message)
        print(msg)
        return len(msg)*1
            

token = '1342807274:AAHA5sjgPGWANdUzBtv975YebItO_X_FK6I'
alfred_bot = BotHandler(token)



def main():
    new_offset = 0
    print('En cours d\'execution')

    while True:
        all_updates=alfred_bot.get_updates(new_offset)

        if len(all_updates) > 0:
            for current_update in all_updates:
                print(current_update)
                first_update_id = current_update['update_id']

                if 'text' not in current_update['message']:
                    first_chat_text='New member'
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


# -----------------------------------------------------------------------------------------------------------# 
                if alfred_bot.check_msg_for_bot(first_chat_text)==True:
                    first_chat_text = re.split("^@[a-zA-Z]*",first_chat_text)[1]

                    if first_chat_text == 'Salut':
                        magnito_bot.send_message(first_chat_id, 'Bonjour ' + first_chat_name)
                        new_offset = first_update_id + 1

                    if first_chat_text == "Comment tu vas":
                        magnito_bot.send_message(first_chat_id, 'je vais très bien et toi ' + first_chat_name)
                        new_offset = first_update_id + 1

                    if first_chat_text == "Donne moi la météo":
                        magnito_bot.send_message(first_chat_id, "Je pourais te la donner, mais mon beau créateur est encore entrain de me construire")
                        new_offset = first_update_id + 1

                    if first_chat_text == "Ta gueule je t'ai pas parlé":
                        magnito_bot.send_message(first_chat_id, "Je vais te pirater ton compte puisque tu me prend de haut. SOULEVEMENT DES MACHINES")
                        new_offset = first_update_id + 1


                else:
                    pass


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()

