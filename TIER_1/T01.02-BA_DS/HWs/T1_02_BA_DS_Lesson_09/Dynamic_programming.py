def find_min_coins(amount, coins):
    """
    Dynamic Programming (bottom-up)
    Goal: make 'amount' with MIN number of coins.
    """
    coins = sorted(coins)      # sorts coins from small to big
    n = len(coins)

    INF = float("inf")         # "infinity" for large number

    # dp[i][s] = minimum coins to make sum s using first i coin types
    dp = [[INF for s in range(amount + 1)] for i in range(n + 1)]

    for i in range(n + 1):     # base case: sum 0 needs 0 coins
        dp[i][0] = 0

    # fill table bottom-up (knapsack)
    for i in range(1, n + 1):
        coin = coins[i - 1]
        for s in range(1, amount + 1):  # s - current sum

            # Option 1: do not use this coin
            dp[i][s] = dp[i - 1][s]

            # Option 2: use this coin (unlimited times = stays in same row i)
            if coin <= s:
                dp[i][s] = min(dp[i][s], 1 + dp[i][s - coin])

    if dp[n][amount] >= INF:
        return {}

    result = {}         # restore answer (shows which coins were used)
    i = n
    s = amount

    while s > 0 and i > 0:
        # dp[i][s] equals dp[i-1][s] means coin i was not used
        if dp[i][s] == dp[i - 1][s]:
            i -= 1
        else:
            coin = coins[i - 1]     # coin i was used
            result[coin] = result.get(coin, 0) + 1
            s -= coin               # stay on the same type of coin i

    return result


if __name__ == "__main__":
    coins = [50, 25, 10, 5, 2, 1]
    amount = 113
    print(find_min_coins(amount, coins))
