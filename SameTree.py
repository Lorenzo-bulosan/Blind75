from Node import Node
from TreeUtils import TreeGen

def is_same_tree(a: Node, b: Node) -> bool:

    if a is None and b is None: 
        return True
    
    if a is not None and b is not None:
        if a.val == b.val: 
            return True

    return False

def test_is_same_tree():

    t = TreeGen()
    firstTree = t.balanced_tree_identity()
    secondTree = t.balanced_tree_identity()

    assert is_same_tree(firstTree, secondTree)

def test_is_same_tree_correctly_identifies_different_trees():

    t = TreeGen()
    firstTree = t.balanced_tree_identity()
    secondTree = t.generate_random_binary_tree(6)

    assert is_same_tree(firstTree, secondTree) == False

if __name__ == '__main__':
    test_is_same_tree()
    test_is_same_tree_correctly_identifies_different_trees()