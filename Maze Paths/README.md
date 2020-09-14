This problem was recently asked by Microsoft:
<br><br>
A maze is a matrix where each cell can either be a <b>0</b> or <b>1</b>. A <b>0</b> represents that the cell is empty, and a <b>1</b> represents a wall that cannot be walked through. You can also only travel either right or down.
<br><br>
Given a <b>n</b>x<b>m</b> matrix, find the number of ways someone can go from the top left corner to the bottom right corner. You can assume the two corners will always be <b>0</b>.

<br><br>
<b>Example:
<br>Input:</b> [[0, 1, 0], [0, 0, 1], [0, 0, 0]]
<br><b># 0 1 0
# 0 0 1
# 0 0 0</b>
<br><b>Output:</b> 2
The two paths that can only be taken in the above example are: <b>down -> right -> down -> right, and down -> down -> right -> right</b>.
