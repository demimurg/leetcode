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


def multiply_strings(num1: str, num2: str) -> str:
    """
    Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2,
    also represented as a string.

    Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

    [MEDIUM] https://leetcode.com/problems/multiply-strings/

    >>> multiply_strings('2', '3')
    '6'
    >>> multiply_strings('123', '456')
    '56088'
    """
    res, l1, l2 = 0, len(num1), len(num2)
    for i in range(l1):
        for j in range(l2):
            res += (ord(num1[l1 - 1 - i]) - ord("0")) * \
                   (ord(num2[l2 - 1 - j]) - ord("0")) * \
                   (10 ** (i + j))
    return str(res)


class DetectSquares:
    """
    A data structure to track points on the X-Y plane and count the number of axis-aligned squares that can be formed.

    The class supports two operations:
    1. `add(point: List[int]) -> None`: Adds a new point [x, y] to the data structure. Duplicate points are allowed
       and should be treated as different points.
    2. `count(point: List[int]) -> int`: Counts the number of ways to choose three points from the data structure such that the
       three points and the query point form an axis-aligned square with positive area.

    Example usage:
    >>> ds = DetectSquares()
    >>> ds.add([3, 10])
    >>> ds.add([11, 2])
    >>> ds.add([3, 2])
    >>> ds.count([11, 10])
    1
    >>> ds.count([14, 8])
    0
    >>> ds.add([11, 2])
    >>> ds.count([11, 10])
    2

    [MEDIUM] https://leetcode.com/problems/detect-squares/
    """
    grid: Dict[int, Dict[int, int]]

    def __init__(self):
        self.grid = dict()

    def add(self, point: List[int]) -> None:
        x, y = point
        if x not in self.grid:
            self.grid[x] = {}
        if y not in self.grid[x]:
            self.grid[x][y] = 0
        self.grid[x][y] += 1

    def exists(self, x: int, y: int) -> bool:
        return x in self.grid and y in self.grid[x]

    def count(self, point: List[int]) -> int:
        squares = 0

        x, y = point[0], point[1]
        for y2 in self.grid.get(x, []):
            delta = abs(y2 - y)
            if delta == 0:
                continue

            if self.exists(x + delta, y) and self.exists(x + delta, y2):
                squares += self.grid[x + delta][y] * self.grid[x + delta][y2] * self.grid[x][y2]
            if self.exists(x - delta, y) and self.exists(x - delta, y2):
                squares += self.grid[x - delta][y] * self.grid[x - delta][y2] * self.grid[x][y2]

        return squares


def encode(strs: List[str]) -> str:
    """
    Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded
    back to the original list of strings.
    [MEDIUM] https://leetcode.com/problems/encode-and-decode-strings/

    >>> encode(['neet', 'code', 'love', 'you'])
    '4#neet4#code4#love3#you'
    >>> encode(['we', 'say', ':', 'yes'])
    '2#we3#say1#:3#yes'
    """
    for i in range(len(strs)):
        strs[i] = str(len(strs[i])) + "#" + strs[i]
    return "".join(strs)


def decode(s: str) -> List[str]:
    """
    Decodes the encoded string back to the original list of strings.

    >>> decode('4#neet4#code4#love3#you')
    ['neet', 'code', 'love', 'you']
    >>> decode('2#we3#say1#:3#yes')
    ['we', 'say', ':', 'yes']
    """
    result = []
    i = 0
    while i < len(s):
        size = 0
        while s[i] != "#":
            size = 10 * size + int(s[i])
            i += 1

        i += 1
        result.append(s[i:i + size])
        i += size

    return result


if __name__ == "__main__":
    import doctest

    doctest.testmod()
