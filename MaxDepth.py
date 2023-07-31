from Node import Node
from collections import deque

def max_depth_tree_recursive(node: Node) -> int:

    if node is None: return 0

    return 1 + max(max_depth_tree_recursive(node.left), max_depth_tree_recursive(node.right))

def max_depth_tree(node: Node) -> int:

    max_depth = 0

    if node is None: 
        return max_depth

    q =  deque()
    q.append([node,1])

    while len(q) > 0:

        n, count = q.popleft()
        max_depth = max(count, max_depth) # check current count vs max as binary tree can be imbalanced, avoids extra space of keeping track of highest count with list

        if n.left is not None:
            q.append([n.left, count+1])
        
        if n.right is not None:
            q.append([n.right, count+1])

    return max_depth

def test_max_depth_tree():
    
    expected = 3
    head = Node(1)
    head.left = Node(1)
    head.right = Node(1)
    head.left.left = Node(1)
    head.left.right = Node(1)
    head.right.left = Node(1)
    head.right.right = Node(1)

    actual = max_depth_tree(head)
    print(f"expected vs actual {[expected, actual]}")

    assert expected == actual

def test_max_depth_tree_recursive():
    
    head = Node(1)
    head.left = Node(1)
    head.left.left = Node(1)
    head.left.left.left = Node(1)
    head.left.left.left.left = Node(1)

    assert 5 == max_depth_tree_recursive(head)

def test_max_depth_tree_recursive_no_tree():
    
    head = None

    assert 0 == max_depth_tree_recursive(head)

test_max_depth_tree()
test_max_depth_tree_recursive()
test_max_depth_tree_recursive_no_tree()