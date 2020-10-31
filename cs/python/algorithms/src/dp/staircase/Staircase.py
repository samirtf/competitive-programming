# https://www.geeksforgeeks.org/count-ways-reach-nth-stair/
# https://www.slader.com/discussion/question/a-find-a-recurrence-relation-for-the-number-of-ways-to-climb-n-stairs-if-the-person-climbing-the-sta/
#
# Fin(i) is the number of distinct ways to reach the i-th stair.
# F(2) = 2 distinct ways to reach the 2nd stair from stair 0.
# F(1) = 1 distinct way to reach the 1st stair from stair 0.
# F(0) = 1 distinct way to reach the 0 stair from stair 0.
#
# F(n) = F(n - 1) + F(n - 2)

# a) Find a recurrence relation for the number of ways to climb n stairs
# if the person climbing the stairs can take one stair of two stairs at a time.
# b) What are the initial conditions?
# c) In how many ways can this person climb a flight of eight stairs?
#
# a) Let n-thA be the number of ways to climb n stairs. In order to climb n stairs, a person must either start with
# a step of one stair and then climb n - 1 stairs (and this can be done in (n-1)thA ways) or else start with a step
# of two stairs and then climb n - 2 stairs (and this can be done in (n-2)thA ways).
#
# From this analysis we can immediately write down the recurrence relation, valid for all n >= 2;
# n-thA = (n-1)thA + (n-2)thA
#
# b) The initial conditions are a0 = 1 and a1 = 1. Since there is one way to climb no stairs (do nothing) and clearly
# only one way to climb one stair. Note that the recurrence relation is the same as that for the Fibonacci sequence
# , and the initial conditions are that a0 = f1 and a1 = f2, so it must be that aN = fn+1 for all n.
#
# c) Each term in our sequence {an} is the sum of the previous two terms, so the sequence begins a0 = 1, a1 = 1,
# a2 = 2, a3 = 3, a4 = 5, a5 = 8, a6 = 13, a7 = 21, a8 = 34. Thus a person can climb a flight fo 8 stairs in
# 34 ways under the restrictions in this problem.
#
#
# Climbing Stairs
# You are climbing a staircase. It takes n steps to reach to the top.
# Each time you can either climb 1 or 2 steps.
# In how many distinct ways can you climb to the top?
#
#
# Framework for Solving DP problems:
# 1. Define objective function
# 2. Identify base cases
# 3. Recurrence relation
# 4. Order of computation
# 5. Location of the answer
#
#
# Framework for Solving DP problems:
# 1. Define objective function
#       f(i) is the number of distinct ways to reach the i-th stair.
# 2. Identify base cases
#       f(0) = 1
#       f(1) = 1
# 3. Recurrence relation - Write down a recurrence relation for the optimized objective function
#       f(n) = f(n - 1) + f(n - 2)
# 4. Order of computation
#       bottom-up
# 5. Location of the answer
#       f(n)
#


class Staircase:

    # Time complexity: O(n)
    # Space complexity: O(n)
    @staticmethod
    def find_number_of_distinct_ways_to_reach(ith_step):
        if ith_step == 0 or ith_step == 1:
            return 1
        memo = [None] * (ith_step + 1)
        memo[0] = 1
        memo[1] = 1
        for i in range(2, ith_step + 1):
            memo[i] = memo[i - 1] + memo[i - 2]
        return memo[ith_step]

    @staticmethod
    def find_number_of_distinct_ways_to_reach_optimized(ith_step):
        if ith_step == 0 or ith_step == 1:
            return 1
        a = 1
        b = 1
        c = 0
        for i in range(2, ith_step + 1):
            c = a + b
            a = b
            b = c
        return c
