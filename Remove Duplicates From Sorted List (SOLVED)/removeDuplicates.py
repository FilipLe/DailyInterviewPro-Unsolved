#Method 1: Naive solution to remove duplicates from list
def remove_dups(nums):
    # Fill this in.
    #Initialize array to store duplicates
    arr = [] 
    #loop through elements in the sorted list
    for i in nums:
        #if the current element does not exist in the array of duplicates,
        if i not in arr:
            #add that element
            arr.append(i)
    return arr

#Method 2: Using set() to remove duplicates from list
def remove_dups1(nums):
    # Fill this in.
    arr = list(set(nums))
    return arr

#Method 3: Using dict to remove duplicates from list
def remove_dups2(nums):
    # Fill this in.
    #dict.fromkeys(nums) --> Creates a dictionary, using the List items as keys. 
    #This will automatically remove any duplicates because dictionaries cannot have duplicate keys.
    arr = list(dict.fromkeys(nums))#the convert back to list using list() method
    return arr

nums = [1, 1, 2, 3, 4, 4, 4, 4, 4, 5, 5, 6, 7, 9]
print(remove_dups(nums))
# [1, 2, 3, 4, 5, 6, 7, 9]
print(len(remove_dups(nums)))
# 8

nums = [1, 1, 1, 1, 1, 1]
print(remove_dups(nums))
print(len(remove_dups(nums)))
# [1]
# 1
 
