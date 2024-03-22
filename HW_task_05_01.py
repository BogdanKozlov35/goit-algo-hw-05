# ФУНКЦІЯ caching_fibonacci
def caching_fibonacci():
    cache = {0: 0, 1: 1}
    def fibonacci(n):

        if n in cache:
            return cache[n]
        else:
            cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
            return cache[n]
    return fibonacci
def main ():

    fib_func = caching_fibonacci()

    print(fib_func(5))
    print(fib_func(10))
    print(fib_func(15))
    print(fib_func(20))
    print(fib_func(0))
    print(fib_func(1))

if __name__ == "__main__":
    main()

