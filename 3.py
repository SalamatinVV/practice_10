def fib_memoization(n):
    memory = {}
    if n in memory:
        return memory[n]
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    else:
        number = fib_memoization(n - 1) + fib_memoization(n - 2)
        memory[n] = number
    return number


print(fib_memoization(35))
