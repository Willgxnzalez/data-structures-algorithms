# Fibonacci using Recursion & Top-Down Memoization
# Avoids recomputing sub-problems by storing their result(memoization) in a hashmap  

memo = {}
def fib(n):
    if n in memo:
        return memo[n]
    
    if n <= 2:
        result = 1
    else:
        result = fib(n-1) + fib(n-2)
    memo[n] = result
    return result


print(fib(100))


# Fibonacci using Iterative & Bottom-Up Tabulation
def fib2(n):
    memo = {}
    for i in range(1, n+1): #include n
        if i <= 2:
            memo[i] = 1
        else:
            memo[i] = memo[i-1] + memo[i-2]
    return memo[n]



print(fib2(100))