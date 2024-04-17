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


class Node:
    def __init__(self, val: int, neighbors: List['Node'] = None):
        if neighbors is None:
            neighbors = []
        self.val = val
        self.neighbors = neighbors


def clone_graph(node: Optional[Node]) -> Optional[Node]:
    """
    Creates a deep copy of a connected undirected graph. Each node in the graph has a value and a list
    of neighbors. This function returns a clone of the graph given a reference to one of its nodes.
    The node values are unique and are the same as the node's index (1-indexed).
    [MEDIUM] https://leetcode.com/problems/clone-graph/
    """
    old_to_new = {}

    def copy_dfs(node: Node) -> Node:
        if node in old_to_new:
            return old_to_new[node]

        copy = Node(val=node.val)
        old_to_new[node] = copy
        for neighbor in node.neighbors:
            copy.neighbors.append(copy_dfs(neighbor))

        return copy

    return copy_dfs(node) if node else None


def max_area_of_island(grid: List[List[int]]) -> int:
    """
    Given a binary matrix where '1' represents land and '0' represents water, identify the maximum area of
    an island in the grid. An island is comprised of adjacent '1's, connected horizontally or vertically.
    The grid is bordered by water on all edges. The area of an island is the count of '1's forming that
    island. The function returns the largest island area in the grid, or 0 if there are no islands.
    [MEDIUM] https://leetcode.com/problems/max-area-of-island/

    >>> max_area_of_island([
    ...     [0,0,1,0,0,0,0,1,0,0,0,0,0],
    ...     [0,0,0,0,0,0,0,1,1,1,0,0,0],
    ...     [0,1,1,0,1,0,0,0,0,0,0,0,0],
    ...     [0,1,0,0,1,1,0,0,1,0,1,0,0],
    ...     [0,1,0,0,1,1,0,0,1,1,1,0,0],
    ...     [0,0,0,0,0,0,0,0,0,0,1,0,0],
    ...     [0,0,0,0,0,0,0,1,1,1,0,0,0],
    ...     [0,0,0,0,0,0,0,1,1,0,0,0,0]
    ... ])
    6
    >>> max_area_of_island([
    ...     [0,0,0,0,0,0,0,0]
    ... ])
    0
    """
    if len(grid) == 0:
        return 0

    rows, cols = len(grid), len(grid[0])
    directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
    que = deque()
    biggest_island = 0

    def mark_island(cur_r: int, cur_c: int) -> None:
        grid[cur_r][cur_c] = 0
        que.append((cur_r, cur_c))

        current_island = 0
        while len(que) > 0:
            (cur_r, cur_c) = que.popleft()
            current_island += 1

            for (delta_r, delta_c) in directions:
                new_r, new_c = cur_r + delta_r, cur_c + delta_c
                if 0 <= new_r < rows and 0 <= new_c < cols and grid[new_r][new_c] == 1:
                    grid[new_r][new_c] = 0
                    que.append((new_r, new_c))

        nonlocal biggest_island
        biggest_island = max(biggest_island, current_island)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                mark_island(r, c)

    return biggest_island


if __name__ == "__main__":
    import doctest

    doctest.testmod()
