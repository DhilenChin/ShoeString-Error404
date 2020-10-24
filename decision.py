from pandas_to_tree import pandas_to_tree
import pandas as pd
from keywords import keywords

def best_branch(tree, text_in):
    """A function that returns the branch of TREE that has the most matching keywords with TEXT_IN"""
    keys_in = keywords(text_in)
    print(keys_in)
    best_intersect = 0

    for branch in tree.branches:
        intersect = len(list(set(keys_in).intersection(set(branch.keywords))))
        print(branch.keywords)
        if best_intersect < intersect:
            best_intersect = intersect
            best_branch = branch

    return best_branch


'''
dataframe = pd.read_csv('milling_machine.csv')

tree = pandas_to_tree(dataframe)

text_in = input('Keywords')
print(best_branch(tree, text_in).label)
'''