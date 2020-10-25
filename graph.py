from keywords import keywords

class Node:

    def __init__(self, label, parents=[], children = [], keywords = []):
        if len(parents) != 0:
            assert all([isinstance(parent, Node) for parent in parents])
        if len(children) != 0:
            assert all([isinstance(child, Node) for child in children])

        self.label = label
        self.keywords = keywords
        self.children = children
        self.parents = parents

    def __str__(self): 
        return 'parents: ' + str(self.parents) + 'children' + str(self.children)
    def add_child(self, lst):
        for child in lst:
            self.children.append(child)
            child.parent.append(self)

q = 'Hello. What machine can I help you with today?'
start = Node(q, keywords = ['start', 'reset'])

q = 'I think the problem is:'
analysis = Node(q)

q = 'Can you describe your issue?'
cnc = Node(q, keywords = ['cnc'], parents = ['start'], children = [analysis])
edm = Node(q, keywords = ['edm'], children = [analysis])
mill = Node(q, keywords = ['milling'], children = [analysis])
start.add_child([cnc,edm])
