# main function -  checks if it's possible to create palindrome by removine a char
def create_palindrome(s):
    count = 0
    # iterate through every char of the string
    while count < len(s):
        # if the string after removing curr char is palindrome, it works
        
        #checking first char
        if count == 0:
            copy = s[count+1:]
            if checkPalindrome(copy) == True:
                return True
            
        #checking last char
        elif count == len(s) - 1:
            copy = s[:count]
            if checkPalindrome(copy) == True:
                return True
            
        #checking char in the middle
        else:
            copy = s[:count] + s[count+1:]
            if checkPalindrome(copy) == True:
                return True

        count += 1    
    return False

# helper (recursive) function to check if the string is a Palindrome
def checkPalindrome(s):
    # base case 
    if s == '' or len(s) == 1:
        return True
    
    # recursive case
    else:
        #call function recursively on input string without 1st and last char
        checkRest = checkPalindrome(s[1:-1])
        if s[0] == s[-1]:
            return True and checkRest
        else:
            return False and checkRest
    

print(create_palindrome("abcdcbea"))
# True
print(create_palindrome("abccba"))
# False
print(create_palindrome("abccaa"))
# False
