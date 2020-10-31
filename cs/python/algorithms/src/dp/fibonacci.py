def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci_dp(n, memo):
    if memo[n] is not None:
        return memo[n]
    if n == 1 or n == 2:
        result = 1
    else:
        result = fibonacci_dp(n - 1, memo) + fibonacci_dp(n - 2, memo)
    memo[n] = result
    return result


def fibonacci_memo(n):
    memo = [None] * (n + 1)
    return fibonacci_dp(n, memo)


def fibonacci_bottom_up(n):
    if n == 1 or n == 2:
        return 1
    bottom_up = [None] * (n + 1)
    bottom_up[1] = 1
    bottom_up[2] = 1
    for i in range(3, n + 1):
        bottom_up[i] = bottom_up[i - 1] + bottom_up[i - 2]
    return bottom_up[n]


print(fibonacci(35))
print(fibonacci_memo(35))
print(fibonacci_bottom_up(35))