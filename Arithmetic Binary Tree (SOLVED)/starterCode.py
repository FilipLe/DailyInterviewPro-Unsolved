class Node:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

PLUS = "+"
MINUS = "-"
TIMES = "*"
DIVIDE = "/"

def evaluate(root):
  # Fill this in.

tree = Node(PLUS)
tree.left = Node(3)
tree.right = Node(TIMES)
tree.right.left = Node(PLUS)
tree.right.left.left = Node(5)
tree.right.left.right = Node(9)
tree.right.right = Node(2)
print evaluate(tree)
# 31
