from typing import *


def max_sub_array(nums: List[int]) -> int:
    """
    Given an integer array nums, find the subarray with the largest sum, and return its sum.
    [MEDIUM] https://leetcode.com/problems/maximum-subarray/

    >>> max_sub_array([-2,1,-3,4,-1,2,1,-5,4])
    6
    >>> max_sub_array([1])
    1
    >>> max_sub_array([5,4,-1,7,8])
    23
    """
    cur_sum, max_sum = 0, -(10 ** 4)
    for num in nums:
        # cur_sum < 0 can't add positive value for current interval
        cur_sum = max(cur_sum, 0) + num
        max_sum = max(max_sum, cur_sum)
    return max_sum


def can_jump(nums: List[int]) -> bool:
    """
    You are given an integer array nums. You are initially positioned at the array's first index,
    and each element in the array represents your maximum jump length at that position.

    Return true if you can reach the last index, or false otherwise.
    [MEDIUM] https://leetcode.com/problems/jump-game/

    >>> can_jump([2, 3, 1, 1, 4])
    True
    >>> can_jump([3, 2, 1, 0, 4])
    False
    """
    can_jump_i = 0
    for i in range(len(nums)):
        can_jump_i = max(can_jump_i, i + nums[i])
        if can_jump_i >= len(nums):
            return True
        if can_jump_i <= i:
            return False
    return True


def jump(nums: List[int]) -> int:
    """
    You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].
    Each element nums[i] represents the maximum length of a forward jump from index i. In other words,
    if you are at nums[i], you can jump to any nums[i + j] where:
    - 0 <= j <= nums[i] and
    - i + j < n

    Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].
    [MEDIUM] https://leetcode.com/problems/jump-game-ii/

    >>> jump([2, 3, 1, 1, 4])
    2
    >>> jump([2, 3, 0, 1, 4])
    2
    """
    l, r = 0, 0
    min_steps = 0
    # stop, when we can reach last step from current level
    while r < len(nums) - 1:
        new_r = r
        # iterate over next steps
        for i in range(l, r + 1):
            # find new farthest jump r
            new_r = max(new_r, i + nums[i])
        l, r = r, new_r
        # new level of possible steps added
        min_steps += 1

    return min_steps


def can_complete_circuit(gas: List[int], cost: List[int]) -> int:
    """
    There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].

    You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next
    (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.

    Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit
    once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique.

    [MEDIUM] https://leetcode.com/problems/gas-station/

    >>> can_complete_circuit([1,2,3,4,5], [3,4,5,1,2])
    3
    >>> can_complete_circuit([2,3,4], [3,4,3])
    -1
    """
    cur, total, start_i = 0, 0, 0
    for i in range(len(gas)):
        diff = gas[i] - cost[i]
        cur += diff
        total += diff
        if cur < 0:
            cur = 0
            start_i = i + 1

    return start_i if total >= 0 else -1


if __name__ == "__main__":
    import doctest

    doctest.testmod()
