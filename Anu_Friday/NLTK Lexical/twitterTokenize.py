import nltk
from nltk.tokenize import TweetTokenizer

text = 'Someone was using a fake email to impersonate me to get free stuff from companies. This is his response.“I googled ways to get free stuff and this popped up”Might want to google “fraud” and “infringing identity” next!'
twtkn = TweetTokenizer()
print(twtkn.tokenize(text))
