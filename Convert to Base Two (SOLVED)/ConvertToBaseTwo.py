def base_2(n):
    # Fill this in.
    binary = ""
    while n > 0:
        remainder = n % 2
        n = (n - remainder)/2
        if remainder == 0:
            binary = "0" + binary
        else:
            binary = "1" + binary
    return binary

print(base_2(123))
# 1111011