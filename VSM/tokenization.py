from util import *

from nltk.tokenize import TreebankWordTokenizer

class Tokenization():

    def naive(self, text):

        tokenizedText = None
        tokenizedText = []
        for sentence in text:
            tokenizedText.append(sentence.split(' '))

        return tokenizedText

    def pennTreeBank(self, text):

        tokenizedText = None
        tokenizedText = []
        for sentence in text:
            tokenizedText.append(TreebankWordTokenizer().tokenize(sentence))

        return tokenizedText
