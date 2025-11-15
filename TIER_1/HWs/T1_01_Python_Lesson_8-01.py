def caching_fibo():      # Creates a Fibonacci function with caching
    cache = {}           # Stores already calculated Fibonacci numbers

    def fibo(n):
        """
        Calculate the n-th Fibonacci number using recursion and caching.

        Argument:
            n (int): Fibonacci index

        Returns:
            int: Fibonacci number at position n
        """

        if n <= 0:           # possible inputs
            return 0
        if n == 1:
            return 1

        if n in cache:       # returns cached result
            return cache[n]

        cache[n] = fibo(n - 1) + fibo(n - 2)   # recursive calculation using caching
        return cache[n]
    return fibo


# TEST FUNCTION
def test_fibo():
    """
    For demonstration purposes
    Prints Fibonacci numbers for an example
    """

    fib = caching_fibo()

    print("Testing Fibonacci with caching:")
    print("fib(10) =", fib(10))   # 55
    print("fib(15) =", fib(15))   # 610
    print("fib(20) =", fib(20))   # 6765
    print("fib(30) =", fib(30))   # 832040 — instant due to cache
    print("Re-check fib(30) =", fib(30))  # cached result

if __name__ == "__main__":        # Runs test
    test_fibo()
