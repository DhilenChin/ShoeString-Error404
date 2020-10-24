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




