from nltk.tokenize import TreebankWordTokenizer

print("ARABIC\n")
arabic = open("arabic.txt", "r", encoding="utf-8").read()
print("Data: ", arabic, "\n\nTokenized: ",
      TreebankWordTokenizer().tokenize(arabic))


print("Japanese\n")
arabic = open("japanese.txt", "r", encoding="utf-8").read()
print("Data: ", arabic, "\n\nTokenized: ",
      TreebankWordTokenizer().tokenize(arabic))


print("Chinese\n")
arabic = open("chinese.txt", "r", encoding="utf-8").read()
print("Data: ", arabic, "\n\nTokenized: ",
      TreebankWordTokenizer().tokenize(arabic))
