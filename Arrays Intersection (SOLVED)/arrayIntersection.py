def intersection(nums1, nums2):
    # Fill this in.
    count1 = 0 
    #Array to store intersections
    arr = []
    #Loop to find intersections
    while count1 < len(nums1):
        count2 = 0
        while count2 < len(nums2):
            if nums1[count1]==nums2[count2]:
                arr.append(nums1[count1])
            count2 += 1
        count1 += 1
    arr = list(set(arr))#remove duplicate elements from list
    return arr
print(intersection([4, 9, 5], [9, 4, 9, 8, 4]))
print(intersection([1,2,2,1], [2,2]))
# [9, 4]
# [2]
