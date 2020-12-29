class Solution:
    def reverse(self, x):
        #Var to determine whether number is positive or negative
        negative = False
        #If number is positive
        if x > 0:
            #convert to string
            strVers = str(x)
            #reverse the string
            reverseStr = strVers[::-1]

        #If number is negative
        else:
            #Absolute value it ==> Make it positive
            x = abs(x)
            #Convert to string
            strVers = str(x)
            #Reverse string
            reverseStr = strVers[::-1]
            #Make 'negative' True to indicate that this number is negative for later
            negative = True

        #if the reversed value starts with 0, get rid of 0
        if reverseStr[0] == 0:
            reverseStr = reverseStr[1:]  

        
        result = int(reverseStr)
        #Checking if resulting number fits signed integer range
        #If it does not fit in the range, return 0
        if result < -2**31 or result > 2**31-1:
            return 0
        else:
            #if number is positive, just return the reversed value
            if negative == False:
                return result
            #if number is negative, multiply by -1 to add the (-) sign in front
            else:
                return result*-1
        
print(Solution().reverse(123))
#321

print(Solution().reverse(-123))
#-321

print(Solution().reverse(120))
#21

print(Solution().reverse(1534236469))
#0
