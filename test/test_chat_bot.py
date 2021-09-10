import os
import unittest

from src.chat import chatbot_response

HEAD, TAIL = os.path.split(os.getcwd())
MODEL_PATH = HEAD + '/src/model/chatbot_model.h5'
INTENTS_PATH = HEAD + '/src/model/intents.json'
WORDS_PATH = HEAD + '/src/model/words.pkl'
CLASSES_PATH = HEAD + '/src/model/classes.pkl'


class TestChatBot(unittest.TestCase):
    def test_salutation(self):
        intent, reponse = chatbot_response("Salut", MODEL_PATH, INTENTS_PATH, WORDS_PATH, CLASSES_PATH)
        self.assertEqual(intent[0]["intent"], "salutation")

        intent, reponse = chatbot_response("Bonjour", MODEL_PATH, INTENTS_PATH, WORDS_PATH, CLASSES_PATH)
        self.assertEqual(intent[0]["intent"], "salutation")

        intent, reponse = chatbot_response("Hello", MODEL_PATH, INTENTS_PATH, WORDS_PATH, CLASSES_PATH)
        self.assertEqual(intent[0]["intent"], "salutation")

        intent, reponse = chatbot_response("Salut toi", MODEL_PATH, INTENTS_PATH, WORDS_PATH, CLASSES_PATH)
        self.assertEqual(intent[0]["intent"], "salutation")

        intent, reponse = chatbot_response("Hey", MODEL_PATH, INTENTS_PATH, WORDS_PATH, CLASSES_PATH)
        self.assertEqual(intent[0]["intent"], "salutation")

    def test_comment_tu_vas(self):
        intent, reponse = chatbot_response("Ca va?", MODEL_PATH, INTENTS_PATH, WORDS_PATH, CLASSES_PATH)
        self.assertEqual(intent[0]["intent"], "comment_tu_vas")

        intent, reponse = chatbot_response("Comment tu vas?", MODEL_PATH, INTENTS_PATH, WORDS_PATH, CLASSES_PATH)
        self.assertEqual(intent[0]["intent"], "comment_tu_vas")

        intent, reponse = chatbot_response("Tu vas bien?", MODEL_PATH, INTENTS_PATH, WORDS_PATH, CLASSES_PATH)
        self.assertEqual(intent[0]["intent"], "comment_tu_vas")

        intent, reponse = chatbot_response("Comment ça va ?", MODEL_PATH, INTENTS_PATH, WORDS_PATH, CLASSES_PATH)
        self.assertEqual(intent[0]["intent"], "comment_tu_vas")

    def test_au_revoir(self):
        intent, reponse = chatbot_response("A+", MODEL_PATH, INTENTS_PATH, WORDS_PATH, CLASSES_PATH)
        self.assertEqual(intent[0]["intent"], "au_revoir")

        intent, reponse = chatbot_response("Bye", MODEL_PATH, INTENTS_PATH, WORDS_PATH, CLASSES_PATH)
        self.assertEqual(intent[0]["intent"], "au_revoir")

        intent, reponse = chatbot_response("Ciao", MODEL_PATH, INTENTS_PATH, WORDS_PATH, CLASSES_PATH)
        self.assertEqual(intent[0]["intent"], "au_revoir")

        intent, reponse = chatbot_response("Au revoir", MODEL_PATH, INTENTS_PATH, WORDS_PATH, CLASSES_PATH)
        self.assertEqual(intent[0]["intent"], "au_revoir")


