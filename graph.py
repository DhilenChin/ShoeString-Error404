from keywords import keywords
from decision import best_children, best_branches
from pandas_to_tree import pandas_to_tree
from flow import high_scores
import pandas as pd
from chatbot import EchoBot, recieveMessage, sendMessage
from RLchatbot import giving_points
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

#initialise
milling_df = pd.read_csv('milling_machine.csv')
milling_tree = pandas_to_tree(milling_df)
#global edm_tree 
#edm_tree = pandas_to_tree(pd.read_csv('edm_milling.csv'))
client = EchoBot("boxwithabutton@gmail.com", "FUCKBotpress")
message = ""
threadId = ""
threadType = ""
start = Node('Hello. What machine can I help you with today?', keywords = ['start', 'reset'])


def millf(): 
    tree = milling_tree
    text = recieveMessage()
    if 'reset' in text.split():
        reset()
        return
    analyses = best_branches(tree, text)
    for i in range(len(analyses)):
        branch = analyses[i]
        solutions = high_scores(branch)
        sendMessage('Your problem could be: ' + branch.label)
        for i in range(len(solutions)):
            sol = solutions[i]
            sendMessage(str(sol.score))
            sendMessage(sol.label)
            sendMessage(sol.branches[0].label)
            sendMessage('Did that work? (yes/no)')
            response = recieveMessage().lower()
            if 'reset' in response.split():
                reset()
                return
            if 'yes' in response.split():
                reset()
                branch.score += 1
                for b in branch.branches:
                    b.score += 1
                return

def reset():
    sendMessage('Resetting the conversation')
    nodes_to_visit = [start]
    tree = None
    sendMessage('Glad I could help!')
    sendMessage('Hello. What machine can I help you with today?')
    


cnc = Node("I don't have any data for a cnc machine", keywords = ['cnc'], f = reset)
edm = Node("I don't have any data for a cnc machine", keywords = ['edm'], f = reset)
mill = Node('MILLING: Can you describe your issue?', keywords = ['milling', 'mill'], f = millf)
start.add_child([cnc,edm, mill])

global nodes_to_visit 
nodes_to_visit = []
nodes_to_visit.append(start)
recieveMessage()
print('Ready')

global tree

while True:
    if len(nodes_to_visit) == 0:
        nodes_to_visit.append(start) 
        cur_node = start    
    else:
        cur_node = nodes_to_visit.pop()
    sendMessage(cur_node.label)
    cur_node.func()
    text_in = recieveMessage()
    if 'reset' in text_in.split():
        reset()
        continue
    nodes_to_visit.extend(best_children(cur_node,text_in))


