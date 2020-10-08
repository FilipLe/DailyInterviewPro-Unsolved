def products(nums):
    # Fill this in.
    # Array to store products  
    products = []
    #Initialize counter
    count = 0
    #Iterate through the elements of the array
    while count < len(nums):
        #Assign a var to store the index of current element 
        current_count = count
        #Assign a new counter for the elements other than the current element
        new_count = 0
        
        #Create array to store the elements that will be multiplied to get products -->  elements other than the current element
    
        #E.g. in the list [1,2,3,4,5], if we are currently on element '2', 
        #this array will store [1,3,4,5]-->these elements will be multiplied to get the product '60'
        current_factors = []
        #Loop to iterate through elements, but to find elements other than the current elements
        while new_count < len(nums):
            #If the index of the elements we are looping through isn't the same as the index of current element
            if new_count != current_count:
                #store the element at that index
                current_factors.append(nums[new_count])
            new_count += 1
        
        #Loop to find product of elements except self
        #Counter to go through elements in the list containing elements except self
        factor_count = 0
        #Initialize a var to keep up the product of elements in array except self element
        current_product = 1
        #Loop to calculate product of elements in array except self element
        while factor_count < len(current_factors):
            current_product = current_product * current_factors[factor_count]
            factor_count += 1
        #Store the products in a separate array
        products.append(current_product)
        #Increment counter after finding product of elements except self and move to next element and do the same
        count += 1
    return products

print(products([1, 2, 3, 4, 5]))
# [120, 60, 40, 30, 24]
