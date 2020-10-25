from pandas_to_tree import pandas_to_tree
import pandas as pd
from keywords import keywords
from decision import best_branch
from flow import high_score

milling = pandas_to_tree(pd.read_csv('milling_machine.csv'))
edm = pandas_to_tree(pd.read_csv('edm_milling.csv'))

text = input("What machine are you having problems with?")

keys = keywords(text)

if 'cnc' in keys:
    print("You are having problems with a CNC milling machine")
    print('No data available for CNC machine')
elif 'edm' in keys:
    print('You are having problems with an electrical discharge milling machine')
    data = edm
elif 'sandvik' in keys:
    print('You are having problems with a sandvik milling machine')
    print('No data available for sandvik machine')
elif 'milling' in keys:
    print("You are having problems with a milling machine")
    data = milling
else:
    print("I'm sorry, I don't know that machine")

text = input("What is your issue with the machine?")

branch = best_branch(data, text)
print('Your issue is', branch.label)
print('Try', high_score(branch).label)

# branches = ordered_score(branch)
# print('Try:')
# for b in branches:
#   print('{num}. '.format(b.index()) + b.label)

text = input('Did this solution work?')
