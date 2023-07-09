import sys
sys.path.insert(0, 'c:/Projects/blind75/')
from Node import Node
from TreeUtils import TreeGen
import random

def exist_in_tree(node: Node, val: int) -> bool:

    if node is None: return False

    existLeft = exist_in_tree(node.left, val)
    existRight = exist_in_tree(node.right, val)

    return val == node.val or existLeft or existRight

def test_exist_in_tree():

    gen = TreeGen()
    tree = gen.generate_random_binary_tree(9)    
    expected1 = gen.display_tree_in_order(tree)[random.randint(0,8)]
    expected2 = gen.display_tree_in_order(tree)[random.randint(0,8)]
    expected3 = gen.display_tree_in_order(tree)[random.randint(0,8)]

    print(f'Searching for {[expected1, expected2, expected3]} in generated tree: {gen.display_tree_in_order(tree)}')

    assert exist_in_tree(tree, expected1 )
    assert exist_in_tree(tree, expected2 )
    assert exist_in_tree(tree, expected3 )

def test_exist_in_tree_unsuccessful():

    gen = TreeGen()
    treeIdentity = gen.balanced_tree_identity()
    value = random.randint(2,100)

    assert exist_in_tree(treeIdentity, value) == False

if __name__ == '__main__':
    test_exist_in_tree()