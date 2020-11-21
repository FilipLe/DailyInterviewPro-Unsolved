class Solution:
    def findMin(self, nums):
        #sort array in ascending order
        nums.sort()
        
        #return firts element in sorted array
        return nums[0]
    
print(Solution().findMin([1,3,5]))
#Output 1

print(Solution().findMin([2,2,2,0,1]))
#Output 0
