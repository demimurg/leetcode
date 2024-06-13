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


if __name__ == "__main__":
    import doctest

    doctest.testmod()
