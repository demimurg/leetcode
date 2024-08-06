from select import select
from typing import *


def rotate_image(matrix: List[List[int]]) -> None:
    """
    You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
    You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
    DO NOT allocate another 2D matrix and do the rotation.
    [MEDIUM] https://leetcode.com/problems/rotate-image/

    >>> rotate_image([[1,2,3],[4,5,6],[7,8,9]]) # [[7,4,1],[8,5,2],[9,6,3]]
    >>> rotate_image([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]) # [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
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


if __name__ == "__main__":
    import doctest

    doctest.testmod()
