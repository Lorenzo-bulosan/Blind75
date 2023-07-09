from Node import Node
from collections import deque

def lowest_common_ancestor(head: Node, a: int, b: int) -> int:

    ancestorListA = get_path(head, a)
    ancestorListB = get_path(head, b)

    print([ancestorListA, ancestorListB])

    Found = False
    i = 0
    lowestCommonAncestor = None

    while Found == False:
        
        if ancestorListA[i] != ancestorListB[i]:
            lowestCommonAncestor = ancestorListA[i-1]
            Found = True
            break

        i += 1

    return lowestCommonAncestor

def get_path(node: Node, val: int) -> list:

    def dfs(node: Node, val: int, l: list) -> bool:

        if node is None: return False

        l.append(node.val)
        inLeft = dfs(node.left, val, l)
        inRight = dfs(node.right, val, l)

        if node.val == val or inLeft or inRight:
            return True
        
        l.pop()
        return False

    res = []
    dfs(node, val, res)

    return res
    
def test_lowest_common_ancestor():

    head = Node(4)
    head.left = Node(2)
    head.right = Node(6)
    head.left.left = Node(1)
    head.left.right = Node(3)
    head.right.left = Node(5)
    head.right.right = Node(7)

    assert 2 == lowest_common_ancestor(head, 1, 3)
    assert 4 == lowest_common_ancestor(head, 1, 7)
    assert 6 == lowest_common_ancestor(head, 5, 7)
    assert 4 == lowest_common_ancestor(head, 2, 7)

test_lowest_common_ancestor()