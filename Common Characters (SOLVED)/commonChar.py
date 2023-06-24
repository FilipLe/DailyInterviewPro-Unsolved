def common_characters(strs):
    # Fill this in.
    result = []
    
    # loop through every char in first string
    for i in strs[0]:
        
        # check the remaining strings
        count = 1
        while count < len(strs):
            
            # if one of the 1st string characters not in one of the remaining strings
            # break loop and stop checking
            if i not in strs[count]:
                break
            count += 1            
        
        # if we went through every remaining string, current char is duplicate in remaining strings 
        if count == len(strs):
            result.append(i)

    # set to remove duplicates
    result = list(set(result))
    return result

print(common_characters(['google', 'facebook', 'youtube']))
# ['e', 'o']

print(common_characters(['apple', 'andy', 'father']))
# ['a']


























'''def common_characters(strs):
    # Fill this in.
    amount = len(strs)
    arr = []
    count = 0
    while count < amount:
        temp = []
        for i in strs[count]:
            temp.append(i)
        arr.append(set(temp))
        count += 1
        
    count = 0
    while count < amount-1:
        z = arr[count].intersection(arr[count+1])
        count += 1
    return arr

print(common_characters(['google', 'facebook', 'youtube']))
# ['e', 'o']

#print(common_characters(['apple', 'andy', 'father']))
# ['a']'''

'''
    #array to store the common characters
    commonChar = []
    
    #amount of words
    amount = len(strs)
    
    #iterate through letters in 1st string

    #we will start from second word
    count = 1
    while count < amount:
        for i in strs[0]:
            if i in strs[count]:
                commonChar.append(i)
        count += 1
    return list(set(commonChar))
    '''
