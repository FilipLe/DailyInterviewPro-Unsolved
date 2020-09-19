def find_primes(n):
    # Fill this in.
    
    #First prime is 2
    count = 2
    #Array to store prime numbers
    primes = []
    #While loop to find prime numbers
    while count < n+1:
        #initialize array to store factors of current number
        factors = []
        factor = 1
        #while loop to find factors of curren number
        while count+1>factor:
            #If the current number is divisible by the current factor, add factor to list of factors
            if count%factor==0:
                #remainder 0 when divided the var factor
                #Add to list if it is divisble
                factors.append(factor)
            factor+=1
        #If the number has 2 factors (1 and itself) --> it is a prime number
        if len(factors)==2:
            primes.append(count)
        count += 1
    return primes

print(find_primes(14))
# [2, 3, 5, 7, 11, 13]