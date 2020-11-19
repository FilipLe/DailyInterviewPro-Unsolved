class Solution:
    def addDigits(self, num):
        #Make num into string because you can only iterate through string
        n = str(num)
        
        #Create boolean for the loop
        isOneDigit = False
        
        #Initialize result
        result = 0
        
        #Loop to make sure final result is one digit
        while isOneDigit == False: 
            
            #Loop to add the digits together
            for i in n:
                result += int(i)
            
            #Create string to store that result
            n = str(result)
            
            #If final result is one digit, exit loop
            if result < 10:
                isOneDigit = True
                break
                
            #Initialize integer result again
            result = 0
        return result
    
print(Solution().addDigits(38))
#Output 2

#The process is like: 3 + 8 = 11, 1 + 1 = 2. 
#Since 2 has only one digit, return it.
