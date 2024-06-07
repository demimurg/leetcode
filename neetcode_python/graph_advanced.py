import heapq
from typing import *


def min_cost_connect_points(points: List[List[int]]) -> int:
    """
    You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].
    The cost of connecting two points [xi, yi] and [xj, yj] is the Manhattan distance between them: |xi - xj| + |yi - yj|.
    Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path 
    between any two points.
    [MEDIUM] https://leetcode.com/problems/min-cost-to-connect-all-points/

    >>> min_cost_connect_points([[0,0],[2,2],[3,10],[5,2],[7,0]])
    20
    >>> min_cost_connect_points([[3,12],[-2,5],[-4,1]])
    18
    >>> min_cost_connect_points([[0,0],[1,1],[1,0],[-1,1]])
    4
    >>> min_cost_connect_points([[-1000000,-1000000],[1000000,1000000]])
    4000000
    >>> min_cost_connect_points([[0,0]])
    0
    """
    manh_dist = lambda i, j: abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
    to_visit = set(i for i in range(len(points)))
    edges, cost = [(0, 0)], 0

    # prim's algorithm
    while len(to_visit) > 0:
        dist, i = heapq.heappop(edges)
        if i not in to_visit:
            continue
        cost += dist
        to_visit.remove(i)

        for j in to_visit:
            heapq.heappush(edges, (manh_dist(i, j), j))
    return cost


if __name__ == "__main__":
    import doctest

    doctest.testmod()
