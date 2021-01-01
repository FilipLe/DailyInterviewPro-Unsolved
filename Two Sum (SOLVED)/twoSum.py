class Solution:
    def twoSum(self, nums, target):
        #count1 iterates through every element of array
        #count2 iterates through elements to the right of the current element at count1
        
        #array to store the resulting indices
        arr = []
        
        #counter to iterate through loop
        count1 = 0
        #counter to iterate starting from element to the right of the first element
        #starting from 2nd element
        #to avoid adding the exact same element
        count2 = count1 + 1
        
        #var to indicate when to end the while loop
        statusMet = False
        
        #main loop
        while count1 < len(nums) and statusMet == False:
            while count2 < len(nums):
                #if the two numbers add up to target integer and the indices are not the same
                if nums[count1] + nums[count2] == target and count1 != count2:
                    
                    #store the indices in the array
                    arr.append(count1)
                    arr.append(count2)
                    statusMet = True
                count2 += 1
            
            #reset count2
            count2 = count1 + 1
            count1 += 1
        return arr

#test case 1
arr1 = [2,7,11,15]
target1 = 9
print(Solution().twoSum(arr1,target1))
#[0,1]

#test case 2
arr2 = [3,2,4]
target2 = 6
print(Solution().twoSum(arr2,target2))
#[1,2]

#test case 3
arr3 = [3,3]
target3 = 6
print(Solution().twoSum(arr3,target3))
#[0,1]

#test case 4
arr4 = [2,5,5,11]
target4 = 10
print(Solution().twoSum(arr4,target4))
#[1,2]

