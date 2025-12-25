# 0 1 1 2 3 5 8
def fib_top_down(n, memo={}):
    if n <= 1:
        return n
    
    if n not in memo:
        memo[n] = fib_top_down(n-1, memo) + fib_top_down(n-2, memo)
        print(memo)
    
    return memo[n]

n = 10
# fib_top_down(n)

#                   fib(8)
#    fib(6)          +             fib(7)
# fib(4) + fib(5)             fib(5)   + fib(6)

def fib_bottom_up(n):
    if n <= 1:
        return n
    
    table = [0] * (n + 1)
    table[1] = 1
    print(table)

    for i in range(2, n+1):
        table[i] = table[i-1] + table[i-2]
        print(table)

    return table[n]

print(fib_bottom_up(n))