## Missing Range

This problem was recently asked by Google:
<br><br>
Given a sorted list of numbers, and two integers <b>low</b> and <b>high</b> representing the lower and upper bound of a range, return a list of (inclusive) ranges where the numbers are missing. 
<br>A range should be represented by a tuple in the format of <b>(lower, upper)</b>.

#### Constraints:
- ```- 109 <= lower <= upper <= 109```
- ```0 <= nums.length <= 100```
- ```lower <= nums[i] <= upper```
- All the values of nums are unique.

#### Starter Code
```python
def missing_ranges(nums, low, high):
  #Fill this in.
  
print(missing_ranges([1, 3, 5, 10], 1, 10))
# [(2, 2), (4, 4), (6, 9)]
```
