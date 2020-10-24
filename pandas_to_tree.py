import spacy
import pandas as pd
from tree import Tree

def pandas_to_tree(dataframe):
    tree = Tree('Milling machine')
    troubles = dataframe['Trouble'].unique()
    for trouble in troubles:
        #analysis = dataframe[trouble]
        #print(analysis)
        tree.branches.append(Tree(trouble))
        
    return tree



dataframe = pd.read_csv('edm_milling.csv')
print(dataframe.head())
#tree = pandas_to_tree(dataframe)
print(dataframe)
#print(tree)