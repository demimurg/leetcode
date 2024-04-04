from collections import deque
from typing import List


def climb_stairs(n: int) -> int:
    """
    You are climbing a staircase with n steps to reach the top. Each time you can climb 1 or 2 steps. 
    The function calculates how many distinct ways you can climb to the top.
    [EASY] https://leetcode.com/problems/climbing-stairs/

    >>> climb_stairs(2)
    2
    >>> climb_stairs(3)
    3
    """
    if n <= 2:
        return n

    prelast, last = 1, 2
    for _ in range(n - 2):
        prelast, last = last, prelast + last
    return last


def min_cost_climbing_stairs(cost: List[int]) -> int:
    """
    Given a staircase where the ith step has a non-negative cost associated with it represented by the array cost[],
    we can climb one or two steps at a time. The goal is to find the minimum cost to reach the top of the staircase
    starting from either the first step or the second step. We pay the cost of a step before climbing it. After paying,
    we can either climb one step or two steps. The top of the staircase is beyond the last step.
    [EASY] https://leetcode.com/problems/min-cost-climbing-stairs/

    >>> min_cost_climbing_stairs([10, 15, 20])
    15
    >>> min_cost_climbing_stairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1])
    6
    """
    a, b = 0, 0  # cost for prelast and last step
    for i in range(2, len(cost) + 1):
        a, b = b, min(a + cost[i - 2], b + cost[i - 1])
    return b


def rob(nums: List[int]) -> int:
    """
    You are a professional robber planning to rob houses along a street. Each house has a
    certain amount of money stashed, the only constraint stopping you from robbing each of
    them is that adjacent houses have security systems connected and it will automatically
    contact the police if two adjacent houses were broken into on the same night. Given an
    integer array nums representing the amount of money of each house, return the maximum
    amount of money you can rob tonight without alerting the police.
    [MEDIUM] https://leetcode.com/problems/house-robber/

    >>> rob([1,2,3,1])
    4
    >>> rob([2,7,9,3,1])
    12
    >>> rob([2,1,1,2])
    4
    """
    prelast, last = 0, 0
    for n in nums:
        prelast, last = last, max(prelast + n, last)
    return last


def rob2(nums: List[int]) -> int:
    """
    As a professional robber planning to rob houses along a street arranged in a circle, each
    house has a certain amount of money stashed. Adjacent houses have security systems that
    automatically contact the police if both are broken into on the same night. Given an
    integer array nums representing the amount of money of each house, return the maximum
    amount of money you can rob tonight without alerting the police.
    [MEDIUM] https://leetcode.com/problems/house-robber-ii/

    >>> rob2([2,3,2])
    3
    >>> rob2([1,2,3,1])
    4
    >>> rob2([1,2,3])
    3
    """
    return max(rob(nums[1:]), rob(nums[:-1]))


def longest_palindromic_substring(s: str) -> str:
    """
    Given a string s, return the longest palindromic substring in s. A palindrome is a
    word, phrase, number, or other sequence of characters that reads the same forward and
    backward (ignoring spaces, punctuation, and capitalization).
    [MEDIUM] https://leetcode.com/problems/longest-palindromic-substring/

    >>> longest_palindromic_substring("babad")
    'bab'
    >>> longest_palindromic_substring("cbbd")
    'bb'
    >>> longest_palindromic_substring("abababa")
    'abababa'
    >>> longest_palindromic_substring("abaaba")
    'abaaba'
    >>> longest_palindromic_substring("a")
    'a'
    """
    longest = ""
    for i in range(len(s)):
        # odd number of letters
        for n in range(0, min(i + 1, len(s) - i)):
            if s[i - n] != s[i + n]:
                break
            if 2 * n + 1 > len(longest):
                longest = s[i - n:i + n + 1]
        # even number of letters
        for n in range(1, min(i, len(s) - i) + 1):
            if s[i - n] != s[i + n - 1]:
                break
            if 2 * n > len(longest):
                longest = s[i - n:i + n]

    return longest


if __name__ == "__main__":
    import doctest

    doctest.testmod()
