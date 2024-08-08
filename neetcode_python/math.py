from select import select
from typing import *


def rotate_image(matrix: List[List[int]]) -> None:
    """
    You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
    You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
    DO NOT allocate another 2D matrix and do the rotation.
    [MEDIUM] https://leetcode.com/problems/rotate-image/

    >>> img = [[1,2,3],[4,5,6],[7,8,9]]
    >>> rotate_image(img)
    >>> img
    [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

    >>> img = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    >>> rotate_image(img)
    >>> img
    [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]
    """
    last = len(matrix) - 1
    for i in range(len(matrix) // 2):
        for j in range(i, last - i):
            temp, matrix[j][last - i] = matrix[j][last - i], matrix[i][j]  # up to right
            temp, matrix[last - i][last - j] = matrix[last - i][last - j], temp  # right to bottom
            temp, matrix[last - j][i] = matrix[last - j][i], temp  # bottom to left
            matrix[i][j] = temp  # left to up


def spiral_matrix(matrix: List[List[int]]) -> List[int]:
    """
    Given an m x n matrix, return all elements of the matrix in spiral order.
    [MEDIUM] https://leetcode.com/problems/spiral-matrix/

    >>> spiral_matrix([[1,2,3],[4,5,6],[7,8,9]])
    [1, 2, 3, 6, 9, 8, 7, 4, 5]
    >>> spiral_matrix([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
    [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
    """
    right, down, left, up = (0, 1), (1, 0), (0, -1), (-1, 0)
    i, j, step = 0, 0, right
    i_min, i_max, j_min, j_max = 1, len(matrix) - 1, 0, len(matrix[0]) - 1

    vals = []
    for _ in range(len(matrix) * len(matrix[0])):
        if step == right and j + step[1] > j_max:
            step = down
            j_max -= 1
        elif step == down and i + step[0] > i_max:
            step = left
            i_max -= 1
        elif step == left and j + step[1] < j_min:
            step = up
            j_min += 1
        elif step == up and i + step[0] < i_min:
            step = right
            i_min += 1

        vals.append(matrix[i][j])
        i, j = i + step[0], j + step[1]

    return vals


def set_zeroes(matrix: List[List[int]]) -> None:
    """
    Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's. You must do it in place.
    [MEDIUM] https://leetcode.com/problems/set-matrix-zeroes/

    >>> m = [[1,1,1],[1,0,1],[1,1,1]]
    >>> set_zeroes(m)
    >>> m
    [[1, 0, 1], [0, 0, 0], [1, 0, 1]]

    >>> m = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    >>> set_zeroes(m)
    >>> m
    [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]
    """
    zero_rows, zero_cols = set(), set()
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                zero_rows.add(i)
                zero_cols.add(j)

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i in zero_rows or j in zero_cols:
                matrix[i][j] = 0


def is_happy(n: int) -> bool:
    """
    Write an algorithm to determine if a number n is happy.

    A happy number is a number defined by the following process:
    * Starting with any positive integer, replace the number by the sum of the squares of its digits.
    * Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle
    which does not include 1.
    * Those numbers for which this process ends in 1 are happy.

    Return true if n is a happy number, and false if not.

    [EASY] https://leetcode.com/problems/happy-number/

    >>> is_happy(19)
    True
    >>> is_happy(2)
    False
    """
    for _ in range(7):
        temp = 0
        while n != 0:
            temp += (n % 10) ** 2
            n //= 10
        if temp == 1:
            return True
        n = temp

    return False


def plus_one(digits: List[int]) -> List[int]:
    """
    You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the
    integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer
    does not contain any leading 0's.

    Increment the large integer by one and return the resulting array of digits.

    [EASY] https://leetcode.com/problems/plus-one/

    >>> plus_one([1,2,3])
    [1, 2, 4]
    >>> plus_one([4,3,2,1])
    [4, 3, 2, 2]
    >>> plus_one([9])
    [1, 0]
    """
    for i in reversed(range(len(digits))):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0

    return [1] + digits


def my_pow(x: float, n: int) -> float:
    """
    Implement pow(x, n), which calculates x raised to the power n (i.e., x^n).

    [MEDIUM] https://leetcode.com/problems/powx-n/

    >>> my_pow(2.00000, 10)
    1024.0
    >>> round(my_pow(2.10000, 3), 5)
    9.261
    >>> my_pow(2.00000, -2)
    0.25
    """
    if n == 0:
        return 1
    if n < 0:
        x = 1 / x
        n *= - 1
    if n % 2 == 1:
        return x * my_pow(x, n - 1)
    num = my_pow(x, n // 2)
    return num * num


if __name__ == "__main__":
    import doctest

    doctest.testmod()
