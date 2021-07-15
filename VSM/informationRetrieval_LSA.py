from util import *

# Add your import statements here
import math
import numpy as np


class InformationRetrieval():

	def __init__(self):
		self.index = None
		self.vocab = None
		self.IDF = None
		self.docIDs = None

	def buildIndex(self, docs, docIDs):
		"""
		Builds the document index in terms of the document
		IDs and stores it in the 'index' class variable

		Parameters
		----------
		arg1 : list
			A list of lists of lists where each sub-list is
			a document and each sub-sub-list is a sentence of the document
		arg2 : list
			A list of integers denoting IDs of the documents
		Returns
		-------
		None
		"""

		index = None
		#Fill in code here
		inv_index={}

		for i in range(len(docs)):
			for sent in docs[i]:
				for word in sent:
					if word not in inv_index:
						inv_index[word] = [[docIDs[i],0]]
					if inv_index[word][-1][0] == docIDs[i]:
						inv_index[word][-1][1] = inv_index[word][-1][1] + 1
					else:
						inv_index[word].append([docIDs[i],1])

		vocab = [i for i in inv_index.keys()]
		N = len(docs)
		IDF = {}
		for keys in vocab:
			IDF[keys] = math.log(N*1.0/len(inv_index[keys]),10)

		TF_IDF = np.zeros([len(docs),len(vocab)])

		for i in range(len(docs)):
			for sent in docs[i]:
				for word in sent:
					if word in vocab:
						TF_IDF[i][vocab.index(word)]= TF_IDF[i][vocab.index(word)] + IDF[word]

		index = TF_IDF

		self.IDF = IDF
		self.vocab = vocab
		self.index = index
		self.docIDs = docIDs

	def rank(self, queries):
		"""
		Rank the documents according to relevance for each query

		Parameters
		----------
		arg1 : list
			A list of lists of lists where each sub-list is a query and
			each sub-sub-list is a sentence of the query
		

		Returns
		-------
		list
			A list of lists of integers where the ith sub-list is a list of IDs
			of documents in their predicted order of relevance to the ith query
		"""

		doc_IDs_ordered = []

		#Fill in code here
		TF_IDF = np.zeros([len(queries), len(self.vocab)])
		for i in range(len(queries)):
			for sent in queries[i]:
				for word in sent:
					if word in self.vocab:
						TF_IDF[i][self.vocab.index(word)] = TF_IDF[i][self.vocab.index(word)] + self.IDF[word]

		cos_sim = np.dot(TF_IDF, np.transpose(self.index))

		for i in range(len(queries)):
			for j in range(len(self.index)):
				if np.linalg.norm(self.index[j]) == 0:
					cos_sim[i][j] = 0
				else:
					cos_sim[i][j] = cos_sim[i][j] * (1/np.linalg.norm(TF_IDF[i])) * (1/np.linalg.norm(self.index[j]))


		for i in cos_sim:
			sorted_sim = np.argsort(i)[::-1]
			doc_IDs_ordered.append([self.docIDs[j] for j in sorted_sim])

		return doc_IDs_ordered




