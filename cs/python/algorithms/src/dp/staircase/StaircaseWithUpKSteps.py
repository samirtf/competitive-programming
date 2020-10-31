# Problem:
#   Climbing Stairs (k steps)
#
#   You are climbing a staircase. It takes n steps to reach to the top.
#   Each time you can climb 1..k steps.
#   In how many distinct ways can you climb to the top?
#
#   Framework for Solving DP Problems:
#       1. Define the objective function.
#           f(i) is the number of distinct ways to reach the i-th stair by making 1 to k steps.
#       2. Identify base cases
#           f(0) = 1
#           f(1) = 1
#       3. Recurrence relation - write down a recurrence relation for the optimized objective function.
#           f(n) = f(n - 1) + f(n - 2) + ... + f(n - k)
#       4. What's the order of execution?
#           bottom-up
#       5. Where to look for the answer?
#           f(n)


class StaircaseWithUpKSteps:

    @staticmethod
    def climb_stairs_with_up_3_steps(ith_step, k):
        if ith_step == 0 or ith_step == 1:
            return 1
        memo = [0] * (ith_step + 1)
        memo[0] = 1
        memo[1] = 1
        for i in range(2, ith_step + 1):
            for j in range(1, k + 1):
                if i - j < 0:
                    continue
                memo[i] += memo[i - j]
        return memo[ith_step]
