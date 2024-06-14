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


if __name__ == "__main__":
    import doctest

    doctest.testmod()
