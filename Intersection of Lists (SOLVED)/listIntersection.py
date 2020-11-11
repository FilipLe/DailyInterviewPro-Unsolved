def intersection(list1, list2, list3):
    # Fill this in.
    #Array to store intersections
    arr = []
    #Iterate through all the elements in list1
    for i in list1:
        #Logic Gate AND 
        #-->Both conditions have to be met in order to execute
        
        #-->Add element ONLY if it's in both list2 and list3
        if i in list2 and i in list3:
            arr.append(i) 
    return arr

print(intersection([1, 2, 3, 4], [2, 4, 6, 8], [3, 4, 5]))
# [4]
