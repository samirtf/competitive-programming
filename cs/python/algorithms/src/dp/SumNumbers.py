# Problem: Find the sum of the first N numbers.
#
# Objective function:
# f(i) is the sum of the first i elements.
#
# Recurrence relation:
# f(n) = f(n - 1) + n
#
# 1 + 2 + 3 + 4 + 5 + ... + N = sum of ( i ) from i to n
#
# F(1) = 1
# F(2) = F(1) + 2 = 3
# F(3) = F(2) + 3 = 6
# F(4) = F(3) + 4 = 10
# F(n) = F(n - 1) + n


class SumNumbers:

    def sum_numbers_recursive(self, n):
        if n == 1:
            return 1
        return self.sum_numbers_recursive(n - 1) + n

    @staticmethod
    def sum_numbers_dp(n):
        memo = [None] * (n + 1)
        memo[0] = 0
        for i in range(1, n + 1):
            memo[i] = memo[i - 1] + i
        return memo[n]

# print(sum_numbers_recursive(1))
# print(sum_numbers_recursive(2))
# print(sum_numbers_recursive(3))
# print(sum_numbers_recursive(4))
#
#
#
# print(sum_numbers_dp(1))
# print(sum_numbers_dp(2))
# print(sum_numbers_dp(3))
# print(sum_numbers_dp(4))

