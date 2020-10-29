def findKthLargest(arr, k):
    # Fill this in.
    #Sort array in ascending order
    arr.sort()
    #Sorted array --> biggest num at the end
    #--> kth largest num --> move from end to the left k elements
    return arr[len(arr)-k]

print(findKthLargest([8, 7, 2, 3, 4, 1, 5, 6, 9, 0], 3))
# 7
