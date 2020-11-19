import math
class Solution:
    def mySqrt(self, x):
        #Instead of sqrt, we can use x^(1/2)
        result = x**(1/2)
        return math.floor(result)
    
print(Solution().mySqrt(4))
#Output 2

print(Solution().mySqrt(8))
#Output 2
#The square root of 8 is 2.82842..., and since the decimal part is truncated, 2 is returned.
