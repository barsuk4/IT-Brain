import spacy

nlp = spacy.load('uk_core_news_sm')

print("Enter two space-separated words")
words = input()

tokens = nlp(words)

for token in tokens:
	# Printing the following attributes of each token.
	# text: the word string, has_vector: if it contains
	# a vector representation in the model,
	# vector_norm: the algebraic norm of the vector,
	# is_oov: if the word is out of vocabulary.
	print(token.text, token.has_vector, token.vector_norm, token.is_oov)

token1, token2 = tokens[0], tokens[1]

print(token1, token2)

print("Similarity:", token1.similarity(token2))
