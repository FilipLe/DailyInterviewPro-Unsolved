def first_recurring_char(s):
    # Fill this in.
    outerCount = 0
    innerCount = 1
    resetInnerCount = 1
    
    # loop through every char of str
    while outerCount < len(s):
        # set inner loop counter
        innerCount = resetInnerCount
        
        # loop through remaining char of str (everything sliced from curr char)
        while innerCount < len(s):
            # if curr char is found again at remaining of str
            if s[outerCount] == s[innerCount]:
                # return str, which breaks the loop
                return s[outerCount]    
            innerCount += 1
        
        # if inner loop passed with no return --> curr char was not found in remainder of str
        # reset inner loop to check next curr char
        resetInnerCount += 1
        
        outerCount += 1
    
    return None
    
print(first_recurring_char('qwertty'))
# t

print(first_recurring_char('qwerty'))
# None
