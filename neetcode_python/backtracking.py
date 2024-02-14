from typing import *


def subsets(nums: List[int]) -> List[List[int]]:
    """
    Given an integer array nums of unique elements, return all possible subsets (the power set).
    The solution set must not contain duplicate subsets. Return the solution in any order.
    [MEDIUM] https://leetcode.com/problems/subsets/

    >>> subsets([1,2,3])
    [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
    >>> subsets([0])
    [[], [0]]
    """
    subs = [[]]
    for n in nums:
        for i in range(len(subs)):
            subs.append(subs[i] + [n])
    return subs


if __name__ == "__main__":
    import doctest

    doctest.testmod()
