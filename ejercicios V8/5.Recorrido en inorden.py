class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def inorder_traversal(root):
  if root:
    inorder_traversal(root.left)
    print(root.data)
    inorder_traversal(root.right)

root = Node(27)
root.left = Node(14)
root.right = Node(35)
root.left.left = Node(10)
root.left.right = Node(19)
root.right.left = Node(31)
root.right.right = Node(42)

inorder_traversal(root)