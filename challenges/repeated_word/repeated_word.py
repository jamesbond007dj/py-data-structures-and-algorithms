import re
import collections

def repeated_word(lengthy):
    punctuation = '''!()-[]{};:'",<>./?@#$%^&*_~'''
    lengthy = lengthy.lower().replace(punctuation, '')
    words = lengthy.split(' ')
    collection = { }
    for word in words:
        if collection.get(word):
            return word
        else:
            collection[word]=1
    return None