import timeit

def find_coins_greedy(sum, coins):   # big coin first
    """
    Greedy algorithm:
    Takes coins in descending order (from largest to smallest)
    """
    coins_count = {}

    for coin in sorted(coins, reverse=True):
        count = sum // coin    # counts how many coins we can take
        if count > 0:          # save in dictionary
            coins_count[coin] = count
        sum -= coin * count    # how much amount left
    return coins_count


def find_coins_greedy_slow(sum, coins): 
    """
    Substruct coins one by one in loop
    """
    coins_count = {}

    for coin in sorted(coins, reverse=True): # sort coins from biggest to smallest
        while sum >= coin:  # continue taking this coin while we still can
            sum -= coin
            coins_count[coin] = coins_count.get(coin, 0) + 1
    return coins_count


def find_coins_greedy_fast(sum, coins):
    """
    Use integer division and modulo
    """
    coins_count = {}

    for coin in coins:      # take as many coins of this type as possible
        count = sum // coin
        if count:           
            coins_count[coin] = count
            sum %= coin
        if sum == 0:
            break
    return coins_count


if __name__ == "__main__":
    cases = [
        ([50, 25, 10, 5, 2, 1], 137),
        ([10, 6, 1], 12),
        ([25, 10, 5, 2, 1], 543210),
    ]

    functions = [find_coins_greedy, find_coins_greedy_slow, find_coins_greedy_fast]

    for coins, cash_amount in cases:
        print(f"\n\tCase for {coins} and sum: {cash_amount}")
        for fun in functions:
            result = fun(cash_amount, coins)

            t = timeit.timeit(lambda: fun(cash_amount, coins), number=10000)

            print("Result for {}: {}".format(fun.__name__, result))
            print("Time taken for {}: {:.6f} seconds".format(fun.__name__, t))
