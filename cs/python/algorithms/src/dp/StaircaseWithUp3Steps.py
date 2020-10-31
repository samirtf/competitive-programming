# Problem:
#   Climbing Stairs (with up 3 steps)
#
#   You are climbing a stair case. It takes n steps to reach to the top.
#   Each time you can either climb 1, 2 or 3 steps.
#   In how many distinct ways can you climb to the top?
#
#   Framework for Solving DP Problems:
#   1. Define the objective function.
#   2. Identify base cases
#       f(0) = 1
#       f(1) = 1
#       f(2) = 2
#   3. Write down a recurrence relatiion for the optimized objective function.
#       f(n) = f(n - 1) + f(n - 2) + f(n - 3)
#   4. What's the order of execution?
#       bottom-up
#   5. Where to look for the answer?
#       f(n)
#
#
#

class StaircaseWithUp3steps:

    def climbStairsWithUp3Steps(self, ithStep):
        if ithStep == 0 or ithStep == 1:
            return 1
        if ithStep == 2:
            return 2
        memo = [None] * (ithStep + 1)
        memo[0] = 1
        memo[1] = 1
        memo[2] = 2
        for i in range(3, ithStep + 1):
            memo[i] = memo[i - 1] + memo[i - 2] + memo[i - 3]
        return memo[ithStep]

    def climbStairsWithUp3StepsOptimized(self, ithStep):
        if ithStep == 0 or ithStep == 1:
            return 1
        if ithStep == 2:
            return 2
        a = 1
        b = 1
        c = 2
        r = 0
        for i in range(3, ithStep + 1):
            r = a + b + c
            a = b
            b = c
            c = r
        return r