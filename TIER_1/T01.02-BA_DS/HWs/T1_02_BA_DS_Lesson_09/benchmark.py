import timeit

from Greedy import find_coins_greedy, find_coins_greedy_fast, find_coins_greedy_slow
from Dynamic_programming import find_min_coins


def bench_seconds_per_call(func, amount, coins, number=200, repeat=5):
    """
    Measure time as seconds per call:
    1. Run func(amount, coins) 'number' times
    2. Repeat this X times
    3. Take the minimal total time and divide by number
    """
    times = timeit.repeat(lambda: func(amount, coins), number=number, repeat=repeat)
    return min(times) / number


if __name__ == "__main__":
    coins = [50, 25, 10, 5, 2, 1]
    amounts = [113, 1000, 5000]

    number = 200
    repeat = 5

    algorithms = [
        ("Greedy", find_coins_greedy),
        ("Greedy Fast", find_coins_greedy_fast),
        ("Greedy Slow", find_coins_greedy_slow),
        ("DP", find_min_coins),
    ]

    print("Coins:", coins)
    print("Metric: seconds per call (min of {} runs), number={}".format(repeat, number))
    print()

    # Header
    header = "{:<12}".format("Amount")
    for name, _ in algorithms:
        header += "{:<18}".format(name)
    print(header)
    print("-" * len(header))

    # Rows
    for a in amounts:
        row = "{:<12}".format(a)
        for _name, func in algorithms:
            t = bench_seconds_per_call(func, a, coins, number=number, repeat=repeat)
            row += "{:<18.8f}".format(t)
        print(row)

    print("\nCheck (results for amount=113):")
    for name, func in algorithms:
        print("{:<12} -> {}".format(name, func(113, coins)))
