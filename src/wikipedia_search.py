import json
import wikipedia

wikipedia.set_lang("fr")

ERROR_CANNOT_FIND_RES = "ERROR cannot find the word given "
def search_on_wikipedia(key_word: str) -> str:
    """
    Search the summary on wikipedia with the key work given
    :param key_word: Keyword given
    :return Summary of the given keyword
    """
    try :
        res = wikipedia.summary(key_word, sentences=1)
        return res
    except Exception as e:
        return e


