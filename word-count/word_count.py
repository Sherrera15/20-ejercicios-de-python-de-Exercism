import re, collections


def count_words(sentence):
    word = re.findall("[a-zA-Z\d]+(?:\'t)?", sentence.lower())
    return collections.Counter(word)