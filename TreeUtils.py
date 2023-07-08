import random
from Node import Node
from UsefulAlgorithms.TreeTraversals import TreeTraversals

class TreeGen:

    def generate_random_binary_tree(self, size):

        if size == 0:
            return None
    
        # Choose random sizes for left and right subtrees
        left_size = random.randint(0, size-1)
        right_size = size - 1 - left_size
    
        # Generate left and right subtrees recursively
        left_subtree = self.generate_random_binary_tree(left_size)
        right_subtree = self.generate_random_binary_tree(right_size)
    
        # Create new node with random value
        root = Node(random.randint(0, 100))
    
        # Assign left and right subtrees to children
        root.left = left_subtree
        root.right = right_subtree
    
        return root
    
    def display_tree_in_order(self, node: Node) -> list:

        output = []

        t = TreeTraversals()
        t.dfs(node, output)

        return output
    

 