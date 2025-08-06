# Select minimum number of coins needed to reach target amount
# coins 1,5,10,25


# Using only recursion
def min_coin(t, coins):
    if t == 0:
        return 0
    else:
        answer = float('inf')
        for c in coins:
            sub = t - c
            if sub < 0:
                continue            
            answer = min(answer, min_coin(sub, coins) + 1) # +1 comes from sub = t - c
        return answer
    
    
memo = {} # Will store the minimum number of coins needed for each amount
def min_coin2(t, coins):
    if t in memo:
        return memo[t]
    elif t == 0:
        answer = 0
    else:
        answer = float('inf')
        for c in coins:
            sub = t - c
            if sub < 0:
                continue
            answer = min(answer, min_coin2(t-c, coins) + 1)
    memo[t] = answer
    return answer

# print(min_coin(50, (1,5,10,25)))
print(min_coin2(150, coins=(1,4,5)))