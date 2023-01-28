from natasha_parser import Natasha_Parser
from generate_rus_vocab import vocab
import re

re.compile('[А-Яа-яЁё]+')

def spelling_corrector(filename):
    nap = Natasha_Parser(filename)
    nap.segmentation()

    words = [_.text for _ in nap.doc.tokens if _.text.isalpha() or re.match(r'[А-я+][-][А-я+]', _.text, re.U)] # only letter-words
    for word in words:
        if word not in vocab:
            print(word)

filename = './test/test.txt'
spelling_corrector(filename)