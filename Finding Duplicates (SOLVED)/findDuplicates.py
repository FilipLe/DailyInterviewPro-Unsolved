class Solution(object):
    def findDuplicates(self, nums):
    # Fill this in.
    
        #Array to store duplicates
        duplicates = []
        #Array storing elements, with duplicates elements removed
        duplicates_removed = []
        
        #Main Loop
        #Iterate through all the elements in input array
        for i in nums:
            #duplicates_removed = List storing elements without duplicates
            #If it is not in duplicates_removed 
            # --> it is not a duplicate
            # --> add it to duplicates_removed
            if i not in duplicates_removed:
                duplicates_removed.append(i)
                
            #If it is already there and we see it again in this iteration
            # ---> it is a duplicate as we've already encountered it
            # ---> add it to list of duplicates
            else:
                duplicates.append(i)
        
        return duplicates

print(Solution().findDuplicates([4,3,2,7,8,2,3,1]))
# [2, 3]
