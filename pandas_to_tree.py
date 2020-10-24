import spacy
import pandas as pd
from tree import Tree

def pandas_to_tree(dataframe):
    tree = Tree('Milling machine')
    troubles = dataframe['Trouble'].unique()
    for i in range(len(troubles)):
        analysis = dataframe.loc[dataframe['Trouble'] == troubles[i]]['Analysis'].values
        tree.branches.append(Tree(troubles[i]))
        for j in range(len(analysis)):
            solutions = dataframe.loc[dataframe['Analysis'] == analysis[j]]['Solution'].values
            tree.branches[i].branches.append(Tree(analysis[j]))
    return tree



dataframe = pd.read_csv('milling_machine.csv')
#print(dataframe.head())
tree = pandas_to_tree(dataframe)
#print(dataframe.loc[dataframe['Trouble'] == 'No power Input'])
#print(tree)