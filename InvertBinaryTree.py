from TreeUtils import TreeGen
import Node

def reverse_binary_tree(head: Node) -> Node:

    if head is None: return

    if head.left is None and head.right is None: return

    tmp = head.left
    head.left = head.right
    head.right = tmp 
    
    reverse_binary_tree(head.left)
    reverse_binary_tree(head.right)
    return head
     

def test_reverse_binary_tree() -> None:
    
    gen = TreeGen()
    head = gen.generate_random_binary_tree(5)
    originalTree = gen.display_tree_in_order(head)
    expectedTree = originalTree[::-1]
    print(f'Original tree: {originalTree}')
    print(f'Expected tree: {expectedTree}')

    actualTree = gen.display_tree_in_order(reverse_binary_tree(head))
    print(f'Actual tree: {actualTree}')

    assert expectedTree == actualTree

test_reverse_binary_tree()