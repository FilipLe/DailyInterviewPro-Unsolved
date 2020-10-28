def checkPerfectNumber(num):
# Fill this in.
    #Array to store input's factors, excluding self
    factors = []
    i = 1
    #While loop to find factors, excluding self
    while i < num:
        if num % i == 0:
            factors.append(i)
        i += 1
    
    #Store sum of factors, excluding self
    total = 0
    #Initialize counter
    count = 0
    #loop to add all the factors
    while count < len(factors):
        total += factors[count]
        count += 1

    if total == num:
        return True
    else:
        return False
    
print(checkPerfectNumber(28))
# True
# 28 = 1 + 2 + 4 + 7 + 14
