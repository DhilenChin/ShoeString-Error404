import pandas as pd
from keywords import keywords

text = input("What machine are you having problems with?")

keys = keywords(text)

milling = pd.read_csv('milling_machine.csv')
edm = pd.read_csv('edm_milling.csv')
print(milling.head())
print(edm.head())


'''
#simple keyword test
print(keywords)
if 'cnc' in keys:
    print("You are having problems with a CNC milling machine")
elif 'edm' in keys:
    print('You are having problems with an electrical discharge milling machine')
elif 'sandvik' in keys:
    print('You are having problems with a sandvik milling machine')
elif 'milling' in keys:
    print("You are having problems with a milling machine")
else:
    print("I'm sorry, I don't know that machine")
'''