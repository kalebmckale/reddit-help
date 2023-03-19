"""
class Tree:
    def __init__(self, root_node, branch_nodes):
        branches = branches or []
        for branch in branches:
            if not isinstance(branch, Tree):
                raise ValueError("Branches must be trees.")
        self.tree = [root_label, branches or []]

    def from_iter()

    @property
    def label(self):
        return self.tree[0]        

    @property
    def branches(self):
        return self.tree[1:]
        
    @staticmethod
    def is_leaf(tree):
        return not tree.branches
        
    def right_binarize(self):
        if self.is_leaf(self):
            return self.tree
        if len(self.tree) > 2:
            self.tree = "        

"""

def tree(root_label, branches=None):
    branches = branches or []
    for branch in branches:
        assert is_tree(branch), "Branches must be trees."
    return [root_label] + branches

def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:] if isinstance(tree, list) else []

def is_tree(tree):
    if not isinstance(tree, list) or len(tree) == 0:
        return False
    # Makes sure each branch is also a tree.
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    return not branches(tree)

def right_binarize(tree):
    if is_leaf(tree):
        return tree
    if len(tree) > 1:
        tree = [tree[0], tree[1:]]
    return [right_binarize(b) for b in tree]


def main():
    return right_binarize([1, 2, 3, 4, 5, 6, 7])
#"""



