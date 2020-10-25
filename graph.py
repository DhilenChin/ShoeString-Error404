from keywords import keywords
from decision import best_children, best_branches
from pandas_to_tree import pandas_to_tree
from flow import high_score
import pandas as pd

class Node:

    def __init__(self, label, parents=[], children = [], keywords = [], f = lambda *args: None):
        if len(parents) != 0:
            assert all([isinstance(parent, Node) for parent in parents])
        if len(children) != 0:
            assert all([isinstance(child, Node) for child in children])

        self.label = label
        self.keywords = keywords
        self.children = children
        self.parents = parents
        self.func = f

    def __str__(self): 
        return self.label

    def add_child(self, lst):
        for child in lst:
            self.children.append(child)
            child.parents.append(self)

def init():
    global milling_tree
    milling_tree = pandas_to_tree(pd.read_csv('milling_machine.csv'))
    global edm_tree 
    edm_tree = pandas_to_tree(pd.read_csv('edm_milling.csv'))

init()


start = Node('Hello. What machine can I help you with today?', keywords = ['start', 'reset'])



def edmf(): 
    tree = edm_tree
    text = input()
    analyses = best_branches(tree, text)
    while len(analyses) > 0:
        branch = analyses.pop()
        print('Your problem could be: ', branch.label)
        print( high_score(branch).label)
        print('Did that work? (yes/no)')
        response = input()
        if 'yes' in response.split():
            break


def millf(): 
    tree = milling_tree
    text = input()
    analyses = best_branches(tree, text)
    while len(analyses) > 0:
        branch = analyses.pop()
        print('Your problem could be: ', branch.label)
        print('Try', high_score(branch).label)
        print('Did that work? (yes/no)')
        response = input()
        if 'yes' in response.split():
            break

cnc = Node("I don't have any data for a cnc machine", keywords = ['cnc'])
edm = Node('EDM: Can you describe your issue?', keywords = ['edm'], f = edmf)
mill = Node('MILLING: Can you describe your issue?', keywords = ['milling', 'mill'], f = millf)
start.add_child([cnc,edm, mill])

nodes_to_visit = []
nodes_to_visit.append(start)


global tree

while True:
    if len(nodes_to_visit) == 0:
        nodes_to_visit.append(start) 
        cur_node = start    
    else:
        cur_node = nodes_to_visit.pop()
    print(cur_node.label)
    cur_node.func()
    text_in = input()
    if 'reset' in text_in.split():
        print('Resetting the conversation')
        nodes_to_visit = [start]
        tree = None
        continue
    nodes_to_visit.extend(best_children(cur_node,text_in))


