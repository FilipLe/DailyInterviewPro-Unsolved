import math
KAPREKAR_CONSTANT = 6174

def num_kaprekar_iterations(n):
    #Fill this in.
    large = 0
    small = 0
    counter = 0
    result = n
    #loop for the main function
    while result != KAPREKAR_CONSTANT:
        #get num in descending order
        large = getLarger(result)
        #get num in ascending order
        small = getSmaller(result)
        #Subtract the ascending number from the descending number.
        result = abs(large-small)
        #count number of iterations
        counter += 1
    return counter

#function to convert the number into an array of digits    
def convert_to_array(n):
    #convert input into a string
    number = str(n)
    #create an empty list to store the digits
    arr = []
    #iterate through the digits
    for digits in number:
        #add each digit into the array
        arr.append(digits)
    #return the array of digits
    return arr
    
#sort the number into a number with digits in descending order (decreasing from left to right) -->largest possible
def getLarger(n):
    #convert num into array of digits
    arr = convert_to_array(n)
    #function to sort the array into descending order
    arr.sort(reverse=True)
    count = 0
    numStr = ''
    #while loop to iterate through the sorted array of digits to put them into one string
    while count < len(arr):
        numStr += arr[count]
        count += 1
    #convert the string into integer with digits in descending order
    numStr = int(numStr)
    #return num with digits in descending order
    return numStr

#sort the number into a number with digits in ascending order (increasing from left to right) -->smallest possible
def getSmaller(n):
    #convert num into array of digits
    arr = convert_to_array(n)
    #function to sort the array into ascending order
    arr.sort()
    count = 0
    numStr = ''
    #while loop to iterate through the sorted array of digits to put them into one string
    while count < len(arr):
        numStr += arr[count]
        count +=1
    #convert the string into integer with digits in ascending order
    numStr = int(numStr)
    #return num with digits in ascending order
    return numStr

print(num_kaprekar_iterations(3524))
# 3
# Explanation:
#  5432 - 2345 = 3087
#  8730 - 0378 = 8352
#  8532 - 2358 = 6174 (3 iterations)
