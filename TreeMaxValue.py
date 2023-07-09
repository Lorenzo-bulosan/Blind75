from Node import Node
from TreeUtils import TreeGen

def tree_max_value(node: Node) -> int:

    if node is None: return 0
    
    leftMax = tree_max_value(node.left)
    rightMax = tree_max_value(node.right)

    return max(node.val, leftMax, rightMax)

def test_tree_max_value():

    gen = TreeGen()
    tree = gen.generate_random_binary_tree(7)
    treeVals = gen.display_tree_in_order(tree)
    expected = max(treeVals)

    assert expected == tree_max_value(tree)

if __name__ == '__main__':
    test_tree_max_value()