from collections import deque

# Node class for the binary tree
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

# Function to build the tree from edge list
def build_tree(edges):
    nodes = {}
    root = None
    for u, v, c in edges:
        if u not in nodes:
            nodes[u] = Node(u)
        if v not in nodes:
            nodes[v] = Node(v)

        if root is None:
            root = nodes[u]

        if c == 'L':
            nodes[u].left = nodes[v]
        else:
            nodes[u].right = nodes[v]
    return root

# Function to do zigzag level order traversal
def zigzag_traversal(root):
    if not root:
        return []

    result = []
    current_level = deque()
