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


def solve(board: List[List[str]]) -> None:
    """
    Modify the given m x n matrix 'board' by flipping all regions that are fully surrounded by 'X'. A region
    is considered captured and flipped from 'O' to 'X' if all 'O's in that region are surrounded by 'X' vertically
    and horizontally. 'O's on the border connected to other 'O's directly or indirectly are not flipped.
    [MEDIUM] https://leetcode.com/problems/surrounded-regions/

    >>> board = [['X', 'X', 'X', 'X'], ['X', 'O', 'O', 'X'],['X', 'X', 'O', 'X'],['X', 'O', 'X', 'X']]
    >>> solve(board)
    >>> board
    [['X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X'], ['X', 'O', 'X', 'X']]
    >>> board = [['X']]
    >>> solve(board)
    >>> board
    [['X']]
    """
    rows, cols = len(board), len(board[0])

    def mark_dfs(r: int, c: int):
        if not 0 <= r < rows or not 0 <= c < cols or board[r][c] != "O":
            return
        board[r][c] = "OO"
        mark_dfs(r + 1, c)
        mark_dfs(r, c + 1)
        mark_dfs(r - 1, c)
        mark_dfs(r, c - 1)

    for c in range(cols):
        mark_dfs(0, c)
        mark_dfs(rows - 1, c)
    for r in range(rows):
        mark_dfs(r, 0)
        mark_dfs(r, cols - 1)

    for r in range(rows):
        for c in range(cols):
            if board[r][c] == "O":
                board[r][c] = "X"
            elif board[r][c] == "OO":
                board[r][c] = "O"


def oranges_rotting(grid: List[List[int]]) -> int:
    """
    In a given m x n grid, each cell can be empty (0), contain a fresh orange (1), or
    contain a rotten orange (2). Each minute, any fresh orange that is 4-directionally
    adjacent to a rotten orange will become rotten. This function returns the minimum
    number of minutes that must elapse until no cell has a fresh orange, or -1 if this
    is impossible.
    [MEDIUM] https://leetcode.com/problems/rotting-oranges/

    >>> oranges_rotting([[2,1,1],[1,1,0],[0,1,1]])
    4
    >>> oranges_rotting([[2,1,1],[0,1,1],[1,0,1]])
    -1
    >>> oranges_rotting([[0,2]])
    0
    """
    rows, cols = len(grid), len(grid[0])
    fresh = 0
    que = deque([])

    # add all roting oranges to first traverse level and count fresh fruits
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                que.append((r, c))
            elif grid[r][c] == 1:
                fresh += 1

    # each minute mark rotting neighbors, stop when que will be empty
    mins = -1
    directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
    level_size = len(que)
    while len(que) > 0:
        (r, c) = que.popleft()
        level_size -= 1

        for dr, dc in directions:
            row, col = r + dr, c + dc
            if 0 <= row < rows and 0 <= col < cols and grid[row][col] == 1:
                fresh -= 1
                grid[row][col] = 2
                que.append((row, col))

        if level_size == 0:
            level_size = len(que)
            mins += 1
    if fresh > 0:
        return -1

    return mins if mins > 0 else 0


def can_finish(num_courses: int, prerequisites: List[List[int]]) -> bool:
    """
    Determines if it's possible to finish all courses given the total number of courses and a list
    of prerequisite pairs. Each pair [a, b] indicates that course a cannot be taken until course b
    has been completed. This function returns true if it is possible to finish all courses, otherwise
    false.
    [MEDIUM] https://leetcode.com/problems/course-schedule/

    >>> can_finish(2, [[1,0]])
    True
    >>> can_finish(2, [[1,0], [0,1]])
    False
    """
    prereq: Dict[int, List[int]] = {}
    for [course, must_get] in prerequisites:
        if course not in prereq:
            prereq[course] = []
        prereq[course].append(must_get)

    visit = set()

    def find_loop(course: int) -> bool:
        if course in visit:
            return True
        if not prereq.get(course, []):
            return False
        visit.add(course)

        for pre_course in prereq[course]:
            ok = find_loop(pre_course)
            if ok:
                return True

        visit.remove(course)
        prereq[course] = []
        return False

    for course in prereq.keys():
        ok = find_loop(course)
        if ok:
            return False

    return True


