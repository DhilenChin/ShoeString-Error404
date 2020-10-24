import spacy
import pandas as pd

nlp = spacy.load("en")
text = input("What machine are you having problems with?")
doc = nlp(text.lower())

keywords = []
for token in doc:
    #print(token.text, token.pos_, token.dep_, token.head.text)
    if token.pos_ == 'NOUN' or token.pos_ == 'VERB' or token.pos_ == 'ADJ' or token.pos_ == "PROPN":
        keywords.append(token.text)

milling = pd.read_csv('milling_machine.csv')
edm = pd.read_csv('edm_milling.csv')
print(milling.head())
print(edm.head())

"""
#simple keyword test
print(keywords)
if 'cnc' in keywords:
    print("You are having problems with a CNC milling machine")
elif 'edm' in keywords:
    print('You are having problems with an electrical discharge milling machine')
elif 'sandvik' in keywords:
    print('You are having problems with a sandvik milling machine')
elif 'milling' in keywords:
    print("You are having problems with a milling machine")
else:
    print("I'm sorry, I don't know that machine")
    """