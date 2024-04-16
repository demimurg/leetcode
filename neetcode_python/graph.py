from typing import *
from collections import *


def num_islands(grid: List[List[str]]) -> int:
    """
    Given an m x n 2D binary grid which represents a map of '1's (land) and '0's (water), return the number of islands.
    An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
    You may assume all four edges of the grid are all surrounded by water.
    [MEDIUM] https://leetcode.com/problems/number-of-islands/

    # >>> num_islands([
    # ...     ["1","1","1","1","0"],
    # ...     ["1","1","0","1","0"],
    # ...     ["1","1","0","0","0"],
    # ...     ["0","0","0","0","0"]
    # ... ])
    # 1
    # >>> num_islands([
    # ...     ["1","1","0","0","0"],
    # ...     ["1","1","0","0","0"],
    # ...     ["0","0","1","0","0"],
    # ...     ["0","0","0","1","1"]
    # ... ])
    # 3
    # >>> num_islands([
    # ...     ["1","1","1"],
    # ...     ["0","1","0"],
    # ...     ["1","1","1"],
    # ... ])
    # 1
    >>> num_islands([
    ...     ["1","0","1","1","1"],
    ...     ["1","0","1","0","1"],
    ...     ["1","1","1","0","1"],
    ... ])
    1
    """
    if len(grid) == 0:
        return 0

    rows, cols = len(grid), len(grid[0])
    directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
    que = deque()

    def mark_island(cur_r: int, cur_c: int) -> None:
        grid[cur_r][cur_c] = "0"
        que.append((cur_r, cur_c))

        while len(que) > 0:
            (cur_r, cur_c) = que.popleft()

            for (delta_r, delta_c) in directions:
                new_r, new_c = cur_r + delta_r, cur_c + delta_c
                if 0 <= new_r < rows and 0 <= new_c < cols and grid[new_r][new_c] == "1":
                    grid[new_r][new_c] = "0"
                    que.append((new_r, new_c))

    islands = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1":
                islands += 1
                mark_island(r, c)

    return islands


if __name__ == "__main__":
    import doctest

    doctest.testmod()
