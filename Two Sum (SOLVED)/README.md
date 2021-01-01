# Two Sum

Given an array of integers ```nums``` and an integer ```target```, return <i>indices of the two numbers such that they add up to</i> ```target```.
<br><br>
You may assume that each input would have <b><i>exactly</i> one solution</b>, and you may not use the <i>same</i> element twice.
<br><br>
You can return the answer in any order.

 

Example 1:
```
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
```
Example 2:
```
Input: nums = [3,2,4], target = 6
Output: [1,2]
```
Example 3:
```
Input: nums = [3,3], target = 6
Output: [0,1]
``` 

<b>Constraints:</b>

• 2 <= nums.length <= 10<sup>3</sup> <br>
• -10<sup>9</sup> <= nums[i] <= 10<sup>9</sup> <br>
• -10<sup>9</sup> <= target <= 10<sup>9</sup> <br>
• <b>Only one valid answer exists.
