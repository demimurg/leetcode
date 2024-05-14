import heapq
import math
from typing import *


class Heap:
    def __init__(self, is_max=True, lis=[]):
        self.storage = []
        # x before y, if x biggen than y for max_heap
        self.before = lambda x, y: x > y
        if not is_max:
            # x before y, if x less than y for min_heap
            self.before = lambda x, y: x < y
        for val in lis:
            self.add(val)

    def __len__(self):
        return len(self.storage)

    def add(self, val):
        self.storage.append(val)
        self.heapify_up()

    def get_top(self):
        if len(self.storage) == 0:
            return None
        return self.storage[0]

    def pop_top(self):
        if len(self.storage) == 0:
            return None
        if len(self.storage) == 1:
            return self.storage.pop()
        top = self.storage[0]
        self.storage[0] = self.storage.pop()
        self.heapify_down()

        return top

    # left = 2n+1, right = 2n+2
    def heapify_up(self):
        i = len(self.storage) - 1
        while i != 0:
            parent_i = (i - 1) // 2
            if not self.before(self.storage[i], self.storage[parent_i]):
                return
            self.storage[i], self.storage[parent_i] = self.storage[parent_i], self.storage[i]
            i = parent_i

    def heapify_down(self):
        i = 0
        while 2 * i + 1 < len(self.storage):
            child_i = 2 * i + 1  # left child
            if child_i + 1 < len(self.storage) and self.before(self.storage[child_i + 1], self.storage[child_i]):
                # right child
                child_i += 1
            if self.before(self.storage[i], self.storage[child_i]):
                return
            self.storage[i], self.storage[child_i] = self.storage[child_i], self.storage[i]
            i = child_i


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = Heap(is_max=False)
        for num in nums:
            self.heap.add(num)
        while len(self.heap) > k:
            self.heap.pop_top()

    def add(self, val: int) -> int:
        self.heap.add(val)
        if len(self.heap) > self.k:
            return self.heap.pop_top()
        return self.heap.get_top()


def last_stone_weight(stones: List[int]) -> int:
    """
    You are given an array of integers stones where stones[i] is the weight of the ith stone. We are playing a game with
    the stones. On each turn, we choose the heaviest two stones and smash them together. Suppose the two stones have
    weights x and y with x <= y. The smash results as follows: If x == y, both stones are destroyed; If x != y, the
    stone of weight x is destroyed, and the stone of weight y has new weight y - x. At the end of the game, at most one
    stone is left. Return the weight of the last remaining stone. If there are no stones left, return 0.
    [EASY] https://leetcode.com/problems/last-stone-weight/

    >>> last_stone_weight([2,7,4,1,8,1])
    1
    >>> last_stone_weight([1])
    1
    """
    for i in range(len(stones)):
        stones[i] *= -1
    heapq.heapify(stones)
    while len(stones) > 1:
        a, b = -heapq.heappop(stones), -heapq.heappop(stones)
        if a == b:
            continue
        heapq.heappush(stones, -1 * (a - b))

    return -stones.pop() if len(stones) > 0 else 0


def k_closest(points: List[List[int]], k: int) -> List[List[int]]:
    """
    Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k,
    return the k closest points to the origin (0, 0). The distance between two points on the X-Y plane is the
    Euclidean distance (i.e., sqrt((x1 - x2)^2 + (y1 - y2)^2)). The answer is guaranteed to be unique and may
    be returned in any order.
    [MEDIUM] https://leetcode.com/problems/k-closest-points-to-origin/

    >>> k_closest([[1,3], [-2,2]], 1)
    [[-2, 2]]
    >>> k_closest([[0,1],[1,0]], 2)
    [[0,1], [1,0]]
    """
    distances = [(math.sqrt(x ** 2 + y ** 2), x, y) for x, y in points]
    heapq.heapify(distances)

    k_points = [[0, 0] for _ in range(k)]
    for i in range(k):
        closest_dist, x, y = heapq.heappop(distances)
        k_points[i] = ([x, y])
    return k_points


if __name__ == "__main__":
    import doctest

    doctest.testmod()
