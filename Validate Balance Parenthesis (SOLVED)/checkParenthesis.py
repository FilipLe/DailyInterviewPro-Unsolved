#Using stacks
#LIFO --> Last In First Out

class Solution:
    def isValid(self, s):
        #Fill this in.
        #Use stack data structure
        #LIFO --> Last In First Out
        
        #Array store the opening brackets
        parenthesis = []
        isValid = True
        for i in s:
            if i == '(' or i == '{' or i == '[':
                #if it's opening bracket, add it to the array
                parenthesis.append(i)
            else:
                #If it's closing bracket:
                #removes the last element stored in the array
                #To compare with the last opening bracket
                current = parenthesis.pop()
                
                #If opening brackets match with closing brackets --> true
                if current == '(' and  i == ')':
                    isValid = True
                elif current == '[' and i == ']':
                    isValid = True
                elif current == '{' and i == '}':
                    isValid = True
                
                #If opening brackets do not match with closing brackets --> false
                else:
                    isValid = False
        #Since opening brackets are removed when paired up with closing brackets
        #if there is an opening bracket left --> it was not paired up
        if isValid and not parenthesis:
            return True
        else:
            return False
        
# Test Program
s = "()(){(())" 
# should return False
print(Solution().isValid(s))

s = "([{}])()"
# should return True
print(Solution().isValid(s))
