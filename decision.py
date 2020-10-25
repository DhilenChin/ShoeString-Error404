from pandas_to_tree import pandas_to_tree
from tree import Tree
import pandas as pd
from keywords import keywords

def best_branch(tree, text_in):
    """A function that returns the branch of TREE that has the most matching keywords with TEXT_IN"""
    keys_in = keywords(text_in)
    #print(keys_in)
    best_intersect = 0
    best_branch = Tree('No matching issues found')
    for branch in tree.branches:
        intersect = len(list(set(keys_in).intersection(set(branch.keywords))))
        #print(branch.keywords)
        if best_intersect < intersect:
            best_intersect = intersect
            best_branch = branch

    return best_branch

def best_branches(tree, text_in):
    """A function that returns the branches of TREE in order of matching the keywords of TEXT_IN"""
    keys_in = keywords(text_in)
    s = lambda x: len(list(set(keys_in).intersection(set(x.keywords))))
    branches = tree.branches[:]
    branches.sort(reverse = True, key = s)
    return branches


def best_children(node, text_in):
    """A function that returns a list of the children of NODE sorted by how much their keywords match TEXT_IN"""
    keys_in = keywords(text_in)
    s = lambda x: len(list(set(keys_in).intersection(set(x.keywords))))
    childs = node.children[:]
    childs.sort(key = s)
    return childs



##edited for ranking branches. might discard - C
# def best_branch(tree, text_in):
#     """A function that returns the branch of TREE that has the most matching keywords with TEXT_IN"""
#     keys_in = keywords(text_in)
#     #print(keys_in)
#     best_intersect = 0
#     branches_order = [] 
#     best_branch = Tree('No matching issues found')
#     for branch in tree.branches:
#         intersect = len(list(set(keys_in).intersection(set(branch.keywords))))
#         #print(branch.keywords)
#         if best_intersect < intersect:
#             best_intersect = intersect
#             best_branch = branch
#             branches_order.append(best_branch)

#     return best_branch, branches_order
"""
dataframe = pd.read_csv('edm_milling.csv')

tree = pandas_to_tree(dataframe)

text_in = input('Keywords')
print(best_branch(tree, text_in).label)
"""