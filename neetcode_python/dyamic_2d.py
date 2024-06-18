from typing import *


def unique_paths(m: int, n: int) -> int:
    """
    There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot
    tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any
    point in time.

    Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-
    right corner.

    [MEDIUM] https://leetcode.com/problems/unique-paths/

    >>> unique_paths(3, 7)
    28
    >>> unique_paths(3, 2)
    3
    """
    # count unique paths for each cell from bottom to up, using 2 rows
    first, second = [1] * m, [1] * m
    # don't use last row and last column, because they always have one path
    for _ in range(n - 1):
        for i in range(m - 2, -1, -1):
            second[i] = first[i] + second[i + 1]
        # reuse memory by swapping rows
        second, first = first, second
    return first[0]
    # return math.comb(m + n - 2, m - 1) we can use mathematical approach too


def longest_common_subsequence(text1: str, text2: str) -> int:
    """
    Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common
    subsequence, return 0.
    A subsequence of a string is a new string generated from the original string with some characters (can be none)
    deleted without changing the relative order of the remaining characters.
    A common subsequence of two strings is a subsequence that is common to both strings.
    [MEDIUM] https://leetcode.com/problems/longest-common-subsequence/

    >>> longest_common_subsequence('abcde', 'ace')
    3
    >>> longest_common_subsequence('abc', 'abc')
    3
    >>> longest_common_subsequence('abc', 'def')
    0
    """
    if len(text1) < len(text2):
        text2, text1 = text1, text2

    row_size = len(text2) + 1  # last column will be always zero
    first, second = [0] * row_size, [0] * row_size
    for i in range(len(text1) - 1, -1, -1):
        for j in range(len(text2) - 1, -1, -1):
            if text1[i] == text2[j]:
                first[j] = 1 + second[j + 1]  # diagonal shift
            else:
                first[j] = max(second[j], first[j + 1])  # max from bottom and right
        first, second = second, first
    return second[0]


def max_profit(prices: List[int]) -> int:
    """
    You are given an array prices where prices[i] is the price of a given stock on the ith day.
    Find the maximum profit you can achieve. You may complete as many transactions as you like
    (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:
    - After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
    Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock
    before you buy again).

    [MEDIUM] https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

    >>> max_profit([1, 2, 3, 0, 2])
    3
    >>> max_profit([1])
    0
    >>> max_profit([1,2,4])
    3
    """
    memo = {}

    def dfs(i: int, buying: bool) -> int:
        if i >= len(prices):
            return 0
        if (i, buying) in memo:
            return memo[(i, buying)]

        cooldown = dfs(i + 1, buying)
        if buying:
            buy = dfs(i + 1, buying=False) - prices[i]
            memo[(i, buying)] = max(buy, cooldown)
        else:
            sell = dfs(i + 2, buying=True) + prices[i]
            memo[(i, buying)] = max(sell, cooldown)
        return memo[(i, buying)]

    return dfs(0, buying=True)


def max_profit_2(prices: List[int]) -> int:
    sell, buy, cooldown = -1001, -1001, 0

    for price in prices:
        sell, buy, cooldown = (
            buy + price,  # profit after selling stock held
            max(buy, cooldown - price),  # max of holding or buying stock
            max(sell, cooldown)  # max of being in cooldown or not holding stock
        )

    return max(sell, cooldown)


def change(amount: int, coins: List[int]) -> int:
    """
    You are given an integer array coins representing coins of different denominations and an integer amount
    representing a total amount of money.

    Return the number of combinations that make up that amount. If that amount of money cannot be made up by any
    combination of the coins, return 0.

    You may assume that you have an infinite number of each kind of coin.

    The answer is guaranteed to fit into a signed 32-bit integer.

    [MEDIUM] https://leetcode.com/problems/coin-change-ii/

    >>> change(5, [1, 2, 5])
    4
    >>> change(3, [2])
    0
    >>> change(10, [10])
    1
    """
    dp = [1] + [0] * amount
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] += dp[i - coin]

    return dp[amount]


def change_bruteforce(total_amount: int, coins: List[int]) -> int:
    memo = {}

    def dfs(amount: int, i: int) -> int:
        if amount == 0:
            return 1
        if (amount, i) in memo:
            return memo[(amount, i)]

        combinations = 0
        for j in range(i, len(coins)):
            next_amount = amount - coins[j]
            if next_amount < 0:
                continue
            combinations += dfs(next_amount, j)
        memo[(amount, i)] = combinations
        return combinations

    return dfs(total_amount, 0)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
