import math
#Examples step by step converting to Hex

#Example 1: 1365 to hex
#1365 ÷ 16 = 85 R 5 --> 5
# 85  ÷ 16 = 5 R 5 --> 5
#           5 --> 5
#--> Hex value: 555

#Example 2: 1237
#1237 ÷ 16 = 77 R 5 --> 5
# 77  ÷ 16 = 4 R 13 --> 13 = D --> D
#     4  --> 4
#-->Hex Value: 4D5

def to_hex(n):
    hexVal = ''
    remainder = 0 
    while n > 0:
        #When n=123, 123÷16=7R11 --> currentQuotient=7
        currentQuotient = math.floor(n/16)
        #current stores the product of currentQuotient and 16 (to later be subtracted to find remainder)
        current = currentQuotient*16
        #remainder = n - product of currentQuotient and 16 --> find remainder of n when divided by 16
        remainder = n - current
        #in Hexadecimal:
        #0-9 in decimal = 0-9 in hex
        #10-15 in dec = A-F in hex
        if remainder < 10:
            hexVal += str(remainder)
        else:
            if remainder == 10:
                hexVal += 'A'
            elif remainder == 11:
                hexVal += 'B'
            elif remainder == 12:
                hexVal += 'C'
            elif remainder == 13:
                hexVal += 'D'
            elif remainder == 14:
                hexVal += 'E'
            else:
                hexVal += 'F'
        n = currentQuotient
    #Reverse hexVal
    return hexVal[::-1]        
print(to_hex(123))
# 7B
#123÷16=7R11-->11=B
#7÷16=0R7
#7B