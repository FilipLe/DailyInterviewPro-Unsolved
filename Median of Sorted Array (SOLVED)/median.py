class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #Create counter to iterate through 2nd array
        count = 0
        
        #Iterate through 2nd array to append the elements into 1st array
        while count < len(nums2):
            nums1.append(nums2[count])
            count += 1
        
        #Sort this new array in ascending order
        nums1.sort()
        
        #Variable to store length of the array
        len1 = len(nums1)
        
        #If the element size is not divisble by 2, median = middle num
        if len1%2==1:
            return float(nums1[int((len1-1)/2)])
        
        #If the element size is divisble by 2, median = average of 1st middle and 2nd middle num
        else:
            numerator = nums1[int((len1-2)/2)]+nums1[int((len1-2)/2+1)]
            result = int(numerator)/2
            return float(result)
