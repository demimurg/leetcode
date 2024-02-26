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
    [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 2, 1], [3, 1, 2]]
    >>> permute([0, 1])
    [[0, 1], [1, 0]]
    >>> permute([1])
    [[1]]
    """
    res = []

    def backtrack(i):
        if i == len(nums):
            res.append(nums[:])

        for j in range(i, len(nums)):
            nums[i], nums[j] = nums[j], nums[i]
            backtrack(i + 1)
            nums[i], nums[j] = nums[j], nums[i]

    backtrack(0)
    return res


def subsets_with_dup(nums: List[int]) -> List[List[int]]:
    """
    Given an integer array nums that may contain duplicates, return all possible subsets (the power set).
    The solution set must not contain duplicate subsets. Return the solution in any order.
    [MEDIUM] https://leetcode.com/problems/subsets-ii/

    >>> subsets_with_dup([1, 2, 2])
    [[], [1], [2], [1, 2], [2, 2], [1, 2, 2]]
    >>> subsets_with_dup([0])
    [[], [0]]
    """
    nums.sort()
    subs = [[]]
    end = 0
    for i in range(len(nums)):
        same_num = i > 0 and nums[i] == nums[i - 1]
        start = 0 if not same_num else end  # skip duplicates
        end = len(subs)
        for j in range(start, end):
            subs.append(subs[j] + [nums[i]])

    return subs


def combination_sum2(candidates: List[int], target: int) -> List[List[int]]:
    """
    Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations
    in candidates where the candidate numbers sum to target. Each number in candidates may only be used once in
    the combination. Note: The solution set must not contain duplicate combinations.
    [MEDIUM] https://leetcode.com/problems/combination-sum-ii/

    >>> combination_sum2([10,1,2,7,6,1,5], 8)
    [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]
    >>> combination_sum2([2,5,2,1,2], 5)
    [[1, 2, 2], [5]]
    """
    candidates.sort()
    result = []

    def dfs(nums: List[int], nums_sum: int, i: int, last_added=False):
        if nums_sum == target:
            result.append(nums.copy())
            return
        if i == len(candidates) or nums_sum > target:
            return

        same_skipped = not last_added and i > 0 and candidates[i] == candidates[i - 1]
        if not same_skipped:
            nums.append(candidates[i])
            dfs(nums, nums_sum + candidates[i], i + 1, last_added=True)
            nums.pop()
        dfs(nums, nums_sum, i + 1)

    dfs([], 0, 0)
    return result


if __name__ == "__main__":
    import doctest

    doctest.testmod()
