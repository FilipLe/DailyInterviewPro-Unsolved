class Solution: 
    def getRange(self, arr, target):
    # Fill this in.
        #Array to store the indices of target number
        indexArr = []
        count = 0
        #Loop to store the indices of target number
        while count < len(arr):
            #If num at this position is the same as the target number, store it in indexArr
            if arr[count] == target:
                indexArr.append(count)
            count += 1
        
        #If array is empty --> target not found --> return -1
        if not indexArr:
            return [-1,-1]
        
        #If array is not empty --> target number exists
        if indexArr:
            #Array to store the range
            rangeArr = []
            #Store the first element from the index array (start of range)
            rangeArr.append(indexArr[0])
            #Store the last element from the index array (end of range)
            rangeArr.append(indexArr[len(indexArr)-1])
            return rangeArr

  
# Test program 1
arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8] 
x = 2
print(Solution().getRange(arr, x))
# [1, 4]

# Test program 2
arr = [1,2,3,4,5,6,10] 
x = 9
print(Solution().getRange(arr, x))
# [-1, -1]
