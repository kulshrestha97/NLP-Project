import nltk
import os
class NLPToken:
    def __init__(self,text):
        self.paragraph = text
        self.tokenize = nltk.tokenize.TreebankWordTokenizer().tokenize(paragraph)
    
    def returnTokens(self):
        with open('NLPTokenized.txt','w', encoding='utf8') as f:
            for token in self.tokenize:
                f.write(token)
                f.write('\n')
            f.close()
        print('Successfully Tokenized')
        print(self.tokenize)
            
             
with open('NLPFridayAssignment.txt','r',encoding='utf8') as f:
    paragraph = f.read()
    
    f.close()
NLPToken(paragraph).returnTokens()
    
    
#with open('NLPTokenized.txt','w') as f1:
#   f1.write(stringArray)
    