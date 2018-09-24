"""
Labour work #1

Count frequencies dictionary by the given arbitrary text
"""
from builtins import str


def calculate_frequences(texts: str) -> dict:
    my_first_dict = {}
    bykva = ''
    texts_list = []

    if texts == '' or texts is None or type(texts) != str:
        return {}
    if type(texts) is str:
        texts = texts.lower()

        for bykva in texts:
            if bykva not in 'abcdefghijklmnopqrstuvwxyz':
                texts = texts.replace(bykva, '')
            if texts.isdigit():
                continue
            if bykva in 'abcdefghijklmnopqrstuvwxyz':
                texts_list.append(bykva)

        texts = texts.split('')

        for bykva in texts_list:
            count_bykva = texts_list.count(bykva)
            my_first_dict[bykva] = count_bykva
            return my_first_dict
        else:
            return {}


def filter_stop_words(my_first_dict: dict, STOP_WORDS: tuple) -> dict:

    if my_first_dict is None:
        return {}
    if STOP_WORDS is None:
        return {}

    my_second_dict = my_first_dict.copy()

    for new_stop_word in STOP_WORDS:
        if new_stop_word in my_second_dict:
            my_second_dict.pop(new_stop_word)
    for key in my_second_dict.keys():
        if type(key) == str and key not in STOP_WORDS:
            my_second_dict[key] = my_first_dict[key]
    return my_second_dict


def get_top_n(my_second_dict: dict, top_n: int) -> tuple:

    top_my_list = []
    if top_n <= 0:
        return()

    for key, value in my_second_dict.items():
        top_my_list.append([value, key])
        tuple_top_n = tuple(top_my_list[:top_n])
    return tuple(top_my_list)
 #my_second_dict = sorted(my_second_dict.items(), key = lambda bykva: bykva[1], reverse = True)

