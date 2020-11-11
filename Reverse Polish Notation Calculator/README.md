This problem was recently asked by Facebook:
<br><br>
Given an expression (as a list) in reverse polish notation, evaluate the expression. Reverse polish notation is where the numbers come before the operand. Note that there can be the 4 operands '+', '-', '*', '/'. You can also assume the expression will be well formed.
<br><br>
<b>Example</b><br>
<i>Input: [1, 2, 3, '+', 2, '*', '-']<br>
Output: -9</i>
<br><br>
The equivalent expression of the above reverse polish notation would be (1 - ((2 + 3) * 2)).
<br><br> Starter Code:
```
def reverse_polish_notation(expr):
  # Fill this in.
  
# 1 - (2 + 3) * 2
print(reverse_polish_notation([1, 2, 3, '+', 2, '*', '-']))
# -9
```
