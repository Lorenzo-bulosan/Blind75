import sys
sys.path.insert(0, 'c:/Projects/blind75/')
from Node import Node
from TreeUtils import TreeGen

def tree_sum(head: Node) -> int:

    if head is None: return 0

    leftSum = tree_sum(head.left)
    rightSum = tree_sum(head.right)
    return 1 + leftSum + rightSum

def test_tree_sum():

    gen = TreeGen()
    expected = 7
    head = gen.balanced_tree_identity()

    assert expected == tree_sum(head)

if __name__ == '__main__':
    test_tree_sum()

    