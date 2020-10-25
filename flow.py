def decision_logic(big_tree):
    branch = high_score(big_tree)
    return branch.label

def high_score(branch):
    children = branch.branches
    max_element = 0
    for i in range(len(children)):
        if children[i].score > children[max_element].score and not children[i].used:
            max_element = i
    return children[max_element]

#The below is edited code for returning solutions in rank order - C
def ordered_score(branch):
    children = branch.branches
    ordered_children = children
    
    N = len(children)
    for i in range(N - 1):
        if ordered_children[i] > ordered_children[i + 1]:
            ordered_children[i + 1], ordered_children[i] = ordered_children[i], ordered_children[i + 1]
        N = N - 1
    
    return ordered_children
