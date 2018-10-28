from nltk.corpus import cmudict

entries = cmudict.entries()
print("Length of entries:",len(entries),"\n")
for entry in entries[1000:1025]:
    print("CMU word list", entry)

