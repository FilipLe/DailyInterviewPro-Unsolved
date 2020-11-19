class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        #Initialize counter to iterate through 2nd array
        count = 0
        
        #Iterate 2nd array and append those elements into 1st arr
        while count < n:
            nums1.append(nums2[count])
            count += 1
        
        #Sort the list into ascending order
        nums1.sort()
        
        #Since list sorted, all 0's at the beginning
        #nums1 has enough space to hold extra elements from nums2
        
        #--> Amount of 0 at the beginning = n (size of nums2)
        counter = 0
        while counter < n:
            #Remove the 0's
            nums1.remove(0)
            counter += 1
        return nums1
    
print(Solution().merge([1,2,3,0,0,0],3,[2,5,6],3))
