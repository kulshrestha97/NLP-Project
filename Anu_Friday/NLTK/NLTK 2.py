from nltk.corpus import reuters
from nltk.probability import FreqDist, ConditionalFreqDist
from nltk.tokenize import RegexpTokenizer
import matplotlib.pyplot as plt
from wordcloud import WordCloud


class col:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def printFD(matrix):
    s = [[str(e) for e in row] for row in matrix]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
    table = [fmt.format(*row) for row in s]
    print('\n'.join(table))


print(col.HEADER+"\nExploring Reuters Corpus\n~~~~~~~~~~~~~~~~~~~~~~~~~\n"+col.ENDC)

fdist = FreqDist(word
                 for word in RegexpTokenizer(r'\w+').tokenize(" ".join(reuters.words())))
matrix = fdist.most_common(20)
fdist.plot(30, cumulative=False)
print(col.OKGREEN+"Frequency Distribution of top 20 words:\n"+col.ENDC)
printFD(matrix)

unique_string = (" ").join(reuters.words())

wordcloud = WordCloud(width=1000, height=500).generate(unique_string)
plt.figure(figsize=(15, 8))
plt.imshow(wordcloud)
plt.axis("off")
plt.savefig("your_file_name"+".png", bbox_inches='tight')
plt.show()
plt.close()

print(col.OKGREEN+"\nFrequency Distribution of top 20 words (2 Letter):\n"+col.ENDC)

cfdist = ConditionalFreqDist()

for word in RegexpTokenizer(r'\w+').tokenize(" ".join(reuters.words())):
    condition = len(word)
    cfdist[condition][word] += 1

for condition in cfdist:
    for word in cfdist[condition]:
        if(condition > 1 and condition < 5):
            print(word, cfdist[condition].freq(
                word), "  ", condition, " letters")
