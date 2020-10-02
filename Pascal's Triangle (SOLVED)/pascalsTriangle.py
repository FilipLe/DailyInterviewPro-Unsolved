import math
def pascal_triangle_row(n):
    # Fill this in.
    # return list of (n-1)Ck, k 0-->n-1
    
    #Binomial theorem
    #          n
    #(a+b)^n = Σ(nCk)•a^(n-k)•b^k
    #         k=0
    coefficients = []
    k=0
    exponent = n - 1# if we do row 6, we only do 5 exponents as shown in example below
    while k < exponent + 1:
        #formula to calulate Combination
        #nCk = n!÷[(n-k)!•k!]
        coefficients.append(int(math.factorial(exponent)/(math.factorial(exponent-k)*math.factorial(k))))
        k += 1
    return coefficients

print(pascal_triangle_row(6))
# [1, 5, 10, 10, 5, 1]
# these are coefficients of (x+1)^5
# we are returning list of nCk, in this case 5Ck, k 0-->5

