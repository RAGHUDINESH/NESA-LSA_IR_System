from util import *

# Add your import statements here
import math
import numpy as np

class Evaluation():

	def queryPrecision(self, query_doc_IDs_ordered, query_id, true_doc_IDs, k):
		"""
		Computation of precision of the Information Retrieval System
		at a given value of k for a single query

		Parameters
		----------
		arg1 : list
			A list of integers denoting the IDs of documents in
			their predicted order of relevance to a query
		arg2 : int
			The ID of the query in question
		arg3 : list
			The list of IDs of documents relevant to the query (ground truth)
		arg4 : int
			The k value

		Returns
		-------
		float
			The precision value as a number between 0 and 1
		"""

		precision = -1

		#Fill in code here
		retrieved_k = query_doc_IDs_ordered[0:k]
		rel_and_ret = 0
		for doc_ID in retrieved_k:
			if doc_ID in true_doc_IDs:
				rel_and_ret = rel_and_ret + 1
		precision = rel_and_ret*1.0/k

		return precision


	def meanPrecision(self, doc_IDs_ordered, query_ids, qrels, k):
		"""
		Computation of precision of the Information Retrieval System
		at a given value of k, averaged over all the queries

		Parameters
		----------
		arg1 : list
			A list of lists of integers where the ith sub-list is a list of IDs
			of documents in their predicted order of relevance to the ith query
		arg2 : list
			A list of IDs of the queries for which the documents are ordered
		arg3 : list
			A list of dictionaries containing document-relevance
			judgements - Refer cran_qrels.json for the structure of each
			dictionary
		arg4 : int
			The k value

		Returns
		-------
		float
			The mean precision value as a number between 0 and 1
		"""

		meanPrecision = -1

		#Fill in code here
		precision_sum = 0

		for i in range(len(query_ids)):
			true_doc_IDs = []
			for j in qrels:
				if int(j["query_num"]) == query_ids[i]:
					true_doc_IDs.append(int(j["id"]))
			precision_sum = precision_sum + self.queryPrecision(doc_IDs_ordered[i], query_ids[i], true_doc_IDs, k)
		meanPrecision = precision_sum/len(query_ids)

		return meanPrecision

	
	def queryRecall(self, query_doc_IDs_ordered, query_id, true_doc_IDs, k):
		"""
		Computation of recall of the Information Retrieval System
		at a given value of k for a single query

		Parameters
		----------
		arg1 : list
			A list of integers denoting the IDs of documents in
			their predicted order of relevance to a query
		arg2 : int
			The ID of the query in question
		arg3 : list
			The list of IDs of documents relevant to the query (ground truth)
		arg4 : int
			The k value

		Returns
		-------
		float
			The recall value as a number between 0 and 1
		"""

		recall = -1

		#Fill in code here
		retrieved_k = query_doc_IDs_ordered[0:k]
		rel_and_ret = 0
		for doc_ID in retrieved_k:
			if doc_ID in true_doc_IDs:
				rel_and_ret = rel_and_ret + 1
		recall = rel_and_ret*1.0/len(true_doc_IDs)
		return recall


	def meanRecall(self, doc_IDs_ordered, query_ids, qrels, k):
		"""
		Computation of recall of the Information Retrieval System
		at a given value of k, averaged over all the queries

		Parameters
		----------
		arg1 : list
			A list of lists of integers where the ith sub-list is a list of IDs
			of documents in their predicted order of relevance to the ith query
		arg2 : list
			A list of IDs of the queries for which the documents are ordered
		arg3 : list
			A list of dictionaries containing document-relevance
			judgements - Refer cran_qrels.json for the structure of each
			dictionary
		arg4 : int
			The k value

		Returns
		-------
		float
			The mean recall value as a number between 0 and 1
		"""

		meanRecall = -1

		#Fill in code here
		recall_sum = 0

		for i in range(len(query_ids)):
			true_doc_IDs = []
			for j in qrels:
				if int(j["query_num"]) == query_ids[i]:
					true_doc_IDs.append(int(j["id"]))
			recall_sum = recall_sum + self.queryRecall(doc_IDs_ordered[i], query_ids[i], true_doc_IDs, k)
		meanRecall = recall_sum/len(query_ids)

		return meanRecall


	def queryFscore(self, query_doc_IDs_ordered, query_id, true_doc_IDs, k):
		"""
		Computation of fscore of the Information Retrieval System
		at a given value of k for a single query

		Parameters
		----------
		arg1 : list
			A list of integers denoting the IDs of documents in
			their predicted order of relevance to a query
		arg2 : int
			The ID of the query in question
		arg3 : list
			The list of IDs of documents relevant to the query (ground truth)
		arg4 : int
			The k value

		Returns
		-------
		float
			The fscore value as a number between 0 and 1
		"""

		fscore = -1

		#Fill in code here
		retrieved_k = query_doc_IDs_ordered[0:k]
		rel_and_ret = 0
		for doc_ID in retrieved_k:
			if doc_ID in true_doc_IDs:
				rel_and_ret = rel_and_ret + 1
		precision = rel_and_ret*1.0/k
		recall = rel_and_ret*1.0/len(true_doc_IDs)

		if precision+recall == 0:
			fscore = 0
		else:
			fscore = (2*precision*recall)/(precision+recall)
		return fscore


	def meanFscore(self, doc_IDs_ordered, query_ids, qrels, k):
		"""
		Computation of fscore of the Information Retrieval System
		at a given value of k, averaged over all the queries

		Parameters
		----------
		arg1 : list
			A list of lists of integers where the ith sub-list is a list of IDs
			of documents in their predicted order of relevance to the ith query
		arg2 : list
			A list of IDs of the queries for which the documents are ordered
		arg3 : list
			A list of dictionaries containing document-relevance
			judgements - Refer cran_qrels.json for the structure of each
			dictionary
		arg4 : int
			The k value
		
		Returns
		-------
		float
			The mean fscore value as a number between 0 and 1
		"""

		meanFscore = -1

		#Fill in code here
		Fscore_sum = 0

		for i in range(len(query_ids)):
			true_doc_IDs = []
			for j in qrels:
				if int(j["query_num"]) == query_ids[i]:
					true_doc_IDs.append(int(j["id"]))
			Fscore_sum = Fscore_sum + self.queryFscore(doc_IDs_ordered[i], query_ids[i], true_doc_IDs, k)

		meanFscore = Fscore_sum/len(query_ids)
		return meanFscore

	def queryNDCG(self, query_doc_IDs_ordered, query_id, true_doc_IDs, k):
		"""
        Computation of nDCG of the Information Retrieval System
        at given value of k for a single query

        Parameters
        ----------
        arg1 : list
            A list of integers denoting the IDs of documents in
            their predicted order of relevance to a query
        arg2 : int
            The ID of the query in question
        arg3 : list
            The list of IDs of documents relevant to the query (ground truth)
        arg4 : int
            The k value

        Returns
        -------
        float
            The nDCG value as a number between 0 and 1
        """

		nDCG = -1

		# Fill in code here
		DCG = 0
		IDCG = 0
		retrieved_k = query_doc_IDs_ordered[0:k]
		true_docs_ids = np.array(true_doc_IDs)[:,0]
		true_docs_rel = np.array(true_doc_IDs)[:,1]

		ret_docs_rel = []

		for j in range(len(retrieved_k)):
			for i in range(len(true_docs_ids)):
				if retrieved_k[j] == true_docs_ids[i]:
					ret_docs_rel.append(true_docs_rel[i])
					DCG = DCG + true_docs_rel[i]*1.0/math.log(j+2,2)

		rel_sorted = np.sort(ret_docs_rel)[::-1]
		for i in range(len(rel_sorted)):
			IDCG = IDCG + (rel_sorted[i] * 1.0 / math.log(i + 2, 2))
		if IDCG == 0:
			nDCG = 0
		else:
			nDCG = DCG/IDCG
		return nDCG

	def meanNDCG(self, doc_IDs_ordered, query_ids, qrels, k):
		"""
        Computation of nDCG of the Information Retrieval System
        at a given value of k, averaged over all the queries

        Parameters
        ----------
        arg1 : list
            A list of lists of integers where the ith sub-list is a list of IDs
            of documents in their predicted order of relevance to the ith query
        arg2 : list
            A list of IDs of the queries for which the documents are ordered
        arg3 : list
            A list of dictionaries containing document-relevance
            judgements - Refer cran_qrels.json for the structure of each
            dictionary
        arg4 : int
            The k value

        Returns
        -------
        float
            The mean nDCG value as a number between 0 and 1
        """

		meanNDCG = -1

		# Fill in code here
		NDCG_sum = 0

		for i in range(len(query_ids)):
			true_doc_IDs = []
			for j in qrels:
				if int(j["query_num"]) == query_ids[i]:
					true_doc_IDs.append([int(j["id"]), 5 - j["position"]])
			NDCG_sum = NDCG_sum + self.queryNDCG(doc_IDs_ordered[i], query_ids[i], true_doc_IDs, k)

		meanNDCG = NDCG_sum / len(query_ids)

		return meanNDCG

	def queryAveragePrecision(self, query_doc_IDs_ordered, query_id, true_doc_IDs, k):
		"""
		Computation of average precision of the Information Retrieval System
		at a given value of k for a single query (the average of precision@i
		values for i such that the ith document is truly relevant)

		Parameters
		----------
		arg1 : list
			A list of integers denoting the IDs of documents in
			their predicted order of relevance to a query
		arg2 : int
			The ID of the query in question
		arg3 : list
			The list of documents relevant to the query (ground truth)
		arg4 : int
			The k value

		Returns
		-------
		float
			The average precision value as a number between 0 and 1
		"""

		avgPrecision = -1

		#Fill in code here
		retrieved_k = query_doc_IDs_ordered[0:k]
		precision_sum = 0
		count = 0
		for l in range(k):
			if retrieved_k[l] in true_doc_IDs:
				precision_sum = precision_sum + self.queryPrecision(query_doc_IDs_ordered, query_id, true_doc_IDs, l+1)
				count = count + 1
		if count == 0:
			avgPrecision = 0
		else:
			avgPrecision = precision_sum*1.0/count
		return avgPrecision


	def meanAveragePrecision(self, doc_IDs_ordered, query_ids, q_rels, k):
		"""
		Computation of MAP of the Information Retrieval System
		at given value of k, averaged over all the queries

		Parameters
		----------
		arg1 : list
			A list of lists of integers where the ith sub-list is a list of IDs
			of documents in their predicted order of relevance to the ith query
		arg2 : list
			A list of IDs of the queries
		arg3 : list
			A list of dictionaries containing document-relevance
			judgements - Refer cran_qrels.json for the structure of each
			dictionary
		arg4 : int
			The k value

		Returns
		-------
		float
			The MAP value as a number between 0 and 1
		"""

		meanAveragePrecision = -1


		#Fill in code here
		AP_sum = 0

		for i in range(len(query_ids)):
			true_doc_IDs = []
			for j in q_rels:
				if int(j["query_num"]) == query_ids[i]:
					true_doc_IDs.append(int(j["id"]))
			AP_sum = AP_sum + self.queryAveragePrecision(doc_IDs_ordered[i], query_ids[i], true_doc_IDs, k)

		meanAveragePrecision = AP_sum/len(query_ids)

		return meanAveragePrecision

