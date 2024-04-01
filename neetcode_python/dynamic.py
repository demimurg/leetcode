from typing import List


def climb_stairs(n: int) -> int:
    """
    You are climbing a staircase with n steps to reach the top. Each time you can climb 1 or 2 steps. 
    The function calculates how many distinct ways you can climb to the top.
    [EASY] https://leetcode.com/problems/climbing-stairs/

    >>> climb_stairs(2)
    2
    >>> climb_stairs(3)
    3
    """
    if n <= 2:
        return n

    prelast, last = 1, 2
    for _ in range(n - 2):
        prelast, last = last, prelast + last
    return last


def min_cost_climbing_stairs(cost: List[int]) -> int:
    """
    Given a staircase where the ith step has a non-negative cost associated with it represented by the array cost[],
    we can climb one or two steps at a time. The goal is to find the minimum cost to reach the top of the staircase
    starting from either the first step or the second step. We pay the cost of a step before climbing it. After paying,
    we can either climb one step or two steps. The top of the staircase is beyond the last step.
    [EASY] https://leetcode.com/problems/min-cost-climbing-stairs/

    >>> min_cost_climbing_stairs([10, 15, 20])
    15
    >>> min_cost_climbing_stairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1])
    6
    """
    a, b = 0, 0  # cost for prelast and last step
    for i in range(2, len(cost) + 1):
        a, b = b, min(a + cost[i - 2], b + cost[i - 1])
    return b


if __name__ == "__main__":
    import doctest

    doctest.testmod()
