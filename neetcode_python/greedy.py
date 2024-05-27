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
