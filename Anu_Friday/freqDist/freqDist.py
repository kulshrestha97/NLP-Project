from nltk.corpus import reuters
from nltk.tokenize import TreebankWordTokenizer
import nltk

#words = TreebankWordTokenizer().tokenize(reuters)
print(reuters.categories())

# use conditional freq dist to fint 2 letter, 3 letter frequency
# Find longest words
# segment chinese, japanese data


cfd = nltk.ConditionalFreqDist((genre, word) for genre in reuters.categories(
) for word in reuters.words(categories=genre))
cfd.tabulate()
