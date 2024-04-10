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


def count_palindromic_substrings(s: str) -> int:
    """
    Given a string s, return the number of palindromic substrings in it. A substring is
    palindromic if it reads the same backward as forward, and a substring is a contiguous
    sequence of characters within the string.
    [MEDIUM] https://leetcode.com/problems/palindromic-substrings/

    >>> count_palindromic_substrings("abc")
    3
    >>> count_palindromic_substrings("aaa")
    6
    """
    count = 0
    for i in range(len(s)):
        # odd number of letters
        for n in range(0, min(i + 1, len(s) - i)):
            if s[i - n] != s[i + n]:
                break
            count += 1
        # even number of letters
        for n in range(1, min(i, len(s) - i) + 1):
            if s[i - n] != s[i + n - 1]:
                break
            count += 1

    return count


def num_decodings(s: str) -> int:
    """
    A message containing letters from A-Z can be encoded into numbers using a given mapping where 'A' -> "1",
    'B' -> "2", ..., 'Z' -> "26". To decode an encoded message, all the digits must be grouped then mapped back into
    letters using the reverse of the mapping (there may be multiple ways). For example, "11106" can be decoded into
    "AAJF" with the grouping (1 1 10 6) or "KJF" with the grouping (11 10 6). Note that grouping like (1 11 06)
    is invalid because "06" cannot be mapped into 'F'since "6" is different from "06".
    Given a string s containing only digits, return the number of ways to decode it.
    [MEDIUM] https://leetcode.com/problems/decode-ways/

    >>> num_decodings("12")
    2
    >>> num_decodings("226")
    3
    >>> num_decodings("06")
    0
    """
    # num decodings plus one and two for current index
    plus_one, plus_two = 1, 1
    # iterate from the end
    for i in range(len(s) - 1, -1, -1):
        if s[i] == "0":
            plus_one, plus_two = 0, plus_one
        elif i < len(s) - 1 and (s[i] == "1" or (s[i] == "2" and int(s[i + 1]) < 7)):
            # combination of two digits added
            plus_one, plus_two = plus_one + plus_two, plus_one
        else:
            # same number of combinations as before
            plus_two = plus_one

    # we end on -1 index, so plus one will be zero
    return plus_one


def coin_change(coins: List[int], amount: int) -> int:
    """
    You are given an integer array coins representing coins of different denominations and an integer
    amount representing a total amount of money. Return the fewest number of coins that you need to
    make up that amount. If that amount of money cannot be made up by any combination of the coins,
    return -1. You may assume that you have an infinite number of each kind of coin.
    [MEDIUM] https://leetcode.com/problems/coin-change/

    >>> coin_change([1, 2, 5], 11)
    3
    >>> coin_change([2], 3)
    -1
    """
    min_change = {0: 0}
    for n in range(1, amount + 1):
        for coin in coins:
            min_last = min_change.get(n - coin, 0)
            if min_last == 0 and coin != n:
                # can't add to another coins and can't start from it
                continue
            if min_last + 1 < min_change.get(n, 1e6):
                min_change[n] = min_last + 1

    return min_change.get(amount, -1)


def max_product(nums: List[int]) -> int:
    """
    Given an integer array 'nums', find a subarray that has the largest product, and return the product.
    The function assumes that the answer will fit in a 32-bit integer.
    [MEDIUM] https://leetcode.com/problems/maximum-product-subarray/

    # [2, 3, -2, 4]
    # 2, min=

    >>> max_product([2,3,-2,4])
    6
    >>> max_product([-2,0,-1])
    0
    """
    result, cur_min, cur_max = -1e6, 1, 1
    for n in nums:
        vals = (cur_max * n, cur_min * n, n)
        cur_min, cur_max = min(vals), max(vals)
        result = max(result, cur_max)

    return result


def word_break(s: str, word_dict: List[str]) -> bool:
    """
    Given a string 's' and a dictionary of strings 'word_dict', return 'true' if 's' can be segmented
    into a space-separated sequence of one or more dictionary words. It's noted that the same word
    in the dictionary may be reused multiple times in the segmentation.
    [MEDIUM] https://leetcode.com/problems/word-break/

    >>> word_break("leetcode", ["leet", "code"])
    True
    >>> word_break("applepenapple", ["apple", "pen"])
    True
    >>> word_break("catsandog", ["cats", "dog", "sand", "and", "cat"])
    False
    """
    have_solution = {len(s): True}  # key = index, value = is solution found
    for i in range(len(s) - 1, -1, -1):  # up-down
        for word in word_dict:
            if have_solution.get(i + len(word), False) and s.startswith(word, i):
                have_solution[i] = True
                break
    return have_solution.get(0, False)


def length_of_lis(nums: List[int]) -> int:
    """
    Given an integer array 'nums', return the length of the longest strictly increasing subsequence.
    The function defines a subsequence as a sequence that can be derived from an array by deleting
    some or no elements without changing the order of the remaining elements.
    [MEDIUM] https://leetcode.com/problems/longest-increasing-subsequence/

    >>> length_of_lis([10,9,2,5,3,7,101,18])
    4
    >>> length_of_lis([0,1,0,3,2,3])
    4
    >>> length_of_lis([7,7,7,7,7,7,7])
    1
    """
    seq_len = [1] * len(nums)  # max sequence length for each nums index
    for i in reversed(range(len(nums))):
        for j in range(i + 1, len(nums)):
            if nums[j] > nums[i]:
                seq_len[i] = max(seq_len[i], 1 + seq_len[j])

    return max(seq_len)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
