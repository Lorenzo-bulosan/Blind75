import sys
sys.path.insert(0, 'c:/Projects/blind75/')
from collections import deque
import Node

class TreeTraversals:

    def dfs(self, node: Node, res: list) -> None:
        if node is not None:            
            self.dfs(node.left, res)
            res.append(node.val)
            self.dfs(node.right, res)

    def bfs(self, node: Node) -> Node:

        if node is None: return None

        q = deque()
        q.append(node)
        res = []

        while len(q) > 0:
            
            n = q.popleft()
            res.append(n.val)
            
            if n.left is not None:
                q.append(n.left)
                
            if n.right is not None:
                q.append(n.right)

        return res
    
