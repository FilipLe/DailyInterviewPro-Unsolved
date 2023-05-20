def pow(x, n):
    # base case
    if n == 0:
        return 1
    
    #recursive case
    else:
        if x % 2 == 0:
            return pow(x, n/2)
        else:
            return x * pow(x, n - 1)

print(pow(5, 3))
# 125
