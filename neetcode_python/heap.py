import heapq
import math
from typing import *
from collections import defaultdict


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


class KthLarges2:
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


class KthLargest:
    """
    Design a class `KthLargest` that finds the `k`th largest element in a stream of integers.
    - `KthLargest(int k, int[] nums)` initializes the object with the integer `k` and the stream of integers `nums`.
    - `int add(int val)` appends the integer `val` to the stream and returns the element representing the `k`th largest element in the stream.

    [MEDIUM] https://leetcode.com/problems/kth-largest-element-in-a-stream/

    kthLargest = KthLargest(3, [4, 5, 8, 2])
    print(kthLargest.add(3))   # returns 4
    print(kthLargest.add(5))   # returns 5
    print(kthLargest.add(10))  # returns 5
    print(kthLargest.add(9))   # returns 8
    print(kthLargest.add(4))   # returns 8
    """

    def __init__(self, k: int, nums: List[int]):
        # minHeap w/ K largest integers
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]


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
    [[0, 1], [1, 0]]
    """
    distances = [(math.sqrt(x ** 2 + y ** 2), x, y) for x, y in points]
    heapq.heapify(distances)

    k_points = [[0, 0] for _ in range(k)]
    for i in range(k):
        closest_dist, x, y = heapq.heappop(distances)
        k_points[i] = ([x, y])
    return k_points


def find_kth_largest(nums: List[int], k: int) -> int:
    """
    Given an integer array nums and an integer k, return the kth largest element in the array.
    Note that it is the kth largest element in the sorted order, not the kth distinct element.
    Can you solve it without sorting?
    [MEDIUM] https://leetcode.com/problems/kth-largest-element-in-an-array/

    >>> find_kth_largest([3,2,1,5,6,4], 2)
    5
    >>> find_kth_largest([3,2,3,1,2,4,5,5,6], 4)
    4
    """
    heapq.heapify(nums)
    for _ in range(len(nums) - k):
        heapq.heappop(nums)
    return heapq.heappop(nums)


def least_interval(tasks: List[str], n: int) -> int:
    """
    You are given an array of CPU tasks, each represented by letters A to Z, and a cooling time, n.
    Each cycle or interval allows the completion of one task. Tasks can be completed in any order, but
    identical tasks must be separated by at least n intervals due to cooling time.
    Return the minimum number of intervals required to complete all tasks.
    [MEDIUM] https://leetcode.com/problems/task-scheduler/

    >>> least_interval(["A", "A", "A", "B", "B", "B"], 2)
    8
    >>> least_interval(["A", "C", "A", "B", "D", "B"], 1)
    6
    >>> least_interval(["A", "A", "A", "B", "B", "B"], 3)
    10
    """
    frequency = [0] * 26
    for task in tasks:
        frequency[ord(task) - ord("A")] += 1
    # formula explanation: https://medium.com/@satyem77/task-scheduler-leetcode-39d579f3440
    max_frequency = max(frequency)
    return max((max_frequency - 1) * (n + 1) + frequency.count(max_frequency), len(tasks))


class Twitter:
    """
    Design a simplified version of Twitter where users can post tweets, follow/unfollow another user,
    and is able to see the 10 most recent tweets in the user's news feed.
    [MEDIUM] https://leetcode.com/problems/design-twitter/
    """

    def __init__(self):
        self.followee = defaultdict(set)  # user id to set of follower ids
        self.tweets = defaultdict(list)  # user id to list of tweet ids
        self.counter = 0

    # Composes a new tweet with ID tweetId by the user userId.
    # Each call to this function will be made with a unique tweetId
    def post_tweet(self, user_id: int, tweet_id: int) -> None:
        self.tweets[user_id].append((tweet_id, self.counter))
        self.counter -= 1

    # Retrieves the 10 most recent tweet IDs in the user's news feed.
    # Each item in the news feed must be posted by users who the user followed or by the user themself.
    # Tweets must be ordered from most recent to least recent
    def get_news_feed(self, user_id: int) -> List[int]:
        # most recent tweets for each user
        tweets_heap = []
        self.followee[user_id].add(user_id)  # get own tweets
        for followee_id in self.followee[user_id]:
            if followee_id not in self.tweets:
                continue
            i = len(self.tweets[followee_id]) - 1
            # add follower id and tweet index to be able to replace popped tweet and counter for heap sort
            tweet_counter = self.tweets[followee_id][i][1]
            tweets_heap.append((tweet_counter, followee_id, i))

        heapq.heapify(tweets_heap)
        feed = []
        while len(tweets_heap) > 0 and len(feed) < 10:
            _, followee_id, i = heapq.heappop(tweets_heap)
            tweet_id = self.tweets[followee_id][i][0]
            feed.append(tweet_id)
            if i != 0:
                # add previous user tweet instead popped
                tweet_counter = self.tweets[followee_id][i - 1][1]
                heapq.heappush(tweets_heap, (tweet_counter, followee_id, i - 1))

        return feed

    # The user with ID followerId started following the user with ID followeeId
    def follow(self, follower_id: int, followee_id: int) -> None:
        self.followee[follower_id].add(followee_id)

    # The user with ID followerId started unfollowing the user with ID followeeId
    def unfollow(self, follower_id: int, followee_id: int) -> None:
        if followee_id in self.followee[follower_id]:
            self.followee[follower_id].remove(followee_id)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
