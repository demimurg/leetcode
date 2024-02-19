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


def combination_sum(candidates: List[int], target: int) -> List[List[int]]:
    """
    Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations
    of candidates where the chosen numbers sum to target. The same number may be chosen from candidates an unlimited
    number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.
    [MEDIUM] https://leetcode.com/problems/combination-sum/

    >>> combination_sum([2, 3, 6, 7], 7)
    [[2, 2, 3], [7]]
    >>> combination_sum([2, 3, 5], 8)
    [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
    >>> combination_sum([2], 1)
    []
    """
    result = []

    def dfs(nums: List[int], nums_sum: int, i: int):
        if i == len(candidates) or nums_sum > target:
            return
        if nums_sum == target:
            result.append(nums.copy())
            return

        nums.append(candidates[i])
        dfs(nums, nums_sum + candidates[i], i)
        nums.pop()
        dfs(nums, nums_sum, i + 1)

    dfs([], 0, 0)
    return result


def permute(nums: List[int]) -> List[List[int]]:
    """
    Given an array nums of distinct integers, return all the possible permutations.
    You can return the answer in any order.
    [MEDIUM] https://leetcode.com/problems/permutations/

    >>> permute([1, 2, 3])
    [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    >>> permute([0, 1])
    [[0, 1], [1, 0]]
    >>> permute([1])
    [[1]]
    """
    result, perm, perm_set = [], [], set([])

    def backtrack():
        if len(perm) == len(nums):
            result.append(perm.copy())
            return

        for num in nums:
            if num in perm_set:
                continue

            perm.append(num)
            perm_set.add(num)
            backtrack()
            perm.pop()
            perm_set.remove(num)

    backtrack()
    return result


if __name__ == "__main__":
    import doctest

    doctest.testmod()
