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


def pacific_atlantic(heights: List[List[int]]) -> List[List[int]]:
    """
    Given an m x n matrix of integers where each value represents the height above sea level,
    the task is to find the coordinates from which water can flow to both the Pacific and Atlantic
    Oceans. Water can flow from any cell to another cell with height less or equal to its own. The
    Pacific Ocean touches the left and top edges of the matrix, while the Atlantic is on the right
    and bottom edges.
    [MEDIUM] https://leetcode.com/problems/pacific-atlantic-water-flow/

    >>> pacific_atlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]])
    [[4, 0], [0, 4], [3, 1], [1, 4], [3, 0], [2, 2], [1, 3]]
    >>> pacific_atlantic([[1]])
    [[0, 0]]
    """
    rows, cols = len(heights), len(heights[0])
    pacific, atlantic = set(), set()

    def dfs(r: int, c: int, seen: Set, prev: int):
        if not 0 <= r < rows or not 0 <= c < cols or \
                (r, c) in seen or heights[r][c] < prev:
            return
        seen.add((r, c))
        dfs(r + 1, c, seen, heights[r][c])
        dfs(r, c + 1, seen, heights[r][c])
        dfs(r - 1, c, seen, heights[r][c])
        dfs(r, c - 1, seen, heights[r][c])

    for col in range(cols):
        dfs(0, col, pacific, -1)
        dfs(rows - 1, col, atlantic, -1)
    for row in range(rows):
        dfs(row, 0, pacific, -1)
        dfs(row, cols - 1, atlantic, -1)

    return [[r, c] for (r, c) in pacific.intersection(atlantic)]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
