def fib_cycle(n):
    first = 1
    second = 1
    i = 0
    while i < n - 2:
        sum = first + second
        first = second
        second = sum
        i = i + 1
    return second


print(fib_cycle(6))
