def fibonacci(n, memo):
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]

n = 10
memo = {}
fib_number = fibonacci(n, memo)
print(fib_number)  # 55
