romanValues = {
    "I":1,
    "V":5,
    "X":10,
    "L":50,
    "C":100,
    "D":500, 
    "M":1000 
}

pre_romanValues = {
    "IV":4,
    "IX":9,
    "XL":40,
    "XC":90,
    "CD":400,
    "CM":900,
}

# recursive function goes through each char of string, if current char is placed before ..., minus ..., otherwise, keep adding the char
def romanToInt(s):
    # base case 1 - the string is a singular roman numeral key
    if s in romanValues:
        return romanValues[s]
    
    # base case 2 - the string has a another numeral placed before
    elif s in pre_romanValues:
        return pre_romanValues[s]
    
    # recursive case - longer strings
    else:
        # case for prefixed numerals
        if s[:2] in pre_romanValues:
            romanToInt_Rest = romanToInt(s[2:])
            return pre_romanValues[s[:2]] + romanToInt_Rest
        
        # the remaining cases
        else:
            romanToInt_Rest = romanToInt(s[1:])
            return romanValues[s[0]] + romanToInt_Rest

n1 = 'MCMIV'
# 1904

n2 = 'MCMX'
# 1910

print(romanToInt(n1))
print(romanToInt(n2))
