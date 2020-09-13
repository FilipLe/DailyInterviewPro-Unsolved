import math
def make_change(coins, n):
    # Fill this in.
    count = 0
    value = n
    change = []
    while value > 0:
        if value > coins[3]:
            amountQuarter = math.floor(value/coins[3])
            count += amountQuarter
            value -= (amountQuarter*coins[3])
            for x in range(amountQuarter):
                change.append(coins[3])
            
        elif value > coins[2] and value < coins[3]:
            amountDime = math.floor(value/coins[2])
            count += amountDime
            value -= (amountDime*coins[2])
            for x in range(amountDime):
                change.append(coins[2])
            
        elif value > coins[1] and value < coins[2]:
            amountNickel = math.floor(value/coins[1])
            count += amountNickel
            value -= (amountNickel*coins[1])
            for x in range(amountNickel):
                change.append(coins[1])
            
        elif value > 0 and value < coins[1]:
            amountCent = math.floor(value/coins[0])
            count += amountCent
            value -= (amountCent*coins[0])
            for x in range(amountCent):
                change.append(coins[0])
            
    return count, change
print(make_change([1, 5, 10, 25], 36))
# 3 coins (25 + 10 + 1)
