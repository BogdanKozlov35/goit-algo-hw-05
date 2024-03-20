# ФУНКЦІЯ caching_fibonacci
from collections import defaultdict
def caching_fibonacci():
    cache = defaultdict(int)
    def fibonacci(n):

        if n <= 0:
            return 0
        if n ==1:
            return 1
        if n in cache:
            return cache[n]
        else:
            cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
            #print(cache)
            return cache[n]
    return fibonacci
fib_func = caching_fibonacci()

print(fib_func(10))
print(fib_func(15))
print(fib_func(20))
print(fib_func(100))
print(fib_func(0))
print(fib_func(1))

