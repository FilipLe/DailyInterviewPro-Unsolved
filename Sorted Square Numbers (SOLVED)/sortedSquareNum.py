def square_numbers(nums):
    # Fill this in.
    count = 0
    new_arr = []
    while count < len(nums):
        new_arr.append(nums[count]**2)
        count+=1
    new_arr.sort()
    return new_arr

print(square_numbers([-5, -3, -1, 0, 1, 4, 5]))
# [0, 1, 1, 9, 16, 25, 25]
