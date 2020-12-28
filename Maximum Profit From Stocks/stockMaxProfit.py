def buy_and_sell(arr):
    #Fill this in.
    #Main idea is that we have count, which iterates through every element of array
    #and count2 iterates through elements to the right of the current element in count
    
    #Var to store the biggest profit
    biggestDifference = 0
    #counter to iterate through every element
    count = 0 
    #shift 1 element to the right
    count2 = count + 1
    
    #Main loop
    while count < len(arr):
        while count2 < len(arr):
            
            #This line was to test if iteration worked properly
            #arr[count] will be every element
            #arr[count] will be every element except to the ones to its left
            #uncomment and run this code to understand
            #print(arr[count],',',arr[count2])
            
            #Max profit basically biggest difference between opening price (buy) and closing price (Sell)
            if arr[count2] - arr[count] > biggestDifference:
                biggestDifference = arr[count2] - arr[count]
                
            count2 += 1
        #reset count2
        count2 = count + 1
        count += 1
        
    return biggestDifference
print(buy_and_sell([9, 11, 8, 5, 7, 10]))
# 5
