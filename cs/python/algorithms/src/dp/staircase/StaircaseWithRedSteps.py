# Climbing staircase skipping the red steps
#
#       R       R   R
#   0   1   2   3   4   5   6   7
#   1   0   1   0   0   1   1   2
#   _____
#           _________
#               _________
#                   _________
#
#


class StaircaseWithRedSteps:

    @staticmethod
    def climb_stairs_k_steps_skip_red(n, k, red_steps):
        memo = [0] * k
        memo[0] = 1
        # 1 2 3 4 5 6
        for i in range(1, n + 1):
            # 1 2
            for j in range(1, k): # run only to k, because i%k already is contained in opp memo += memo.
                # 1: 1 2
                # 0 -1
                print("i:", i, " j:", j, "i % k:", i % k, " (i - j) % k:", (i - j) % k)
                if i - j < 0:
                    continue
                if i < len(red_steps) and red_steps[i]:
                    memo[(i % k)] = 0
                else:
                    memo[(i % k)] += memo[(i - j) % k]
        return memo[n % k]


# correct
# 0 1 2 3 4 5 6 7
# 1 0 1 0 0 1 1 2

# 0 1 2 3 4 5 6 7 8
# 1 1 0 2 0 0 2 2 4
# red_steps = [False, True, False, True, True, False, False, False]
# print(StaircaseWithRedSteps.climb_stairs_k_steps_skip_red(0, 3, red_steps))
# print(StaircaseWithRedSteps.climb_stairs_k_steps_skip_red(1, 3, red_steps))
# print(StaircaseWithRedSteps.climb_stairs_k_steps_skip_red(2, 3, red_steps))
# print(StaircaseWithRedSteps.climb_stairs_k_steps_skip_red(3, 3, red_steps))
# print(StaircaseWithRedSteps.climb_stairs_k_steps_skip_red(4, 3, red_steps))
# print(StaircaseWithRedSteps.climb_stairs_k_steps_skip_red(5, 3, red_steps))
# print(StaircaseWithRedSteps.climb_stairs_k_steps_skip_red(6, 3, red_steps))
# print(StaircaseWithRedSteps.climb_stairs_k_steps_skip_red(7, 3, red_steps))
# print(StaircaseWithRedSteps.climb_stairs_k_steps_skip_red(8, 3, red_steps))
# quebra no red step print(StaircaseWithRedSteps.climb_stairs_k_steps_skip_red(9, 3, red_steps))
# 1 0 0 1 0 0 1 0 1
# print("")
#
# print(StaircaseWithRedSteps.climb_stairs_k_steps_skip_red(0, 3, red_steps))
# print(StaircaseWithRedSteps.climb_stairs_k_steps_skip_red(1, 3, red_steps))
# print(StaircaseWithRedSteps.climb_stairs_k_steps_skip_red(2, 3, red_steps))
# print(StaircaseWithRedSteps.climb_stairs_k_steps_skip_red(3, 3, red_steps))
# print(StaircaseWithRedSteps.climb_stairs_k_steps_skip_red(4, 3, red_steps))
# print(StaircaseWithRedSteps.climb_stairs_k_steps_skip_red(5, 3, red_steps))
# print(StaircaseWithRedSteps.climb_stairs_k_steps_skip_red(6, 3, red_steps))
# print(StaircaseWithRedSteps.climb_stairs_k_steps_skip_red(7, 3, red_steps))
# print(StaircaseWithRedSteps.climb_stairs_k_steps_skip_red(8, 3, red_steps))
# 1 0 0 1 0 0 1 0 1