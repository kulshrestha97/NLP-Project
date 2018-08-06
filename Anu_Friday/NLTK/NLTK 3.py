from nltk.corpus import reuters, brown
from nltk.tokenize import TreebankWordTokenizer
import nltk


class col:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


print(col.HEADER+"\nExploring Brown Corpus\n~~~~~~~~~~~~~~~~~~~~~~~~~\n"+col.ENDC)
print(col.OKGREEN+"Categories : "+col.ENDC)
print(brown.categories())
print(col.BOLD+"\nChoosing category \"Cotton\": \n"+col.ENDC)
print(col.OKGREEN+"\nText (First 200 words): "+col.ENDC)
print(" ".join(brown.words(categories="news")[:200]))

print(col.HEADER+"\nExploring Reuters Corpus\n~~~~~~~~~~~~~~~~~~~~~~~~~\n"+col.ENDC)
print(col.OKGREEN + "Categories : " + col.ENDC)
print(reuters.categories())
print(col.BOLD+"\nChoosing category \"Cotton\": \n"+col.ENDC)
print(col.OKGREEN+"\nText (First 200 words): "+col.ENDC)
print(" ".join(reuters.words(categories="cotton")[:200]))
