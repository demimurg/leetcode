import heapq
from typing import *
from collections import *


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


def network_delay_time(times: List[List[int]], n: int, k: int) -> int:
    """
    You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed
    edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a
    signal to travel from source to target.

    We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal.
    If it is impossible for all the n nodes to receive the signal, return -1.

    [MEDIUM] https://leetcode.com/problems/network-delay-time/

    >>> network_delay_time([[2,1,1],[2,3,1],[3,4,1]], 4, 2)
    2
    >>> network_delay_time([[1,2,1]], 2, 1)
    1
    >>> network_delay_time([[1,2,1]], 2, 2)
    -1
    """
    delays = {}
    for (a, b, delay) in times:
        if a not in delays:
            delays[a] = []
        delays[a].append([b, delay])

    paths = [[0, k]]  # complete delay to achive node
    to_visit = set(i for i in range(1, n + 1))
    network_delay = 0
    while paths and to_visit:
        delay, node = heapq.heappop(paths)
        if node not in to_visit:
            continue
        to_visit.remove(node)
        network_delay = max(network_delay, delay)

        for child_node, child_delay in delays.get(node, []):
            if child_node in to_visit:
                heapq.heappush(paths, [delay + child_delay, child_node])

    return network_delay if len(to_visit) == 0 else -1


if __name__ == "__main__":
    import doctest

    doctest.testmod()
