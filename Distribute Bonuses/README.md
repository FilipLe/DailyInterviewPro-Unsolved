# Distribute Bonuses
This problem was recently asked by Twitter:
<br>
<br>
You are the manager of a number of employees who all sit in a row. The CEO would like to give bonuses to all of your employees, but since the company did not perform so well this year the CEO would like to keep the bonuses to a minimum.
<br>
<br>
The rules of giving bonuses is that:
<br>
- Each employee begins with a bonus factor of 1x.
- For each employee, if they perform better than the person sitting next to them, the employee is given +1 higher bonus (and up to +2 if they perform better than both people to their sides).
<br>
<br>
Given a list of employee's performance, find the bonuses each employee should get.
<br>
<br>
Example:
<br>
Input: [1, 2, 3, 2, 3, 5, 1]
<br>
Output: [1, 2, 3, 1, 2, 3, 1]
