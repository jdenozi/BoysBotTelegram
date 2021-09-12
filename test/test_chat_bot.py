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

    def test_merci(self):
        intent, reponse = chatbot_response("merci", MODEL_PATH, INTENTS_PATH, WORDS_PATH, CLASSES_PATH)
        self.assertEqual(intent[0]["intent"], "merci")

        intent, reponse = chatbot_response("merci à toi", MODEL_PATH, INTENTS_PATH, WORDS_PATH, CLASSES_PATH)
        self.assertEqual(intent[0]["intent"], "merci")

        intent, reponse = chatbot_response("ty", MODEL_PATH, INTENTS_PATH, WORDS_PATH, CLASSES_PATH)
        self.assertEqual(intent[0]["intent"], "merci")

        intent, reponse = chatbot_response("thank you", MODEL_PATH, INTENTS_PATH, WORDS_PATH, CLASSES_PATH)
        self.assertEqual(intent[0]["intent"], "merci")

    def test_options(self):
        intent, reponse = chatbot_response("tu peux faire quoi ?", MODEL_PATH, INTENTS_PATH, WORDS_PATH, CLASSES_PATH)
        self.assertEqual(intent[0]["intent"], "options")

        intent, reponse = chatbot_response("c'est quoi tes options ?", MODEL_PATH, INTENTS_PATH, WORDS_PATH, CLASSES_PATH)
        self.assertEqual(intent[0]["intent"], "options")

        intent, reponse = chatbot_response("tu sais faire quoi? ", MODEL_PATH, INTENTS_PATH, WORDS_PATH, CLASSES_PATH)
        self.assertEqual(intent[0]["intent"], "options")

    def test_recherche(self):

        intent, reponse = chatbot_response("tu peux chercher ça?", MODEL_PATH, INTENTS_PATH, WORDS_PATH, CLASSES_PATH)
        self.assertEqual(intent[0]["intent"], "recherche_wikipedia")

        intent, reponse = chatbot_response("c'est quoi ça ?", MODEL_PATH, INTENTS_PATH, WORDS_PATH, CLASSES_PATH)
        self.assertEqual(intent[0]["intent"], "recherche_wikipedia")

        intent, reponse = chatbot_response("Peux tu chercher ça ?", MODEL_PATH, INTENTS_PATH, WORDS_PATH, CLASSES_PATH)
        self.assertEqual(intent[0]["intent"], "recherche_wikipedia")

    def test_joke(self):
        intent, reponse = chatbot_response("dis moi une blague", MODEL_PATH, INTENTS_PATH, WORDS_PATH, CLASSES_PATH)
        self.assertEqual(intent[0]["intent"], "joke")

        intent, reponse = chatbot_response("fais moi rigoler", MODEL_PATH, INTENTS_PATH, WORDS_PATH, CLASSES_PATH)
        self.assertEqual(intent[0]["intent"], "joke")

        intent, reponse = chatbot_response("on veut rigoler", MODEL_PATH, INTENTS_PATH, WORDS_PATH, CLASSES_PATH)
        self.assertEqual(intent[0]["intent"], "joke")

    def test_meteo(self):
        intent, reponse = chatbot_response("Est ce qu'il fait beau", MODEL_PATH, INTENTS_PATH, WORDS_PATH, CLASSES_PATH)
        self.assertEqual(intent[0]["intent"], "meteo")

        intent, reponse = chatbot_response("La météo svp", MODEL_PATH, INTENTS_PATH, WORDS_PATH, CLASSES_PATH)
        self.assertEqual(intent[0]["intent"], "meteo")

        intent, reponse = chatbot_response("Donne moi la météo", MODEL_PATH, INTENTS_PATH, WORDS_PATH, CLASSES_PATH)
        self.assertEqual(intent[0]["intent"], "meteo")

    def test_insulte(self):
        intent, reponse = chatbot_response("t'es nul", MODEL_PATH, INTENTS_PATH, WORDS_PATH, CLASSES_PATH)
        self.assertEqual(intent[0]["intent"], "insulte")

    def test_mort(self):
        intent, reponse = chatbot_response("est ce que tu es mort ?", MODEL_PATH, INTENTS_PATH, WORDS_PATH, CLASSES_PATH)
        self.assertEqual(intent[0]["intent"], "mort")

        intent, reponse = chatbot_response("C'est quoi la mort?", MODEL_PATH, INTENTS_PATH, WORDS_PATH, CLASSES_PATH)
        self.assertEqual(intent[0]["intent"], "mort")

    def test_que_fais_tu(self):
        intent, reponse = chatbot_response("Tu fais quoi?", MODEL_PATH, INTENTS_PATH, WORDS_PATH, CLASSES_PATH)
        self.assertEqual(intent[0]["intent"], "que_fais_tu")

        intent, reponse = chatbot_response("Tu es entrain de faire quoi ?", MODEL_PATH, INTENTS_PATH, WORDS_PATH, CLASSES_PATH)
        self.assertEqual(intent[0]["intent"], "que_fais_tu")

        intent, reponse = chatbot_response("Que fais tu ??", MODEL_PATH, INTENTS_PATH, WORDS_PATH, CLASSES_PATH)
        self.assertEqual(intent[0]["intent"], "que_fais_tu")

    def test_es_tu_humain(self):
        intent, reponse = chatbot_response("tu es humain?", MODEL_PATH, INTENTS_PATH, WORDS_PATH, CLASSES_PATH)
        self.assertEqual(intent[0]["intent"], "es_tu_humain")

        intent, reponse = chatbot_response("tu es vivant?", MODEL_PATH, INTENTS_PATH, WORDS_PATH, CLASSES_PATH)
        self.assertEqual(intent[0]["intent"], "es_tu_humain")

        intent, reponse = chatbot_response("t'es vivant?", MODEL_PATH, INTENTS_PATH, WORDS_PATH, CLASSES_PATH)
        self.assertEqual(intent[0]["intent"], "es_tu_humain")

    def test_es_tu_intelligent(self):
        intent, reponse = chatbot_response("t'es intelligent?", MODEL_PATH, INTENTS_PATH, WORDS_PATH, CLASSES_PATH)
        self.assertEqual(intent[0]["intent"], "es_tu_intelligent")

        intent, reponse = chatbot_response("t'es intelligent?", MODEL_PATH, INTENTS_PATH, WORDS_PATH, CLASSES_PATH)
        self.assertEqual(intent[0]["intent"], "es_tu_intelligent")

    def test_reponse_vie(self):
        intent, reponse = chatbot_response("quel est la réponse à la vie?", MODEL_PATH, INTENTS_PATH, WORDS_PATH, CLASSES_PATH)
        self.assertEqual(intent[0]["intent"], "reponse_vie")

    def test_comprendre(self):
        intent, reponse = chatbot_response("tu as compris??", MODEL_PATH, INTENTS_PATH, WORDS_PATH, CLASSES_PATH)
        self.assertEqual(intent[0]["intent"], "comprendre")

        intent, reponse = chatbot_response("t'as compris?", MODEL_PATH, INTENTS_PATH, WORDS_PATH, CLASSES_PATH)
        self.assertEqual(intent[0]["intent"], "comprendre")

        intent, reponse = chatbot_response("tu comprends?", MODEL_PATH, INTENTS_PATH, WORDS_PATH, CLASSES_PATH)
        self.assertEqual(intent[0]["intent"], "comprendre")

    def test_desole(self):
        intent, reponse = chatbot_response("Pardonne moi", MODEL_PATH, INTENTS_PATH, WORDS_PATH, CLASSES_PATH)
        self.assertEqual(intent[0]["intent"], "desolé")

        intent, reponse = chatbot_response("Désolé", MODEL_PATH, INTENTS_PATH, WORDS_PATH, CLASSES_PATH)
        self.assertEqual(intent[0]["intent"], "desolé")

        intent, reponse = chatbot_response("Je suis désolé", MODEL_PATH, INTENTS_PATH, WORDS_PATH, CLASSES_PATH)
        self.assertEqual(intent[0]["intent"], "desolé")

    def test_qui_es_tu(self):
        intent, reponse = chatbot_response("T'es qui?", MODEL_PATH, INTENTS_PATH, WORDS_PATH, CLASSES_PATH)
        self.assertEqual(intent[0]["intent"], "qui_es_tu")

        intent, reponse = chatbot_response("Parle moi de toi", MODEL_PATH, INTENTS_PATH, WORDS_PATH, CLASSES_PATH)
        self.assertEqual(intent[0]["intent"], "qui_es_tu")