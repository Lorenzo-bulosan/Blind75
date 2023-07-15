from TreeUtils import TreeGen
from collections import deque
import Node

def recursive_reverse_binary_tree(head: Node) -> Node:

    if head is None: return

    tmp = head.left
    head.left = head.right
    head.right = tmp 
    
    recursive_reverse_binary_tree(head.left)
    recursive_reverse_binary_tree(head.right)
    return head
     
def iterative_reverse_binary_tree(head: Node) -> Node:

    if head is None: return

    st = deque()
    st.append(head)

    while len(st) > 0:
        
        n = st.pop()

        if n is None: continue

        tmp = n.left
        n.left = n.right
        n.right = tmp 
        
        st.append(n.left)
        st.append(n.right)

    return head

def test_recursive_reverse_binary_tree() -> None:
    
    gen = TreeGen()
    head = gen.generate_random_binary_tree(5)
    originalTree = gen.display_tree_in_order(head)
    expectedTree = originalTree[::-1]
    print(f'Original tree: {originalTree}')
    print(f'Expected tree: {expectedTree}')

    actualTreeRecursive = gen.display_tree_in_order(recursive_reverse_binary_tree(head))
    print(f'Actual tree recursive: {actualTreeRecursive}')

    assert expectedTree == actualTreeRecursive

def test_iterative_reverse_binary_tree() -> None:
    
    gen = TreeGen()
    head = gen.generate_random_binary_tree(5)
    originalTree = gen.display_tree_in_order(head)
    expectedTree = originalTree[::-1]
    print(f'Original tree: {originalTree}')
    print(f'Expected tree: {expectedTree}')

    actualTreeIterative = gen.display_tree_in_order(iterative_reverse_binary_tree(head))
    print(f'Actual tree iterative: {actualTreeIterative}')

    assert expectedTree == actualTreeIterative

test_recursive_reverse_binary_tree()
test_iterative_reverse_binary_tree()