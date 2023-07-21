def larger_number(nums):
    indices = []
    currIndex = 0
    
    while currIndex < len(nums):
        innerCount = currIndex
        statusBig = False
        
        while innerCount < len(nums):
            # if bigger num found in inner loop, store that index and end inner loop
            if nums[innerCount] > nums[currIndex]:
                indices.append(innerCount)
                statusBig = True
                innerCount = len(nums)
            
            innerCount += 1
        
        # if status still false, outer loop did not find smaller inner loop, store -1
        if statusBig == False:
            indices.append(-1)
        
        currIndex += 1
    
    return indices

  
# print [2, 2, 3, 4, -1, -1]
print(larger_number([3, 2, 5, 6, 9, 8]))
