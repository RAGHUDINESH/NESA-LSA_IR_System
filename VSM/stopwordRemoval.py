from util import *

from nltk.corpus import stopwords

class StopwordRemoval():

    def fromList(self, text):
        """
        Sentence Segmentation using the Punkt Tokenizer

        Parameters
        ----------
        arg1 : list
            A list of lists where each sub-list is a sequence of tokens
            representing a sentence

        Returns
        -------
        list
            A list of lists where each sub-list is a sequence of tokens
            representing a sentence with stopwords removed
        """

        stopwordRemovedText = None
        stop_words = stopwords.words("english")
        stopwordRemovedText = []

        for s in text:
            filtered_sentence = []
            for w in s:
                if w not in stop_words:
                    filtered_sentence.append(w)
            stopwordRemovedText.append(filtered_sentence)
        return stopwordRemovedText