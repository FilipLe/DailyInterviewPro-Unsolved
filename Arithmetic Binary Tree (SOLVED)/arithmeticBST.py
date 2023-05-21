class Node:
    # constructor method
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

PLUS = "+"
MINUS = "-"
TIMES = "*"
DIVIDE = "/"

def evaluate(root):
    # if current node is an operator
    if root.val == PLUS:
        return evaluate(root.left) + evaluate(root.right)
    
    elif root.val == MINUS:
        return evaluate(root.left) - evaluate(root.right)
    
    elif root.val == TIMES: 
        return evaluate(root.left) * evaluate(root.right)
    
    elif root.val == DIVIDE:
        return evaluate(root.left) / evaluate(root.right)
    
    # if current node is a number
    else:
        return root.val

tree = Node(PLUS)
tree.left = Node(3)
tree.right = Node(TIMES)
tree.right.left = Node(PLUS)
tree.right.left.left = Node(5)
tree.right.left.right = Node(9)
tree.right.right = Node(2)
print(evaluate(tree))
# 31