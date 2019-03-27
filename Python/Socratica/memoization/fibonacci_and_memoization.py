from functools import lru_cache

@lru_cache(maxsize = 1000)
def fibonacci_with_memoization(n):
    # * Chek the input is a positive integer
    if type(n) != int:
        raise TypeError("n must be a positive integer")
    if n < 1:
        raise ValueError("n must be a positive integer")
    
    # Compute the Nth term
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci_with_memoization(n - 1) + fibonacci_with_memoization(n - 2)

for i in range(1, 1001):
    print("{}: {}".format(i, fibonacci_with_memoization(i)))