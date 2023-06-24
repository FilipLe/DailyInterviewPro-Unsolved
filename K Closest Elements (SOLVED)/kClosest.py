def closest_nums(nums, k, x):
    # Fill this in.
    
    # loop to find differences between every element of nums[] and pivot x
    differences = []
    for i in nums:
        differences.append(abs(x-i))
        
    # loop to find indices of k closest num to pivot x (smallest differences)
    count = 0
    index_closest = []
    while count < k:
        min_diff = differences[0]
        for i in range(len(differences)):
            if differences[i] < min_diff:
                index_closest.append(i)
                differences[i] = 100
        count += 1
    
    # loop for k closest num
    result = []
    for n in index_closest:
        result.append(nums[n])
    
    return result
 
print(closest_nums([1, 3, 7, 8, 9], 3, 5))
# [7, 3, 8]
