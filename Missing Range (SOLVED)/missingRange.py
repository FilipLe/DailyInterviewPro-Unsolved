def missing_ranges(nums, low, high):
    result = []
    index1 = 0
    index2 = 1
    
    while index2 < len(nums):
        # lower <= nums[i]
        if nums[0] > low:
            result.append((low, nums[0]-1))
        
        # nums[i] <= upper
        elif nums[-1] > high and index2 == len(nums) - 1:
            result.append((nums[-1]+1, high))
        
        # remaining cases
        else:
            result.append((nums[index1]+1, nums[index2]-1))
        
        index1 += 1
        index2 += 1
    
    return result
  
print(missing_ranges([1, 3, 5, 10], 1, 10))
# [(2, 2), (4, 4), (6, 9)]
