class TreeNode:
    def __init__(self, x):
        self.x = x
        self.left = None
        self.right = None

def insert(root, data):
    if root is None:
        return TreeNode(data)
    if data < root.x:
        root.left = insert(root.left, data)
    else:
        root.right = insert(root.right, data)
    return root

def height(root):
    if root is None:
        return -1  # height is counted in edges
    return 1 + max(height(root.left), height(root.right))

values = [10, 5, 20, 3, 7, 30]  

root = None
for val in values:
    root = insert(root, val)

print("Height of the tree:", height(root))
