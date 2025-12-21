def fibo(n, a, b):
    if (n > 0): 
        fibo(n-1, b, a +b)
    print(a, end=" ")  # print current number


# 1 1 2 3 5 8 ...


def recur_fibo(n):
    if n <= 1:  # Base case
        return n == 1  # return True for n=1 and False for n=0
    else:
        return (recur_fibo(n - 1) + recur_fibo(n - 2))  # recursive sum


#1 1 2 3 5 8


def iter_fibo(n):
    result = 1  # start value
    for i in range(n):  # loop n times
        n += n + i  # change n each iteration
    return result  # return result


if __name__ == "__main__":
    N = 5  # number for tests
    print(recur_fibo(N))  # print recursion result
    fibo(N, 1, 1)  # print N fibonacci numbers
    print(iter_fibo(10))  # print iterative result
