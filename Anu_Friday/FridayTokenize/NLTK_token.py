from nltk.tokenize import TreebankWordTokenizer

print("ARABIC\n")
arabic = open("FridayTokenize/arabic.txt", "r", encoding="utf-8").read()
print("Data: ", arabic, "\n\nTokenized: ",
      TreebankWordTokenizer().tokenize(arabic))


print("\nJAPANESE\n")
arabic = open("FridayTokenize/japanese.txt", "r", encoding="utf-8").read()
print("Data: ", arabic, "\n\nTokenized: ",
      TreebankWordTokenizer().tokenize(arabic))


print("\nCHINESE\n")
arabic = open("FridayTokenize/chinese.txt", "r", encoding="utf-8").read()
print("Data: ", arabic, "\n\nTokenized: ",
      TreebankWordTokenizer().tokenize(arabic))
