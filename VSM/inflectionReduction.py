from util import *
from nltk.stem import PorterStemmer
#from nltk.stem import WordNetLemmatizer

class InflectionReduction:

    def reduce(self, text):
        """
        Stemming/Lemmatization

        Parameters
        ----------
        arg1 : list
            A list of lists where each sub-list a sequence of tokens
            representing a sentence

        Returns
        -------
        list
            A list of lists where each sub-list is a sequence of
            stemmed/lemmatized tokens representing a sentence
        """

        reducedText = None
        reducedText = []
        ps = PorterStemmer()
        #lemmatizer = WordNetLemmatizer()

        for s in text:
            stemmed_sentence = []
            for w in s:
                stemmed_sentence.append(ps.stem(w))
                #stemmed_sentence.append(lemmatizer.lemmatize(w))
            reducedText.append(stemmed_sentence)

        return reducedText

