from nltk.corpus import reuters, brown
from nltk.tokenize import TreebankWordTokenizer
import nltk


print("\nExploring Brown Corpus\n~~~~~~~~~~~~~~~~~~~~\n")
print("Categories : ")
print(brown.categories())
print("\nChoosing category \"News\": \n")
print("\nText: ")
print(" ".join(brown.words(categories="news")))
