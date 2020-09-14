def find_fixed_point(nums):
    # Fill this in.
    counter = 0
    arr = [] #array to store the fixed points
    while counter < len(nums):
        #if index is equal to number at that index, store it in arr 
        if counter == nums[counter]:
            arr.append(counter)
        counter += 1
    if len(arr)==0:
        return None
    else:
        return arr
print('Fixed points:',find_fixed_point([-5, 1, 3, 4]))
# 1
