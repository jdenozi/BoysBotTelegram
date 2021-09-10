import os
from typing import List

import nltk
from nltk.stem import WordNetLemmatizer

import pickle
import numpy as np
import nltk
import json
import random
from keras.models import load_model

nltk.download('punkt')
nltk.download('wordnet')
lemmatizer = WordNetLemmatizer()

MODEL_PATH = os.getcwd() + '/model/chatbot_model.h5'
INTENTS_PATH = os.getcwd() + '/model/intents.json'
WORDS_PATH = os.getcwd() + '/model/words.pkl'
CLASSES_PATH = os.getcwd() + '/model/classes.pkl'


def clean_up_sentence(sentence: str) -> List:
    """
    Clean the message and transform it into sentence lemmatized
    :param sentence: String mesage
    :return: List of lemmatized word
    """
    # tokenize the pattern - split words into array
    sentence_words = nltk.word_tokenize(sentence)
    # stem each word - create short form for word
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words


# return bag of words array: 0 or 1 for each word in the bag that exists in the sentence

def bow(sentence, words, show_details=True):
    # tokenize the pattern
    sentence_words = clean_up_sentence(sentence)
    # bag of words - matrix of N words, vocabulary matrix
    bag = [0] * len(words)
    for s in sentence_words:
        for i, w in enumerate(words):
            if w == s:
                # assign 1 if current word is in the vocabulary position
                bag[i] = 1
                if show_details:
                    print("found in bag: %s" % w)
    return (np.array(bag))


def predict_class(sentence: str, model, words_path: str, classes_path: str) -> List:
    # Open file
    with open(words_path, 'rb') as wp, open(classes_path, 'rb') as cp:
        # filter out predictions below a threshold
        words = pickle.load(wp)
        classes = pickle.load(cp)

        p = bow(sentence, words, show_details=False)
        res = model.predict(np.array([p]))[0]
        ERROR_THRESHOLD = 0.25
        results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
        # sort by strength of probability
        results.sort(key=lambda x: x[1], reverse=True)
        return_list = []

        for r in results:
            return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
        return return_list


def get_response(ints, intents_json):
    tag = ints[0]['intent']
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if (i['tag'] == tag):
            result = random.choice(i['responses'])
            return result


def get_event(ints, intents_jon):
    pass


def chatbot_response(msg: str, path_model: str = MODEL_PATH, intents_path: str = INTENTS_PATH, words_path=WORDS_PATH, classes_path=CLASSES_PATH):
    model = load_model(path_model)
    ints = predict_class(msg, model, words_path, classes_path)

    with open(intents_path) as ip:
        intents = json.loads(ip.read())
        res = get_response(ints, intents)
        return ints, res
