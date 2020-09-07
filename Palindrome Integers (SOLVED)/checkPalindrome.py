import math

def is_palindrome(n):
    # Fill this in.
    #Convert num into string
    stringVal = str(n)
    #Store the digits in a list
    arr = []
    #Loop through the digits and append them into the list arr[]
    for digits in stringVal:
        arr.append(digits)
    #Number of the digits
    sizeVal = len(arr)
    #initialize counter
    counter = 0
    #since we're working with palindromes supposingly, we only 
    #need to loop through the first half and check if they 
    #correspond to the last half
    #E.g. if it's a number consisting of 7 digits:
        # check if digit[0]=digit[6], digit[1]=digit[5],... and so on
    while counter < math.floor(sizeVal/2):
        if arr[counter] != arr[sizeVal-1-counter]:
            return False 
        else:
            return True   
print(is_palindrome(1234321))
# True
print(is_palindrome(1234322))
# False
print(is_palindrome(1221))
# False
