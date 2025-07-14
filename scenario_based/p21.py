class TreeNode:
    def __init__(self, x):
        self.x = x
        self.left = None
        self.right = None

def build_tree(edges):
    nodes = {}
    root = None
    for u, v, c in edges:
        if u not in nodes:
            nodes[u] = TreeNode(u)
        if v not in nodes:
            nodes[v] = TreeNode(v)
        if root is None:
            root = nodes[u]
        if c == 'L':
            nodes[u].left = nodes[v]
        else:
            nodes[u].right = nodes[v]
    return root

def is_mirror(tree1, tree2):
    if tree1 is None and tree2 is None:
        return True
    if tree1 is None or tree2 is None:
        return False
    return (
        tree1.x == tree2.x and
        is_mirror(tree1.left, tree2.right) and
        is_mirror(tree1.right, tree2.left)
    )


n = 4  # Number of edges per tree

# Tree 1 edges: u, v, direction (L or R)
tree1_edges = [
    (1, 2, 'L'),
    (1, 3, 'R'),
    (2, 4, 'L')
]

# Tree 2 edges (mirror of Tree 1)
tree2_edges = [
    (1, 3, 'L'),
    (1, 2, 'R'),
    (2, 4, 'R')
]

root1 = build_tree(tree1_edges)
root2 = build_tree(tree2_edges)

print("yes" if is_mirror(root1, root2) else "no")