def find_order(num_courses: int, prerequisites: List[List[int]]) -> List[int]:
    """
    There are a total of num_courses you have to take, labeled from 0 to num_courses - 1.
    You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that to
    take course ai you must first take course bi. For example, the pair [0, 1], indicates
    that to take course 0 you must first take course 1. Return the ordering of courses you
    should take to finish all courses. If there are many valid answers, return any of them.
    If it is impossible to finish all courses, return an empty array.
    [MEDIUM] https://leetcode.com/problems/course-schedule-ii/

    >>> find_order(2, [[1,0]])
    [0, 1]
    >>> find_order(4, [[1,0],[2,0],[3,1],[3,2]])
    [0, 1, 2, 3]
    >>> find_order(1, [])
    [0]
    """
    prereq: Dict[int, List[int]] = {}
    for course, pre in prerequisites:
        if course not in prereq:
            prereq[course] = []
        prereq[course].append(pre)

    ordered, ordered_set = [], set()

    def dfs(course: int, i: int = 0) -> bool:
        if i > num_courses:
            return False
        if course in ordered_set:
            return True

        for pre in prereq.get(course, []):
            if not dfs(pre, i + 1):
                return False

        ordered.append(course)
        ordered_set.add(course)
        return True

    for course in range(num_courses):
        if not dfs(course):
            return []

    return ordered


def find_redundant_connection(edges: List[List[int]]) -> List[int]:
    """
    In this problem, we have an undirected graph that is connected and has no cycles. We need to
    find an edge that can be removed so that the resulting graph is still connected. This graph
    started as a tree with nodes labeled from 1 to n, and an additional edge was added. If there
    are multiple answers, we return the edge that occurs last in the input.
    [MEDIUM] https://leetcode.com/problems/redundant-connection/

    >>> find_redundant_connection([[1,2], [1,3], [2,3]])
    [2, 3]
    >>> find_redundant_connection([[1,2], [2,3], [3,4], [1,4], [1,5]])
    [1, 4]
    """
    parent = [n for n in range(len(edges) + 1)]
    childrens: Dict[int, int] = defaultdict(lambda: 1)

    def get_parent(n: int) -> int:
        while n != parent[n]:
            n = parent[n]
        return n

    for (n1, n2) in edges:
        p1, p2 = get_parent(n1), get_parent(n2)
        if p1 == p2:
            # this edge will create cycle
            return [n1, n2]
        if childrens[p2] > childrens[p1]:
            # we always add smaller tree to bigger
            p1, p2 = p2, p1
        parent[p2] = p1
        childrens[p1] += childrens[p2]

    return []


def find_redundant_connection_dfs(edges: List[List[int]]) -> List[int]:
    node2node: Dict[int, List[int]] = defaultdict(list)

    def is_connected(a: int, b: int, skip: int = -1) -> bool:
        if a == b:
            return True
        for a_neighbor in node2node.get(a, []):
            if a_neighbor != skip and is_connected(a_neighbor, b, skip=a):
                return True
        return False

    for edge in edges:
        if is_connected(edge[0], edge[1]):
            # it will be loop if they already connected
            return edge
        node2node[edge[0]].append(edge[1])
        node2node[edge[1]].append(edge[0])

    return []


def islands_and_treasure(grid: List[List[int]]) -> None:
    """
    You are given a m x n 2D grid initialized with these three possible values:
    -1: A water cell that can not be traversed.
    0: A treasure chest.
    INF: A land cell that can be traversed (represented by 2^31 - 1 = 2147483647).

    Fill each land cell with the distance to its nearest treasure chest. If a land cell cannot
    reach a treasure chest, the value should remain INF. The grid can only be traversed up,
    down, left, or right.

    [MEDIUM] https://leetcode.com/problems/islands-and-treasure/

    >>> grid = [
    ...    [2147483647, -1, 0, 2147483647],
    ...    [2147483647, 2147483647, 2147483647, -1],
    ...    [2147483647, -1, 2147483647, -1],
    ...    [0, -1, 2147483647, 2147483647]
    ... ]
    >>> islands_and_treasure(grid)
    >>> grid
    [[3, -1, 0, 1],
     [2, 2, 1, -1],
     [1, -1, 2, -1],
     [0, -1, 3, 4]]
    """
    que = deque([])
    for m in range(len(grid)):
        for n in range(len(grid[0])):
            if grid[m][n] == 0:
                que.append((m, n))

    inf = 2 ^ 32 - 1
    directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
    distance, left = 0, 0
    while que:
        if left == 0:
            left = len(que)
            distance += 1

        (m, n) = que.popleft()
        left -= 1
        for (dm, dn) in directions:
            new_m, new_n = m + dm, n + dn
            is_valid = 0 <= new_m < len(grid) and \
                       0 <= new_n < len(grid[0]) and \
                       grid[new_m][new_n] == inf
            if is_valid:
                grid[new_m][new_n] = distance
                que.append((new_m, new_n))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
