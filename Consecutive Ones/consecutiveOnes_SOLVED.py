#main function
def longest_run(n):
    #store the binary input as a list of strings so that you can iterate through later
    char = []
    #convert input into binary
    binary = convert_to_binary(n)
    #initializecount
    count = 0 
    #initializemax
    countMax = 0
    for digits in binary:
        char += digits
    for i in range(0,len(char)):
        #reset count if 0 is found
        if char[i]=='0':
            count = 0
        # If 1 is found, increment count and update countMax if count becomes bigger. 
        else:
            count += 1
            countMax = max(count,countMax)
    return countMax

#Convert input into binary function
def convert_to_binary(n):
    binary = ""
    while n > 0:
        remainder=n%2
        n=(n-remainder)/2
        if remainder == 0:
            binary = "0" + binary            
        elif remainder == 1:
            binary = "1" + binary
    return binary

print(longest_run(242))
# 4
