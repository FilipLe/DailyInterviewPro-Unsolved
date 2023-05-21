# Arithmetic Binary Tree
This problem was recently asked by Apple:
<br>
<br>
You are given a binary tree representation of an arithmetic expression. In this tree, each leaf is an integer value,, and a non-leaf node is one of the four operations: '+', '-', '*', or '/'.
<br>
<br>
Write a function that takes this tree and evaluates the expression.
<br>
<br>
Example:
<img src="https://media.geeksforgeeks.org/wp-content/uploads/expression-tree.png">
<br>
<br>
This is a representation of the expression ((5 + 9) * 2) + 3, and should return 31.
<br><br>
Starter Code:
```
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
```
